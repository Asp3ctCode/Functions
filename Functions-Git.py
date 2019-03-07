# 4.13.4: Functions and Variables
# Tyler Goodrich
# 2.11.19
name = input("What is your name:")

def greeting():
    print("Hi there " + name + "!")
    print("Nice to meet you")

greeting()

'''name = input("What is your name: ")

def greeting():
    print("Hi there " + name +"! ")
    print("Nice to meet you")'''

x = 10

def print_something():
    x = 3
    print('\n' , x)

print('\n', x)
print_something()


#4.14.4: Name and Age
# Mr. Lange
# 2.18.19

def name_and_age(name, age):
    print('Hi, my name is', name, 'and I am',str(age), 'years old!')

name_and_age('Mike', 15)
name_and_age('Zane', 18)


# 4.14.5
# Tyler Goodrich
# 2.19.19

def print_two_numbers(x, y = 20):
    print('First number:', x)
    print('Second number: ' + str(y))

print_two_numbers(34, 45)
print_two_numbers(78)
Print('done')
