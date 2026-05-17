# 1. შეინახეთ ცვლადებში ცვლადების ტიპები მათი მნიშვნელობების ნაცვლად

var1 = 1
var2 = -1
var3 = True
print(var1, var2, var3)

var1 = type(var1)
var2 = type(var2)
var3 = type(var3)
print(var1, var2, var3)

# 2. შეცვალეთ ცვლადების ტიპები (type casting-ის მეშვეობით)

var4 =False # გადაიყვანეთ Float -ში
var5 =3 # გადაიყვანეთ Float -ში
var6 = {"key":"value", "key1":"value", "key3":"value"} # გადაიყვანეთ list -ში
print(var4, var5, var6)

var4 = float(var4)
var5 = float(var5)
var6 = list(var6)
print(var4, var5, var6)

# 3. შექმენით შესაფერისი ტიპის ცვლადები მონაცემებისთვის.

name = "Python2023"
count = 35
male = 22
female = 13
students = ["student1", "student2", "student3", "student4", "student5"]
ages = [24, 33, 15, 45, 42]

print(name)
print(count)
print(male)
print(female)
print(students)
print(ages)

# 4. დააფორმატეთ სტრიქონი და გამოითვალეთ თქვენი ასაკი
def calc()
    birth_year = int(input("please enter your birth year: "))
    name = input("please enter your name: ")
    surname = input("please enter your surname: ")
    current_year = int(input("please enter current year: "))
    age = current_year - birth_year
    print(f'{name} {surname} is {age} years old and is born in {birth_year}.')

calc()
# 5. გამოითვალეთ მომხრეთა და მოწინააღმდეგეთა პროცენტი და აჩვენეთ ორივე.
# (შეეცადეთ დაამრგვალოთ პროცენტები მეასედებამდე)

Yes = 119
No = 82
print("yes:",Yes/(Yes+No)*100 )
print("no:",No/(Yes+No)*100)
print("yes:",round(Yes/(Yes+No)*100,2) )
print("no:",round(No/(Yes+No)*100,2))

# 6. გადაიყვანეთ 3670 წამი საათებად და წუთებად

seconds = 3670
hours = (seconds // 3600)
minutes = (seconds % 3600) // 60
remaining = seconds % 60
print(f"{hours:02}:{minutes:02}:{remaining:02}")
print(f"{hours:02} საათი {minutes:02} წუთი {remaining:02} წამი")

# 7. გამოიტანეთ სტრიქონის პირველი და ბოლო ასო

text = "Python"
print(text[0],text[-1])

# 8. გამოითვალეთ სასწავლო საგნის შეფასების პროცენტული წილი

math = 45
total = 60
print("პროცენტი:",math / total * 100)

# 9. გამოითვალეთ ასაკი მომავალ წელს

birth_year = 2000
current_year = 2025
next_year = current_year + 1
age = next_year - birth_year
print(f"“მომავალ წელს შენ იქნები {age} წლის”")

def ages_calc():
    birth_date = int(input("please enter your birth year: "))
    this_year = int(input("please enter current year: "))
    age = this_year + 1 - birth_year
    print(f"მომავალ წელს შენ იქნები {age} წლის")

ages_calc()

# 10. 350 წუთი რამდენი საათია და რამდენი წუთი დარჩება გამოიტანეთ

minute = 350
hours = minute // 60
left_minute = minute % 60
print(f"{hours:02}:{left_minute:02}")
print(f"{hours:02} საათი {left_minute:02} წუთი")

