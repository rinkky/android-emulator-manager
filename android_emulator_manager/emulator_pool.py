"""
Emulator pool.

Devices info is configured in a yaml file.

Environment variables `EMULATOR_POOL_CONFIG` define the config file path.
"""

import os
import re

from ruamel.yaml import YAML
from .manager import is_in_use

EMULATOR_POOL_CONFIG_ENV = 'EMULATOR_POOL_CONFIG'
pool_cfg_file = os.environ[EMULATOR_POOL_CONFIG_ENV]

def get_all():
    """get all devices that is not turned on
    
    returns:
    ```
        [
            {
                'id': 'emulator-5554',
                'port': 5554,
                'name': 'Android6.0',
                'version': '6.0'
            },
            {
                ...
            },
            ...
        ]
    ```
    """
    with open(pool_cfg_file) as file:
        cfg = YAML().load(file)
    devices = cfg['devices']
    off_devices = []
    for device in devices:
        device = dict(device)
        if not is_in_use(device['id']):
            off_devices.append(device)
    return off_devices

def get_one(version=None, id_=None):
    """get a device which is not turned on
    
    returns:
    ```
        {
            'id': 'emulator-5554',
            'port': 5554,
            'name': 'Android6.0',
            'version': '6.0'
        }
    ```
    """
    with open(pool_cfg_file) as file:
        cfg = YAML().load(file)
    devices = cfg['devices']
    for device in devices:
        if not is_in_use(device['id']):
            if version is not None and device['version'] != version:
                continue
            if id_ is not None and device['id'] != id_:
                continue
            return dict(device)
    return None

