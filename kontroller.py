import subprocess
import platform

def ping_address(address):
    if address == "":
        return False
    
    if platform.system() == "Windows":
        count = "-n"
    else:
        count = "-c"
    
    result = subprocess.run(
    ["ping",count,"1",address],
    capture_output=True,
    text=True
    )
    if result.returncode == 0:
        return True
    else:
        return False