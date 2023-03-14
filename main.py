"""Excercise 1"""
"""Task Nr.1: Fix these coding examples according to the standards we learnt during this lecture:"""

class Person():
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def say_hello(self) -> str:
        return f"hello, {self.name}"
    

person = Person("first", "person")
print(person.say_hello())

"""Excercise 1.2"""

def get_greeting(fullname: str) -> str:
    return(f"Hello {fullname.split()[0]} {fullname.split()[1]}, how are you today?")

print(get_greeting("John Kebabas"))


"""Excercise 1.3"""

def greet_user(age: int) -> str:
    eligible_to_enter = age >= 21
    if eligible_to_enter:
        return("Welcome")
    return("Access denied")

print(greet_user(22))

"""Excercise 2"""
"""Task Nr.2: Magic Number problem. A number is said to be a magic number, if the sum of its digits are calculated till a single digit recursively by adding the sum of the digits after every addition. If the single digit comes out to be 1,then the number is a magic number.
For example Number = 50113 => 5+0+1+1+3=10 => 1+0=1 This is a Magic Number

For example Number = 1234 => 1+2+3+4=10 => 1+0=1 This is a Magic Number

Write a python function that takes in one parameter - integer and then returns True if number is magic number or False if it is not a magic number"""

def get_magic_number(number: int) -> int:
    while number > 9:
        number_sum = sum(int(digit) for digit in str(number))
        number = number_sum
    return number == 1

print(get_magic_number(198989))

"""Excercise 2.1 [dėstytojo kodas]"""

def is_magic_number(number: int) -> bool:
    number = str(number)
    if len(number) == 1:
        if number == "1":
            return True
        else:
            return False
    else:
        number = sum([int(n) for n in number])
        return is_magic_number(number)
print(is_magic_number(50113))