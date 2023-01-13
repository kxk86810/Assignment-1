givenString = input("Enter a string:")
l = len(givenString)
if l>2:
    stringTrim = givenString[:l-2]
    strRev = stringTrim[::-1]
    print("Final Output: ",strRev)
else:
    print("Please enter a string with valid length")