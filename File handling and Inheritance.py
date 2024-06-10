#Opening a File: Use the open() function
file = open('example.txt', 'r')  # 'r' for reading, 'w' for writing,content = file.read()  # Read entire content

#Reading from a File: Use methods like read(), readline(), or readlines()
content = file.read()  # Read entire content
line = file.readline()  # Read a single line
lines = file.readlines()  # Read all lines into a list

# Writing to a File: Use methods like write() or writelines()
file = open('example.txt', 'w')
file.write("Hello, World!\n")
file.writelines(["Line 1\n", "Line 2\n"])

# Closing a File: Always close the file to free up resources
file.close()

# Using with Statement: Ensures the file is properly closed after its suite finishes
with open('example.txt', 'r') as file:
    content = file.read()
# No need to explicitly close the file

# Inheritance in Python

# Defining a Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Defining a Child Class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Using the Child Class
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!

# Method Overriding: Child class can override methods of the parent class
class Bird(Animal):
    def speak(self):
        return f"{self.name} says Tweet!"

bird = Bird("Tweety")
print(bird.speak())  # Output: Tweety says Tweet!

# super() Function: Call a method from the parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Initialize parent class
        self.student_id = student_id

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}"

student = Student("Alice", 21, "S12345")
print(student)  # Output: Name: Alice, Age: 21, Student ID: S12345



