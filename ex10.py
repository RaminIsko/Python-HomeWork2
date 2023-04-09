n = int(input("В-те кол-во монеток: "))
str = ""


print("\nВведите 0 или 1: ")

for i in range(n) :

    penny = int(input(f"{i + 1}. "))

    str += f"{penny} "

print(str)

countZero = 0
countOne = 0

for i in str :
    if(i == "0") :
        countZero += 1
    if(i == "1") :
        countOne += 1

if(countZero > countOne) :
    print(f"Сколько монет требуется перевернуть? -> {countOne}")
else :
    print(f"Сколько монет требуется перевернуть? -> {countZero}")

#Я не знаю функции пайтона поэтому решил сделать как-то так
    
    