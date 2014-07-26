"""
see: https://github.com/todbot/blink1/blob/master/docs/app-url-api.md
"""
from __future__ import absolute_import
from os.path import basename
from flask import Flask
from flask import request
from flask.ext import restful
from shell import shell

from parsers import RgbParserMixin


app = Flask(__name__)
app.config.from_object('config.Config')
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


class fadeToRGB(RgbParserMixin, restful.Resource):

    def post(self):
        args = self.parse_args()
        result = shell('blink1-tool --rgb %s' % args.rgb)
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
    app.run(
        debug=app.config['DEBUG'],
        host=app.config['HOST'],
        port=app.config['PORT'],
    )
