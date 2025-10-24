import re
pattern = r'^(25[0-5]|2[0-4][0-9]|1\d{2}|0\d{2}|00[0-9])$'
sample = ["000", "0", "69", "255", "300", "abc"]
#sample = input("Enter a number:" )
for s in sample:
    if re.match(pattern, s):
        print(f"{s} Valid")
    else:
        print(f"{s} Invalid")