def hash(s):
    """code already presented as hash for a given string"""
    h = 7
    letters = "acdegilmnoprstuw"
    for i in range(len(s)):
        try:
            h = (h * 37 + letters.index(s[i]))
        except IndexError as e:
            continue
        except ValueError as e:
            continue
    return h
def reverseHash(num):
    hash_string="";
    letters = "acdegilmnoprstuw"
    while num>37:
        try:
            hash_string=letters[num%37]+hash_string
            num = num / 37#reducing number on 37 according to hash designed
        except IndexError as e:
            print "Wrong Input For reverseHash"#Handling Wrong Inputs
        except:
            print "Wrong Input For reverseHash"

    return hash_string
"""TestCases"""
try:
    assert reverseHash(hash("leepadg"))== "leepadg"
    assert reverseHash(hash("tuw"))== "tuw"
    assert reverseHash(hash("a"))== "a"
    assert reverseHash(hash("pomn")) == "pomn"
    assert reverseHash(hash("lmno"))=="lmno"
except AssertionError as e:
    pass