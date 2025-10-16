f = open("stringmatrix.dat", "w")
ascii_A = 65
for i in range(3):
     row = [chr(ascii_A + j) for j in range(i * 4, (i + 1) * 4)]
     f.write(" ".join(row) + "\n")
f.close()