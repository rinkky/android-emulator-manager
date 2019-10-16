import os
import subprocess

def run(avd, port=5554):
    cmd = 'start emulator -avd {} -port {}'.format(avd, port)
    os.system(cmd)
    
def stop(did=None):
    if did:
        cmd = 'adb -s {} emu kill'.format(did)
    else:
        cmd = 'adb emu kill'
    os.system(cmd)

def shutdown(did=None):
    if did:
        cmd = 'adb -s {} shell reboot -p'.format(did)
    else:
        cmd = 'adb shell reboot -p'
    os.system(cmd)

def available(did=None):
    if did:
        cmd = 'adb -s {} shell getprop sys.boot_completed'.format(did)
    else:
        cmd = 'adb shell getprop sys.boot_completed'
    try:
        cmd_out, cmd_err = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate(timeout=3)
        cmd_out = cmd_out.decode().strip() if cmd_out else ''
        if cmd_out and (cmd_out.split()[-1] == '1'):
            return True
    except subprocess.TimeoutExpired:
        pass
    return False

def killall():
    os.system('taskkill /F /T /IM emulator.exe')
