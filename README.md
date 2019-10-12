# Android Emulator Manager

Run and stop official android emulator on Windows.

## setup

```python
python setup.py install
```

## usage

```python
import android_emulator_manager

android_emulator_manager.run('pixel2', port=5554)
android_emulator_manager.stop('emulator-5554')
```
