#!/usr/bin/env python3
import math

def calculate_factorial(n):
    if n < 0:
        return "Ошибка: Факториал отрицательного числа не определен"
    elif n == 0:
        return 1
    else:
        return math.factorial(n)

def main():
    print("=" * 50)
    print("Вычисление факториалов чисел от 0 до 10")
    print("=" * 50)
    
    for i in range(11):
        result = calculate_factorial(i)
        print(f"{i}! = {result}")
    
    print("\n" + "=" * 50)
    print("Дополнительный пример:")
    print(f"15! = {calculate_factorial(15):,}")
    print("=" * 50)

if __name__ == "__main__":
    main()
