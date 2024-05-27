# Birth Day and age Calculator

from datetime import date

def days_till_birthday(birthdate):
    today = date.today()
    birthday_date = date(today.year,birthdate.month,birthdate.day)
    if birthday_date < today:
        nxt_birthday = date(today.year + 1,birthdate.month,birthdate.day)
    else:
        nxt_birthday = birthday_date
    days_left = (nxt_birthday - today).days
    #print(f"Days till next birthday: {days_left} days")
    return days_left

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
        return age 
    
day = int(input("Enter your day of birth: "))
month = int(input("Enter your month of birth: "))
year = int(input("Enter your year of birth: "))

birthdate = date(year,month,day)
days_left = days_till_birthday(birthdate)
age = calculate_age(birthdate)

print(f"Days till your next birthday: {days_left} days")
print(f"So, your age is: {age} years old")



