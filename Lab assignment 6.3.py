#Generate a Python Student class with name, roll_number, branch attributes, a constructor, display_details() method, and sample object creation with output.
class Student:
    def __init__(self, name, roll_number, branch):
        self.name = name
        self.roll_number = roll_number
        self.branch = branch
    def display_details(self):
        print(f"Name: {self.name}, Roll Number: {self.roll_number}, Branch: {self.branch}")
student1 = Student("John", 123456, "Computer Science")
student1.display_details()

#Write a Python function to print the first 10 multiples of a given number using both for and while loops and explain the loop logic.
def print_multiples(n):
    for i in range(1, 11):
        print(n * i)
    i = 1
    while i <= 10:
        print(n * i)
        i += 1
print_multiples(5)

#Create a Python function that classifies age into child, teenager, adult, and senior using if-elif-else and an alternative simplified approach.
def classify_age(age):
    if age < 13:
        return "Child"
    elif age < 18:
        return "Teenager"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"
print(classify_age(10))
print(classify_age(15))
print(classify_age(20))
print(classify_age(65))

#Generate a Python function to calculate the sum of the first n natural numbers using for loop, while loop, and mathematical formula with comparison.
def sum_of_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
print(sum_of_numbers(10))
print(sum_of_numbers(100))
print(sum_of_numbers(1000))
print(sum_of_numbers(10000))
print(sum_of_numbers(100000))

#Develop a Python BankAccount class with deposit(), withdraw(), check_balance() methods, demonstrate transactions, and explain the code.
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def check_balance(self):
        return self.balance
bank_account = BankAccount(1000)
bank_account.deposit(500)
bank_account.withdraw(200)
print(bank_account.check_balance())

