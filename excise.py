
f = open("words.txt", "r")
out = open("4words.txt", "w")

for line in f:
    if len(line) == 5:
        out.write(line)

f.close()
out.close()
