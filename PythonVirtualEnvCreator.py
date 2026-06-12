import subprocess
import sys

subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
subprocess.run([r"venv\Scripts\python.exe", "-m", "pip", "install", "pandas"], check=True)
