import subprocess
import sys

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'hikari'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'hikari-lightbulb'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'asyncio'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pynput'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gitdb'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Gitpython'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyautogui'])

subprocess.run(
    [
        "python", "./bot.py"
    ]
)