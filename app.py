"""
see: https://github.com/todbot/blink1/blob/master/docs/app-url-api.md
"""
from os.path import basename
from flask import Flask
from flask import request
from flask.ext import restful
from shell import shell


app = Flask(__name__)
api = restful.Api(app, prefix="/blink1")


class SimpleCommand(restful.Resource):
    "Simple commands, no specific argument"

    @property
    def command(self):
        return str(basename(request.path))

    def post(self):
        result = shell('blink1-tool --%s' % self.command)
        data = {'status': 'ok'}
        data['output'] = '\n'.join(result.output())
        return data

    def get(self):
        return self.post()

api.add_resource(
    SimpleCommand,
    '/on', '/off', '/white',
    '/red', '/green', '/blue',
    '/cyan', '/magenta', '/yellow',
    '/running', '/list',
)

if __name__ == '__main__':
    app.run(debug=True)
