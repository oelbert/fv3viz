from . import cubedsphere
from .xarray_loaders import open_tiles, open_delayed, open_remote_nc, dump_nc
from .cloud import get_fs
from .cloud.fsspec import to_url

__all__ = [item for item in dir() if not item.startswith("_")]
__version__ = "0.1.0"
