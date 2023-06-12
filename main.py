# На 3
a = float(input("Введите значение для a: "))
b = float(input("Введите значение для b: "))

equation1 = (a - b) * (a + b)
equation2 = a**2 - 2*a*b + b**2
equation3 = a**2 + 2*a*b + b**2
equation4 = a**3 - 3*a**2*b + 3*a*b**2 - b**3
equation5 = a**3 + 3*a**2*b + 3*a*b**2 + b**3
equation6 = (a + b) * (a**2 - a*b + b**2)
equation7 = (a - b) * (a**2 + a*b + b**2)

print("Результаты выражений:")
print("1. (a - b) * (a + b) =", equation1)
print("2. a^2 - 2ab + b^2 =", equation2)
print("3. a^2 + 2ab + b^2 =", equation3)
print("4. a^3 - 3a^2b + 3ab^2 - b^3 =", equation4)
print("5. a^3 + 3a^2b + 3ab^2 + b^3 =", equation5)
print("6. (a + b)(a^2 - ab + b^2) =", equation6)
print("7. (a - b)(a^2 + ab + b^2) =", equation7)

