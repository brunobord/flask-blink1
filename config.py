from default_config import Config
try:
    from local_config import Config  # noqa
except ImportError:
    pass
