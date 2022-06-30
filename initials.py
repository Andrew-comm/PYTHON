def initials(phrase):
    words=phrase.split()
    
    for word in words:
        result=word[0].upper()
        return result
print (initials("universal serial bus"))

