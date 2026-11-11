import subprocess
import platform
import os

def ping_address(address):
    if address == "":
        return False
    
    count = None
    if os.name == "nt":
        count = "-n"
    elif os.name == "posix":
        count = "-c"
    else:
        raise OSError("Unsupported operating system")
    
    result = subprocess.run(
    ["ping",count,"1",address],
    capture_output=True,
    text=True
    )
    if result.returncode == 0:
        return True
    else:
        return False