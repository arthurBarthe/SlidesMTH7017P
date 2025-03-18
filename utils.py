import logging
import warnings
warnings.simplefilter('ignore')

import cartopy.crs as ccrs
import pickle
from pathlib import Path


import climada
logging.getLogger("climada").setLevel(logging.CRITICAL)

def set_cache_dir(path):
    global CACHE_DIR
    CACHE_DIR = Path(path)


def get_projection(name: str = 'Mollweide'):
    projection = getattr(ccrs, name)()
    return projection



def load_from_cache(name):
    with open(CACHE_DIR / name, 'rb') as f:
        return pickle.load(f)

def save_to_cache(name, var):
    with open(CACHE_DIR / name, 'wb') as f:
        pickle.dump(var, f)