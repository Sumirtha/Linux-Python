import re
dna = "ATCGCGAATTCAC"
pattern = r'GGACC|GGTCC'
if re.search(pattern, dna):
    print("AvaII site found")
else:
    print("No AvaII site found")