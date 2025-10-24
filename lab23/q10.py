import re
dna = "ATCGCGYAATTCAC"
pattern = r'[^ATGC]'
ambiguous = re.findall(pattern, dna)
if ambiguous:
    print("Contains ambiguous bases:", ambiguous)
else:
    print("No ambiguous bases found")