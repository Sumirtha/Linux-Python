import re
dna = "ATCGCGAATTCAC"
pattern = r'GAATTC'
if re.search(pattern, dna):
    print("EcoRI site found")
else:
    print("No EcoRI site found")