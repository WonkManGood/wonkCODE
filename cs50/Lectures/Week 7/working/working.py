import re
import sys

regex_split = re.compile(r'[0-9|:|AM|PM]+')
regex_to = re.compile("-")

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if s.index("PM") or s.index("AM"): pass
    else: raise ValueError
    if re.search(regex_to, s): raise ValueError
    a, b, c, d, e, f, g, h= "", "", "", "", "", "", "", ""
    s = re.findall(regex_split, s)
    d = s[1]
    try: h = s[3]
    except: raise ValueError
    b, f = ":", ":"
    if ":" in s[0]: a, c = s[0].split(":")
    else: a = s[0]
    if ":" in s[2]: e, g = s[2].split(":")
    else: e = s[2]


    if c != "":
        c = int(c)
        if c >= 60: raise ValueError
    if g != "":
        g = int(g)
        if g >= 60: raise ValueError


    e = int(e)
    a = int(a)

    if a > 23: raise ValueError
    if e > 23: raise ValueError
    if d.lower() == "pm" and a < 12: a = a + 12
    if h.lower() == "pm" and e < 12: e = e + 12
    if a == 12 and d.lower() == "am": a = 0
    if e == 12 and h.lower() == "am": e = 0
    return f"{a:02}{b}{c:02} to {e:02}{f}{g:02}"

if __name__ == "__main__":
    main()
