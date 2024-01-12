deposit = input("Укажите сумму вклада:")
deposit = float(deposit)
validity = input("Укажите срок вклада в форате ГГ")
validity = int(validity)
interest_on_deposit = 10

print("Ваш вклад", deposit, "Сроком на ", validity, "Года", "Под годовой процент", interest_on_deposit, "%")

def bank(deposit, validity):
   for _ in range(validity):
     deposit = deposit + deposit*0.1
   return(deposit)
print("Итоговая сумма", bank(deposit, validity))
