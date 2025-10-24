import re
pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
sample = input("Enter a line:" )
emails = set(re.findall(pattern, sample))
print("Unique emails found:", emails)