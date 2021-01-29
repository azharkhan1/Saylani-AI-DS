def punctuationCount(str):
    count = 0
    punctuations = []
    for i in range (0, len(str)):
        if str[i] in ("," , "," , "/`" , "\'" , ";" , "." , "-" , "?"):
                       count = count + 1
                       punctuations.append(str[i])
        return count
                       
                       
def removePunctuation(str):
    count=list(str)
    removedPunctuation = []
    for i in range(0 , len(str)):
        if str[i] not in ("," , "." , "/'" , "\'" , ";" , "." , "-" , "?"):
            removedPunctuation.append(str[i])
    return removedPunctuation
