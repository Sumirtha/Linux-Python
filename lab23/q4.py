import re
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
line = "Sums,20,sums.joyce@gmail.com,Zoologist"
fields = line.split(',')
if len(fields) > 3 and re.match(pattern, fields[2].strip()):
    print("3rd field contains a valid email")
else:
    print("3rd field does not contain a valid email")