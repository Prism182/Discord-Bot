import time

#!/usr/bin/env python3
NULL_CHAR = chr(0)

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

# Press Windows + R keys
write_report(chr(216)+NULL_CHAR+chr(21)+NULL_CHAR*5)
# Release keys
write_report(NULL_CHAR*8)
# Press c key
write_report(NULL_CHAR*2+chr(6)+NULL_CHAR*5)
# Release keys
write_report(NULL_CHAR*8)
# Press m key
write_report(NULL_CHAR*2+chr(16)+NULL_CHAR*5)
# Press d key
write_report(NULL_CHAR*2+chr(7)+NULL_CHAR*5) 

time.sleep(2)

# Press Shift + C key
write_report(chr(214)+NULL_CHAR+chr(6)+NULL_CHAR*5)
# Press shift + ; key
write_report(chr(214)+NULL_CHAR+chr(193)+NULL_CHAR*5)
# Press / key
write_report(NULL_CHAR*2+chr(56)+NULL_CHAR*5)

# Release all keys
write_report(NULL_CHAR*8)