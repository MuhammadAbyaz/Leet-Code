_, disinfectant = map(int, input().split(" "))
aliens = map(int, input().split(" "))
count = 0
for alien in aliens:
    if disinfectant > 0 and disinfectant >= alien:
        disinfectant -= alien
        count += 1
print(count)


string = input()
u_count = 0
l_count = 0
for val in string:
    ascii = ord(val)
    if ascii >= 65 and ascii <= 90:
        u_count += 1
    else:
        l_count += 1
if u_count > l_count:
    print(string.upper())
else:
    print(string.lower())
