import re
def mask_email(match):
    email = match.group()
    name, domain = email.split('@')
    if len(name) > 2:
        masked_name = name[0] + "*"*(len(name)-2) + name[-1]
    else:
        masked_name = name
    return masked_name + '@' + domain
pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
text = "helloworld@python.com and sumirtha@gmail.com."
masked = re.sub(pattern, mask_email, text)
print(masked)