givenScore = int(input("Please enter your marks : "))
if givenScore >= 90 and givenScore <= 100:
    print("Your Grade : A")
elif givenScore >= 80 and givenScore < 90:
    print("Your Grade : B")
elif givenScore >= 70 and givenScore < 80:
    print("Your Grade : C")
elif givenScore >= 60 and givenScore < 70:
    print("Your Grade : D")
else :
    print("Your Grade : F")
