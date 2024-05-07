def transformSentence(sentence):
    splittedSentence = sentence.split(" ")
    resultStr = ""
    for val in splittedSentence:
        resultStr += val[0]
        if len(val) > 1:
            l = 0
            for i in range(1, len(val)):
                if val[l].lower() < val[i].lower():
                    resultStr += val[i].upper()
                elif val[l].lower() == val[i].lower():
                    resultStr += val[i]
                else:
                    resultStr += val[i].lower()
                l += 1
        resultStr += " "
    return resultStr


print(transformSentence("a Blue MOON"))
