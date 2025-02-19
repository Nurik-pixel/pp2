#1
def square_generator(N):
	for i in range(N + 1):
		yield i ** 2

N = int(input("Enter a number: "))
print("Squares up to", N, ":")
for value in square_generator(N):
	print(value)

#2
def even_numbers(n):
	for i in range(0, n + 1, 2):
		yield i

n = int(input("Enter a number: "))
print(", ".join(map(str, even_numbers(n))))

#3
def divisible_by_3_and_4(n):
	for i in range(n + 1):
		if i % 3 == 0 and i % 4 == 0:
			 yield i

n = int(input("Enter a number: "))
print("Numbers divisible by 3 and 4:", ", ".join(map(str, divisible_by_3_and_4(n))))

#4
def squares(a, b):
	for num in range(a, b + 1):
		yield num ** 2

a, b = 1, 10
for square in squares(a, b):
	print(square)

#5
def countdown(n):
	for num in range(n, -1, -1):
		yield num

n = 10
for num in countdown(n):
	print(num)