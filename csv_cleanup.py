import csv

new = []

with open(...) as a:
    with open("output.csv", "w", newline="") as b:
        c = csv.reader(a)
        d = csv.writer(b)
        for line in c:
            try: new.index(line)
            except: new.append(line)
        for line in new: d.writerow(line)