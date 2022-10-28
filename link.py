import os
import subprocess
from unittest import result

result = subprocess.run(["host", "127.0.0.1"], capture_output=True)
print(result.stdout.decode().split())