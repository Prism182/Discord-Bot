from pynput.keyboard import Key, Controller
import time
import subprocess



keyboard = Controller()

time.sleep(4)



print("received")
print("running server startup")


#set to file directory
subprocess.run(
        [
            r"C:\\Users\\Kyle Foster\\OneDrive\\Documents\\Server\\run.bat"
        ]
    )

time.sleep(10)

subprocess.run(
    [
        "python", ".\bot.py"
    ]
)
