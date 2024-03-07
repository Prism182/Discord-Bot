import time

#!/usr/bin/env python3
NULL_CHAR = chr(0)

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

# Press WINDOWS key
write_report(NULL_CHAR*2+chr(216)+NULL_CHAR*5)
# Press r key
write_report(NULL_CHAR*2+chr(21)+NULL_CHAR*5)
# Release keys
write_report(NULL_CHAR*8)

# Press c
write_report(NULL_CHAR*2+chr(6)+NULL_CHAR*5)
# Release keys
write_report(NULL_CHAR*8)

#Press m
write_report(NULL_CHAR*2+chr(16)+NULL_CHAR*5)
# Release keys
write_report(NULL_CHAR*8)

#Press d
write_report(NULL_CHAR*2+chr(7)+NULL_CHAR*5)
# Release keys
write_report(NULL_CHAR*8)

time.sleep(5)

# Press c key
write_report(NULL_CHAR*2+chr(6)+NULL_CHAR*5)
# Press d key
write_report(NULL_CHAR*2+chr(7)+NULL_CHAR*5)

# Press RETURN/ENTER key
write_report(NULL_CHAR*2+chr(40)+NULL_CHAR*5)

# Press e key
write_report(NULL_CHAR*2+chr(8)+NULL_CHAR*5)
# Press f key
write_report(NULL_CHAR*2+chr(9)+NULL_CHAR*5)

# Release all keys
write_report(NULL_CHAR*8)

