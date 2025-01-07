import re

def main():
    print(parse(input("HTML: ")))


def parse(source):
    if link := re.search(r"<iframe src=\"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"></iframe>", source):
        return (f"https://youtu.be/{link.group(2)}")


if __name__ == "__main__":
    main()
