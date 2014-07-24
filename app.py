"""
see: https://github.com/todbot/blink1/blob/master/docs/app-url-api.md
"""
from flask import Flask
from flask.ext import restful
from shell import shell

app = Flask(__name__)
api = restful.Api(app, prefix="/blink1")


class SimpleCommandMixin(object):
    def post(self):
        out = shell('blink1-tool --%s' % self.command)
        print out.output()
        return {'status': 'ok'}


class SimpleCommand(SimpleCommandMixin, restful.Resource):
    def get(self):
        return self.post()

    def post(self):
        return super(SimpleCommand, self).post()


class On(SimpleCommand):
    command = 'on'


class Off(SimpleCommand):
    command = 'off'


class Red(SimpleCommand):
    command = 'red'


api.add_resource(On, '/on')
api.add_resource(Off, '/off')
api.add_resource(Red, '/red')

if __name__ == '__main__':
    app.run(debug=True)
