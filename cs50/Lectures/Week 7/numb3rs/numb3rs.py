import re
import sys

def main():
    print(validate(input("IPv4 Address: ")), end="")

def validate(ip):
    if re.search(r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ip):
        try: a = ip.split(".")
        except: return False
        if len(a) > 4: return False
        for number in a:
            if int(number) > 255:
                return False
        else: return True
    else: return False

if __name__ == "__main__":
    main()
