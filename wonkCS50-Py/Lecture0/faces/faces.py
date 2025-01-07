def main():
    text = str(input())
    print(convert(text))
def convert(n):
    return n.replace(':(', '🙁').replace(':)', '🙂')

main()
