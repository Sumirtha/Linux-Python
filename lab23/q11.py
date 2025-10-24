import re
dna = "ACTNGCATRGCTACGTYACGATSCGAWTCG"
nicks = re.split(r'[^ATGC]+', dna)
nicks = [n for n in nicks if n]
print(nicks)