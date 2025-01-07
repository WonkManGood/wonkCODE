inp = str(input("Filename: ")).lower().strip(" ")

if inp.endswith(".gif") is True:
    print("image/gif", end="")
elif inp.endswith(".jpg") is True:
    print("image/jpeg", end="")
elif inp.endswith(".jpeg") is True:\
    print('image/jpeg', end="")
elif inp.endswith(".png") is True:\
    print("image/png", end="")
elif inp.endswith(".pdf") is True:
    print("application/pdf", end="")
elif inp.endswith(".txt") is True:\
    print("text/plain", end="")
elif inp.endswith(".zip") is True:\
    print("application/zip", end="")
else:
    print("application/octet-stream", end="")
