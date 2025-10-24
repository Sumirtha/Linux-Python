import re
pattern = r'^(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)$'
sample = input("Enter a number:" )
for s in sample:
    if re.match(pattern, s):
        print(f"{s} Valid")
    else:
        print(f"{s} Invalid")