"""
see: https://github.com/todbot/blink1/blob/master/docs/app-url-api.md
"""
from os.path import basename
from flask import Flask
from flask import request
from flask.ext import restful
from flask.ext.restful import reqparse
from shell import shell
import htmlcolor


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


class fadeToRGB(restful.Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('rgb', type=str)
        args = parser.parse_args()
        color_parser = htmlcolor.Parser()
        color = ','.join(map(str, color_parser.parse(args.rgb)))
        result = shell('blink1-tool --rgb %s' % color)
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

api.add_resource(fadeToRGB, '/fadeToRGB')

if __name__ == '__main__':
    app.run(debug=True)
