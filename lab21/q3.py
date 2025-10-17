class AgeTooYoungError(Exception):
    pass
def checkAge(age):
    try:
        if age < 18:
            raise AgeTooYoungError("Age must be more than 18")
        else:
            print("Age is valid.")
    except AgeTooYoungError as e:
        print("Error:", e)

checkAge(3)