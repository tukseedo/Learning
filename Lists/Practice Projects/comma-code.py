def commaSeperator(listOfStuff):
    sumStr = ''
    for ls in listOfStuff:
        if ls == listOfStuff[len(listOfStuff) - 1]:
            sumStr += 'and ' + ls
            break
        sumStr += ls + ', '
    return sumStr

spam = ['apples', 'bananas', 'tofu', 'cats']
print(commaSeperator(spam))