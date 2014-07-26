from flask.ext.restful import reqparse
import htmlcolor
from flask.ext import restful


def get_color_from_args(rgb):
    """Extract a color tuple out of a raw string argument.
    """
    if len(rgb.split(',')) == 3:
        rgb = map(int, rgb.split(','))
        if max(rgb) <= 255 and min(rgb) >= 0:
            return ','.join(map(str, rgb))
    color_parser = htmlcolor.Parser()
    color = ','.join(map(str, color_parser.parse(rgb)))
    return color


class ParserMixin(object):
    @property
    def parser(self):
        return reqparse.RequestParser()

    def parse_args(self):
        args = self.parser.parse_args()
        return args


class RgbParserMixin(ParserMixin):

    @property
    def parser(self):
        parser = super(RgbParserMixin, self).parser
        parser.add_argument('rgb', type=str, required=True)
        return parser

    def parse_args(self):
        args = super(RgbParserMixin, self).parse_args()
        if not args.rgb:
            msg = "Missing required parameter rgb in json or the post body" \
                  " or the query string"
            restful.abort(400, message=msg)

        try:
            color = get_color_from_args(args.rgb)
        except:
            msg = "Malformed color code. Please refer to a CSS-compatible" \
                  " color specification (#ff0095, #fcb, 255,200,33...)."
            restful.abort(400, message=msg)

        args.rgb = color
        return args
