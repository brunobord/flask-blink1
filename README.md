# Flask / Blink1

As stupid as it sounds, it's a Flask app that mimics the blink1 server.

## Why?

* Because it looks like there's no headless HTTP server available for

## Install

You'll need at least the [blink1-tool binary](https://github.com/todbot/blink1)in your path. I hope that one day I could use the native [Python lib](https://github.com/todbot/blink1/tree/master/python/pypi), but at the moment it's so buggy that I'm helpless.

Preferrably in a virtualenv, install the requirements with the command:

```
pip install -r requirements.txt
```

## Usage

1 - Plug your *blink1 mk2*.

2 - Run the server with:

```
python app.py
```

3 - Using a browser or the [amazing httpie tool](https://github.com/jakubroztocil/httpie), point to your ``http://localhost:5000/blink1/on``

4 - Let there be the light!

## Available methods

- ``/blink1/on``
- ``/blink1/off``
- ``/blink1/red``

## TODO

- Every other method available in the ``blin1-tool``, including optional arguments,
- server response should mimic the BlinkControl HTTP server responses,
- add a way to configure things (ports, prefixes, auth?)

## License

This code is published under the terms of the [WTFPL](http://www.wtfpl.net/).

![WTFPL](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png)
