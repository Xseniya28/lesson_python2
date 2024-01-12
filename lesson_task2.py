year = input("Укажите год ")
year = int(year)
def is_year_leap(year):
    if year % 4 == 0 :
        return True
    else:
        return False
result=is_year_leap(year)
print("Год: " + str(year) + " : "+ str(result))