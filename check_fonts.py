# check_fonts.py
import os
fonts = os.popen('reg query "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Fonts"').read()
for line in fonts.splitlines():
    if "rbit" in line or "ajdh" in line:
        print(line)