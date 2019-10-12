import os

def run(avd, port=5554):
    cmd = 'start emulator -avd {} -port {}'.format(avd, port)
    os.system(cmd)
    
def stop(did=None):
    if did:
        cmd = 'adb -s {} emu kill'.format(did)
    else:
        cmd = 'adb emu kill'
    os.system(cmd)
