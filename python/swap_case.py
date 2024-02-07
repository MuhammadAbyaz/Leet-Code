string = "Hello World"

new_string = []
for i in string:
    if i == i.upper():
        new_string.append(i.lower())
    elif i == " ":
        new_string.append(i)
    else:
        new_string.append(i.upper())

print("".join(new_string))
