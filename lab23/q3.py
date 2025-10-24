import re
pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
email = input("Enter your email: ")
match = re.findall(pattern, email)
print(email)
if re.search(pattern, email):
    print("Email found")
else:
    print("No email found")