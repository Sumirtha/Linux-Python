import re
dna = "ATCGCGAATTCAC"
pattern = r'GC[ATGC]GC'
if re.search(pattern, dna):
    print("BisI site found")
else:
    print("No BisI site found")