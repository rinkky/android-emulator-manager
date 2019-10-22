# Android Emulator Manager

Run and stop official android emulator on Windows.

## setup

```python
python setup.py install
```

## basic usage

```python
import android_emulator_manager

android_emulator_manager.run('pixel2', port=5554)
android_emulator_manager.stop('emulator-5554')
```

## emulator pool usage

```python
from android_emulator_manager import emulator_pool
device = emulator_pool.get_one()
all_device = emulator_pool.get_all()
```
