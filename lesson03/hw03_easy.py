# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):             
    new_number = number * 10**(ndigits+1)  
    idx = int(new_number) % 10             
    if idx >= 5:                           
        new_number = new_number // 10 + 1  
    else:                                  
        new_number = new_number // 10      
                                           
    return new_number / 10**ndigits        


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    left_nbr = 0
    right_nbr = 0
    ticket_str = str(ticket_number)
    idx = 0
    count = int(len(ticket_str) / 2 - 1)
    while idx <= count:
        left_nbr += int(ticket_str[idx])
        right_nbr += int(ticket_str[idx+count+1])
        idx+=1

    return "Билет счастливый" if left_nbr == right_nbr else "Билет НЕ счастливый"


print(lucky_ticket(123006))
print(lucky_ticket(123321))
print(lucky_ticket(436751))

