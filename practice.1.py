yearAge = int(input("Enter your age/Year of birth?"))
isAge = False
isYear = False

if len(str(yearAge))==4:
    isYear = True

else:
    isAge = True

if (yearAge<1900 and isYear):
    print("you seem to be the oldest person alive")
    exit()

if (yearAge>2021):
    print("yet to be born ")
    exit()

if isAge:
    yearAge = 2021 - yearAge

print(f"You will be 100 years old in {yearAge + 100}")

interestedYear = int(input("Enter the year you want to know your age in\n"))

print(f"You will be {interestedYear - yearAge} years old in {interestedYear}")
