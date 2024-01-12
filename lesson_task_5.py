month =  input("Укажите номер месяца:")
month = int(month)
def month_to_season(month):
       if month == 12 and month <=2 :
         return ("Зима")
       elif month >=3 and month <=5:
         return("Весна")
       elif month >=6 and month <=8:
         return("Лето")
       elif month >=9 and month <=11:
         return("Осень") 
print(month_to_season(month))
