a=list(range(1,51))
#,
comma=",".join([str(num) for num in a])
print(comma)
#.
period=".".join([str(num) for num in a])
print(period)
#_
dash="_".join([str(num) for num in a])
print(dash)
#square
square="\n".join([f"{num} {num**2}" for num in a])
print(square)
#list of people
people=["sumirtha joyce","george abraham","winfred mathew","manjula ruth","kishore kailash","sharon sheeba","rida khan",
        "alexander varuvel","william stains","muruga anand"]
#upppercase
uppercase=[person.upper() for person in people]
print(uppercase)
#swap
swap=[" ".join(person.split()[::1]) for person in people]
print(swap)
#first.last
#first_last=["{}.{}".format(p.split()[0].capitalize(), p.split()[1].capitalize()) for p in people]
#print(first_last)
#sentence
sentence="she sells sea shells on the sea shore"
words=sentence.split()
longest=max([word for word in words], key=len)
print(longest)
repeat=list(set([word for word in words if words.count(word)>1]))
print(repeat)