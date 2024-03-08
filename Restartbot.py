import subprocess
import asyncio

asyncio.sleep(0.1)
subprocess.run(
    [
        "python", "./bot.py"
    ]
)
print("received")