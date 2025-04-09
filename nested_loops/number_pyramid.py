n = int(input())
current = 1
is_current_num_bigger_than_n = False

#За да излезем и от двата цикъла трябва да използваме оператора break и в двата
for row in range(1, n+1):   #външният цикъл ще определя колко реда да се отпечатат
    for column in range(1, row+1):  #вътрешният – колко числа се принтират на съответния ред
        if current > n:
            is_current_num_bigger_than_n = True
            break
        print(str(current) + ' ', end="")   # we transform it to str so we can add space
        current += 1
#В тялото на външния цикъл направете проверка дали трябва да излезем и от него.\
# След това отпечатйте един празен ред, за да може следващите числа да са на нов ред.\
# Ако сме излeзли от външния цикъл, няма да се стигне до изпълнение на командата print()
    if is_current_num_bigger_than_n:
        break
    print()