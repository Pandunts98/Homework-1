number = int(input("write a number : "))

sum_digits = 0

while number:
    sum_digits += number % 10
    number //= 10

print(sum_digits)

