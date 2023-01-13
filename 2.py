txt = input("Enter the String: ")
chooseStrng = input("Choose Substring to replace: ")
if chooseStrng in txt:
    strReplace = input("Enter new Substring: ")
    newTxt = txt.replace(chooseStrng, strReplace)
    print(newTxt)
else:
    print("The substring is not present in given text")