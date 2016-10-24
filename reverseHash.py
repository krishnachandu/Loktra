def reverseHash(num):
    hashStr="";
    letters = "acdegilmnoprstuw"
    while num>37:
        inpStr=letters[num%37]+hashStr
        num = num / 37
    return hashStr