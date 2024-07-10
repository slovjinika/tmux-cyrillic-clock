import subprocess
import time

python_interpreter = "/usr/bin/python3"
script_path = f"/data/data/com.termux/files/home/storage/shared/Github/dec2cyrs/dec2cyrs.py"

result1 = subprocess.check_output([python_interpreter, script_path, '-t', time.strftime('%H')]).decode('utf-8').strip()
result2 = subprocess.check_output([python_interpreter, script_path, '-t', time.strftime('%M')]).decode('utf-8').strip()

print(result1 + ":" + result2)
