def replaceWords(dictionary: list[str], sentence: str) -> str:
    splittedSentences = sentence.split(" ")
    for val in dictionary:
        for i in range(len(splittedSentences)):
            if (
                len(val) <= len(splittedSentences[i])
                and splittedSentences[i][0 : len(val)] == val
            ):
                splittedSentences[i] = val
    return " ".join(splittedSentences).strip()


print(replaceWords(["a", "b", "c"], "aadsfasf absbs bbab cadsfafs"))
