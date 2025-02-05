#1
class StringProcessor:
	def __init__(self):
		self.text = ""

	def getString(self):
		self.text = input("Enter a string: ")

	def printString(self):
		print(self.text.upper())

if __name__ == "__main__":
	processor = StringProcessor()
	processor.getString()
	processor.printString()

#2
class Shape:
	def area(self):
		print(0)

class Square(Shape):
	def __init__(self):
		self.length = float(input("Enter the length of the square: "))

	def area(self):
		print(self.length * self.length)

if __name__ == "__main__":
	shape = Shape()
	shape.area()
	square = Square()
	square.area()

#3
class Shape:
	def area(self):
		print(0)
class Rectangle(Shape):
	def __init__(self):
		self.length = float(input("Enter the length of the rectangle: "))
		self.width = float(input("Enter the width of the rectangle: "))

	def area(self):
		print(self.length * self.width)

if __name__ == "__main__":
	shape = Shape()
	shape.area()
	rectangle = Rectangle()
	rectangle.area()

#4
import math
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def show(self):
		print(f"Point coordinates: ({self.x}, {self.y})")

	def move(self, new_x, new_y):
		self.x = new_x
		self.y = new_y

	def dist(self, initial):
		return math.sqrt((self.x - initial.x) ** 2 + (self.y - initial.y) ** 2)

if __name__ == "__main__":
	point1 = Point(3, 4)
	point2 = Point(6, 8)
	point1.show()
	point1.move(5, 5)
	point1.show()
	print(f"Distance between points: {point1.dist(point2)}")
    
#5
class Account:
	def __init__(self, owner, balance=0.0):
		self.owner = owner
		self.balance = balance

	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
			print(f"Deposited {amount}. New balance: {self.balance}")
		else:
			print("Deposit amount must be positive.")

	def withdraw(self, amount):
		if amount > self.balance:
			print("Insufficient funds. Withdrawal denied.")
		elif amount > 0:
			self.balance -= amount
			print(f"Withdrew {amount}. New balance: {self.balance}")
		else:
			print("Withdrawal amount must be positive.")

acc = Account("John Doe", 1000)

acc.deposit(500)
acc.deposit(300)

acc.withdraw(200)
acc.withdraw(2000)

print(f"Final balance for {acc.owner}: {acc.balance}")

#6
def is_prime(n):
	if n < 2:
		return False
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True
numbers = [10, 15, 17, 19, 22, 23, 29, 30]
primes = list(filter(lambda x: is_prime(x), numbers))
print(primes)