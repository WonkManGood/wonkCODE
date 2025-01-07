import sys
import pyfiglet
try:
    font_flag = str(sys.argv[1])
    inputted_font = str(sys.argv[2])
    msg = input("")
except IndexError:
    sys.exit(1)

if font_flag == "-f":
    out = str(pyfiglet.print_figlet(msg, font=inputted_font))
    out = out.replace("None", "")
    print(out)
if font_flag != "-f":
    print("Incorrect args")
    sys.exit(1)
