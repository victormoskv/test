import random
print("Укажите правую границу для рандомного числа")
n=int(input())
a=random.randint(1,n)
print("Добро пожаловать в числовую угадайку")
def is_valid(b,n):
    if int(b)>n or int(b)<1:
        return False
    else:
        return True
c=0
counter=0
while a!=c:
    counter+=1
    print("Введите число от 1 до",n )
    b=input()
    if is_valid(b,n)==False:
        print("А может быть все-таки введем целое число от 1 до",n)
        continue
    else:
        c=int(b)
        if c<a :
            print("Ваше число меньше загаданного попробуйте еще раз")
            continue
        if c > a :
            print("Ваше число больше загаданного попробуйте еще раз")
            continue
        else:
            print("количество попыток равно "+ str(counter),"Вы угадали,поздравляем!","Спасибо что играли в числовую угадайку.Еще увидемся...",sep="\n")
            print("Хотите играт? д/н")
            p=input()
            if p=='д':
                print("Укажите правую границу для рандомного числа")
                n=int(input())
                a=random.randint(1,n)



