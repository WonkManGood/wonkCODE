import re

def main():
    if is_valid(input("Enter Plate Number: ")):
        print("Valid")
    else: print("Invalid")

numbers = re.compile(r"[0-9]")
banned = re.compile(r"[\.|\s|?|!|,]")
a = "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"
def is_valid(s):
    s = str(s)
    if 2 <= len(s) <= 6:
        if s[0:1].isalpha():
            if s[0] != "0":
                try:
                    b = re.findall(r"(\d)", s)
                    if b[0] == "0":
                        return False
                except: return False
                if re.search(numbers, s) and s.endswith(a) != True:
                    return False
                elif re.search(banned, s) == True:
                    return False
                else:
                    return True
            else: return False
        else: return False
    else: return False


if __name__ == "__main__":
    main()
    
