import os
import sys


python_path = os.path.dirname(sys.executable)
python_version = sys.version


print(f'Path to Interpretator: {python_path}, \nVersion: {python_version}')