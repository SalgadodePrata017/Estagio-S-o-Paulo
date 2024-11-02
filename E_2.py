user_num = int(input("Insira um número e diremos se ele faz parte da sequência de Fibonacci: "))
print()

num1 = 0
num2 = 1
num3 = 1

print(num1)
print(num2)
print(num3)
fibonacci = 0
num1 = num2 + num3
num3 = num1 + num3
print(num1)
print(num3)


while num3 <  user_num:
    # bloco de codigo a ser executado
    num1 = num1 + num3
    print(num1)
    num3 = num1 + num3
    print(num3)

if num1 == user_num:
    print()
    print("O número pertence a sequência de Fibonacci!")
elif num3 == user_num:
    print()
    print("O número pertence a sequência de Fibonacci!")
elif 0 == user_num:
    print()
    print("O número pertence a sequência de Fibonacci!")
elif 1 == user_num:
    print()
    print("O número pertence a sequência de Fibonacci!")
elif 2 == user_num:
    print()
    print("O número pertence a sequência de Fibonacci!")
elif 3 == user_num:
    print()
    print("O número pertence a sequência de Fibonacci!")
elif num1 != user_num:
    print()
    print("O número não pertence a sequência de Fibonacci")
elif num3 != user_num:
    print()
    print("O número não pertence a sequência de Fibonacci")