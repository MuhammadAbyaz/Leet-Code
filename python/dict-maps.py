phoneBook = {}
n = int(input())
for _ in range(n):
    userInput = input().split(" ")
    phoneBook[userInput[0]] = int(userInput[1])
inputList = []
userInput = input()
inputList.append(userInput)
try:
    while userInput:
        userInput = input()
        inputList.append(userInput)
except Exception as e:
    pass
finally:
    for val in inputList:
        if val:
            if phoneBook.get(val):
                print(f"{val}={phoneBook.get(val)}")
            else:
                print("Not found")
