#!/usr/bin/env python
# coding: utf-8

# # Python basics
# 
# ## Conditional statements
# 
# Python has only one built-in conditional statement and it is the `if` -` elif` - `else` statement. We will not find here the `case` -` switch` construct known from other programming languages. Here is the simplest form of this instruction:
# 
# ```python
# number_1 = 5
# number_2 = 2
# if number_1 > number_2:
#     print('First number is bigger than the 2nd.')
# ```
# 
# Let's see how its more extensive version looks like, with support for data entered from the keyboard.
# 
# ```python
# number = input('Give me a number: ')
# number = int(number)
# 
# if number < 10:
#     print('This is a rather small number')
# elif 9 < number < 100:  # shorthand for ranges
#     print('Quite a large number')
# else:
#     print('This has to be a really big number')
# ```
# 
# To build more complex conditions we use Boolean operators.
# 
# 
# ```python
# if number < 10 or number > 15:
#     print('The number is in the wrong range.')
#     
# # We can also check if a value is in a list
# my_list = [1, 3, 5, 7,9]
# if number not in my_list:
#     print('The number is not in the list.')
# ```
# 
# As mentioned before, Python has the type `None`, which corresponds to Null known from other languages and databases.
# 
# ```python
# nothing = None
# empty_string = ''
# 
# if not nothing:
#     print('None is False')
#     
# if not empty_string:
#     print('Empty string is False')
#     
# if nothing == empty_string:
#     print('Not equal!')
#     
# # If we want to check if a string is empty
# if empty_string == '':
#     print('This is an empty string')
# ```

# In[ ]:


# Here you can test out conditional statements


# ## Loops
# 
# In Python, we have two loops: `for` and` while`, while the former is definitely more "popular" among Python programmers. An example of using the `for` loop has already been found before where the` range` function was described. As a reminder, the following examples will also show its use.
# 
# ```python
# # for with range function
# for i in range(3):
#     print(i)
# 
# # for with a list
# my_list = [4, 5, 6]
# for i in my_list:
#     print(i)
# 
# # if we want to get index values as well
# for index, value in enumerate(my_list):
#     print(str(index) + ' -> ' + str(value))
#     
# # Or we can do it without unpacking
# # so basically we get a tuple
# 
# for tpl in enumerate(my_list):
#     print(str(tpl[0]) + ' -> '+ str(tpl[1]))
#     print(type(tpl[0]))
#     print(type(tpl[1]))
#     print(type(tpl))
#     
# # For with dictionaries
# # If we don't specify how we want to enumerate
# # keys are picked as default
# dictionary = {
#     'name': 'Marek',
#     'surname': 'Kowalski',
#     'gender': 'male'
# }
# 
# for key in dictionary:
#     print(key)
#     
# for val in dictionary.values():
#     print(val)
#     
# for key, value in dictionary.items():
#     print(key + ' -> ' + value)
#     
# for key in dictionary:
#     print(key + ' -> ' + dictionary[key])
# ```
# 
# The form of a Python while loop does not differ from its way of working in other languages.
# 
# ```python
# # While loop
# counter = 0
# while True:
#     counter += 1
#     if counter > 10:
#         break
# 
# counter = 0
# while counter < 5:
#     print(str(counter) + ' lower than 5')
#     counter += 1
#     
# # While loop is good when we don't know when it ends
# # (we don't know the number of iterations), eg. when fetching input
# # data until the user decides he gave all the data
# 
# my_list = []
# print('Give the numbers you want to put in the list.')
# print('Print "stop" to end.')
# while True:
#     input = input()
#     if input == 'stop':
#         break
#     my_list.append(int(input))
#     
# print('Your list -> ' + repr(my_list))
# ```
# 
# At this point, mention should be made of the instructions `break` and` continue`, which can be placed inside the loop. `break` terminates the loop (only the block in which the instruction was included) while` continue` finishes the course of the current iteration of the loop (i.e. what is after `continue` will not be executed) and starts the next iteration.

# In[ ]:


# Here you can test out loops


# ## Python Comprehensions
# 
# This mechanism consists in generating a collection (list, dictionary, set) based on a single-line record specifying the conditions for variables that will be placed in a given collection. This is best represented by the relevant examples.
# 
# ```python
# # comprehensions for lists
# x = [i for i in range(5)]
# print(x)
# 
# y = [i for i in range(10) if i % 2 == 0]
# print(y)
# 
# # We can do something for each of the values
# # For example cast the values
# my_list = ['1', '2', '3', '4', '5']
# numbers = [int(i) for i in my_list]
# print(numbers)
# 
# # Instructions can be in the form of a graph
# # Python documentation example:
# vec_of_vec = [[1,2, 3], [4, 5, 6], [7, 8, 9]]
# single = [num for elem in vec_of_vec for num in elem]
# print(single)
# 
# # Comprehensions and dictionaries
# # Switching keys and values
# dictionary = {1: 'Burek', 2: 'Azor', 3: 'Fafik'}
# print({value: key for key, value in dictionary.items()})
# 
# # Coprehensions and sets
# # Create set from list
# my_list = [1, 2, 2, 3, 4, 4, 4, 5]
# my_set = {i for i in lista}
# print(my_set)
# ```
# 
# The mechanism presented in this section is very useful, although complex commands can be a challenge to interpret in relation to the "traditional" approach. More examples can be found in the Python documentation at https://docs.python.org/3/tutorial/datastructures.html.

# In[ ]:


# Here you can play with python comprehensions


# ## Functions
# 
# The general definition of the function is that it is a separate block of code that has to do as little as possible at once, but it does it well. It is also an indispensable element of the DRY (Don’t Repeat Yourself) methodology, i.e. where a function will be used repeatedly, we can use the function. Sample Python function declaration below.
# 
# ```python
# def start():
#     print('Starting...')
# ```
# 
# The `def` keyword informs the interpreter that it is a function declaration. The function has its name and zero or more arguments. The function can perform some operations and change the state of objects without returning anything at the exit (in Java we use void as the return type) or it can return some values. Unlike some programming languages, the function signature does not tell us what value we can expect.
# 
# ```python
# def multiply(text, n):
#     return (text + ' ') * n
#     
# print(multiply('summer', 5)
# ```
# 
# It should also be remembered that if the declaration and function call take place in the same file, the function call must be after its declaration. Similarly to the PHP language, function arguments may have their default values and will be used if the programmer does not pass them.
# 
# ```python
# def multiply(text='Hello ', n=3):
#     return (text + ' ') * n
#     
# print(multiply())
# ```
# 
# In case the function contains optional arguments in order to avoid having to watch the order of passed arguments, we can pass the values of arguments together with their names.
# 
# ```python
# print(multiply(n=5, text='Jingle bells'))
# ```
# 
# Functions in Python can take virtually an unlimited number of arguments or key arguments (those whose name we specify). By convention, the variable that stores the former is `*args`, and the variable for arguments with the key is` **kwargs`, but their names in our functions can be arbitrary.
# 
# ```python
# def doing_cool_things(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     
# doing_cool_things(
#     3, 4, 5.6,
#     name='Lukasz',
#     hobby=['sport', 'fantasy']
# )
# ```
# 
# Variable range and global variables. Variables declared within a function only have scope within that function, which means that any attempt to refer to them outside of the function will fail. However, you can define such a variable as a global variable. Although it is part of the language, using this mechanism is not recommended, and often even stigmatized by other programmers.
# 
# ```python
# def my_global():
#     global a
#     a = 1
#     b = 2
#     return a + b
#     
# def no_global():
#     c = 3
#     return a + c
#     
# print(my_global())
# print(no_global())
# ```

# In[ ]:


# Here you can test out functions


# ## Modules and `virtualenv`
# 
# Virtually every popular programming language has a mechanism that allows you to manage additional libraries or packages. Python also has its own package manager called `pip`. In version 3.x it is not necessary to manually install it because it is already included by default in these distributions.
# 
# ### PIP in windows cmd
# 
# To use the PIP tool on the Windows command line, we must first make sure that the Python interpreter (and the Scripts folder) is in the `PATH` environment variable. We can either display the path variable or simply run the `python –version` command in the terminal, which will return the Python version we are currently using or the command will not be recognized.
# 
# If the above condition is met, we can run the PIP tool and e.g. display a list of packages from the current Python environment:
# 
# ```bash
# python –m pip list
# ```
# 
# A list of commands and modest help will be obtained after the command:
# 
# ```bash
# python –m pip help
# ```
# 
# The index of packages that can be installed from the PyPi index can be found at https://pypi.python.org/pypi, where currently there are over 122,000 packages ...
# 
# As the help shows, the command for installing the package is `install package_name`. Let's install the `requests` package.
# 
# ```bash
# python –m pip install requests
# ```
# 
# It is also possible to choose the specific version of the package that you want to install.
# 
# ```bash
# python –m pip install requests==2.18.0
# ```
# 
# As you can guess, the `uninstall` option is used to uninstall packages.
# 
# The PIP tool also allows you to install packages based on a requirements file, an example of which might look like this:
# 
# ```python
# ####### example-requirements.txt #######
# 
# ###### no version specified ######
# nose
# nose-cov
# beautifulsoup4
# 
# ###### wspecific version ######
# docopt==0.6.1 # exactly 0.6.1
# keyring>=4.1.1 # minimum 4.1.1
# coverage!=3.5 # without version 3.5
# Mopidy-Dirble~=1.1 # compatible to 1.1
# 
# ###### read a different requirements file ######
# -r other-requirements.txt
# 
# ###### install from downloaded file ######
# ./downloads/numpy-1.9.2-cp34-none-win32.whl
# http://wxpython.org/Phoenix/snapshot-builds/wxPython_Phoenix-3.0.3.dev1820+49a8884-cp34-none-win_amd64.whl
# 
# ###### additional packages without version ######
# # To show you that order doesn't matter
# rejected
# green
# ```
# 
# The command that starts the package installation from the requirements.txt file:
# 
# ```bash
# python –m pip install –r requirements.txt
# ```
# 
# These are the basic and most frequently used PIP commands. For more detailed documentation and examples, please refer to: https://pip.pypa.io/en/stable/.
# 
# ### Virtualenv
# 
# Virtualenv is short for **virtual environment**. This tool allows you to create separate environments containing the Python interpreter and a set of packages that you want to use in a specific project or before you want to update packages in a production project we want to check how the application will behave in the new environment.
# 
# Virtualenv is a Python package, so to use it, you need to make sure that the appropriate package is installed and possibly install it.
# 
# To create a new virtual environment, indicate the folder in which you want to create it. Then execute the command:
# 
# ```bash
# virtualenv env_name
# ```
# 
# will create a new folder here and copy the Python interpreter that was currently set in the PATH environment variable and attach several scripts allowing, among others to activate and deactivate the virtual environment.
# The next step that you must take to get started in this environment is to activate it, which consists in running the script from the Scripts \ activate file in the new environment folder. From now on, the active interpreter is the one contained in the new environment. We can now run Python scripts, install packages, and use the Python console for this environment.
# 
# ### Conda environment
# 
# You can do the same things with the Anaconda distribution as follows:
# 
# - Create environment
#    ```
#    conda create -n env_name python=3.7
#    ```
# - Install package
#    ```
#    conda install package_name
#    ```
# - Uninstall package
#    ```
#    conda uninstall package_name
#    ```
# - Remove conda environment
#    ```
#    conda remove --name env_name --all
#    ```
# - Create conda environment from environment file (similar to requirements.txt)
#    ```
#    conda create -f environment.yml
#    ```
# - Create environment file
#    ```
#    conda env export --name env_name > environment.yml
#    ```

# In[ ]:


# Play around with environments and install a couple of packages from conda store


# ## Object-oriented Python
# 
# Object-oriented programming - a programming paradigm in which programs are defined by means of objects - elements connecting state (i.e. data, usually called fields) and behavior (i.e. procedures, here: methods). The object-oriented computer program is expressed as a set of such objects that communicate with each other to perform tasks.
# 
# This approach differs from traditional procedural programming, where data and procedures are not directly related to each other. Object-oriented programming is intended to facilitate writing, maintenance and reuse of programs or their fragments.
# 
# The biggest advantage of programming, design and object-oriented analysis is the compatibility of this approach with reality - _the human brain is naturally best adapted to such an approach when processing information_. (Wikipedia)
# 
# By way of introduction, I cited the definition of object oriented programming quite concisely and specifically. When designing objects, their methods and connections, we try to model the world around us and transfer virtual reality elements known to us to solve a problem or create a tool for work for us or other people. The design principle also says that objects should be as limited as possible in the range of operations we can perform with them. Let them do relatively little but do it well. It also helps to better understand the program and the relationships between objects, reuse them as well as extend its capabilities and maintain code more easily.
# 
# From general assumptions, we move to the sample class declaration in Python.
# 
# ```python
# """docstring for module"""
# 
# class Car:
#     """docstring for class"""
#     def __init__(self):'
#         """constructor"""
#         pass
# ```
# 
# In the example above, only one method has been declared called `__init__` which is a constructor. The definition of the method (because that is what the class functions are called) is not much different from the definition of the functions we have already learned. Each method accepts a special argument called self, which means a reference to the object in which it was defined. It is the equivalent of thishnana from other programming languages.
# 
# Let's expand our class a bit:
# 
# ```python
# """docstring for module"""
# 
# 
# class Car:
#     """docstring for class"""
#     def __init__(self, color, brand):
#         """constructor"""
#         self.color = color
#         self.brand = brand
#         
#     def stop(self):
#         """stop the car"""
#         return 'stopping...'
#         
#     def go(self):
#         """go further"""
#         return f'{self.brand} is going.'
#         
# 
# my_car = Car('blue', 'Ford')
# print(my_car.go())
# print(my_car.stop())
# ```
# 
# The thing that can be noticed here is definitely the lack of access modifiers for both fields and methods of the class because in Python there are no private methods or variables. However, there is a convention that says that prefixing a variable or method with the prefix `_` or `__` means that the variable / method should be treated as private and other developers should not use it, because there is permission to change it without warning. So they are not considered as part of the API. For names from `__`, there is also a mechanism that slightly blurred the visibility of such a variable or method, causing the reference to it to be `_classname_variable`. More information can be found here: https://docs.python.org/3/tutorial/classes.htm.
# 
# Standard class variables are stored for each class instance, but Python also allows you to define variables that can be shared by all instances of a given class. Listing example:
# 
# ```python
# """docstring for module"""
# 
# class Car:
#     """docstring for class"""
#     signal = 'Piiib piiib'
#     
#     def __init__(self, color, brand):
#         """constructor"""
#         self.color = color
#         self.brand = brand
#         
#     def stop(self):
#         """stop the car"""
#         return 'stopping...'
#         
#     def go(self):
#         """go further"""
#         return f'{self.brand} is going.'
#         
#         
# class OpelOmega(Car):
#     def stop(self):
#         return 'stopping quite fast...'
#         
# 
# my_car = Car('blue', 'Ford')
# print(my_car.go())
# print(my_car.stop())
# 
# opel = OpelOmega('green', 'Opel')
# print(opel.stop())
# print(opel.signal)
# ```
# 
# Issues of object-oriented programming are also more complex mechanisms such as abstract classes or polymorphism. It is worth saying here that Python allows multiple inheritance and therefore does not have the ability to define interfaces. These topics, however, are beyond the scope of this subject and will be discussed in advanced Python classes.

# In[ ]:


# Have a go at object oriented programming. Create a Student class with some functions.


# ## Files
# 
# Let's go straight to discussing a few examples.
# 
# ```python
# file = open('plik.txt')
# file = open(r'C:\Users\lukzmu\Projects\python_intro\plik.txt', 'r')
# ```
# 
# The first command opens a file that is in the folder where the file is run. By default, the file is read-only. The second command takes the absolute path and, in addition, the next parameter passes the read mode of the file, which is also read-only here. The letter `r` preceding the path informs Python that it should treat this text string 'literally', i.e. any occurrences of special characters will not be taken into account. which should be preceded by the `\` character.
# 
# Basic reading of data from a file can be done as follows:
# 
# ```python
# file = open('plik.txt')
# file = open(r'C:\Users\kropiak\Projects\python_intro\plik.txt', 'r')
# data = file.read()
# print(data)
# file.close()
# ```
# 
# And here we can notice the first problem if there were Polish letters in the text file. We can overcome this by adding an additional parameter that specifies how the characters to be read should be coded. Remember to close the file handle after reading the data.
# 
# ```python
# file = open(
#     r'C:\Users\lukzmu\Projects\python_intro\plik.txt',
#     'r', encoding='utf-8'
# )
# ```
# 
# We can also read the file line by line with the help of a loop:
# 
# ```python
# file = open('plik.txt', 'r', encoding='utf-8')
# 
# for row in file:
#     print(row)
#     
# file.close()
# ```
# 
# In this case, a situation may arise where a new line will be printed after each output line. This is because the print function adds the character `\ n` to the end, which means a new line, and if such a character was also read from the file, we have the answer why this is happening. To change this, you can set the value of the `end` parameter of the print function to something other than the default value.
# 
# We can also specify the size of the file fragments expressed in bytes. This time with a while loop:
# 
# ```python
# file = open('plik.txt', 'r', encoding='utf-8')
# 
# while True:
#     data = file.read(1024)
#     print(data, end='')
#     if not data:
#         file.close()
#         break
# ```
# 
# Now it's time to save to file.
# 
# ```python
# file = open('plik2.txt', 'w', encoding='utf-8')
# file.write('Writing something to file.')
# file.close()
# ```
# 
# There is a more modern method of accessing files, the use of which frees us from the obligation to remember to close the file handle.
# 
# ```python
# with open('plik.txt', 'r', encoding='utf-8') as file_reader:
#     for row in file_reader:
#         print(row, end='')
# ```
# 
# Finally, an example with exception handling, more on this in the advanced Python section.
# 
# ```python
# try:
#     with open("plik.txt", "r", encoding="utf-8") as file_reader:
#         for row in file_reader:
#             print(row, end="")
# except IOError:
#     print("IOError exception has occured!")
# ```

# In[ ]:


# Play a bit with files. Read a file, change the contents and save. Remember to add the file to the repository.


# # Exercises
# 
# Create a function that takes two lists `a_list` and` b_list` as parameters. Then return a list that will have even indexes from list `a_list` and odd indexes from` b_list`.

# In[1]:


def merge (a_list, b_list):
    c_list=[]
    for i in range(len(a_list)):
        if(i%2==0):
            c_list.append(a_list[i])
        else:
            c_list.append(b_list[i])
    return c_list


a_list = [1, 2, 3, 4, 5, 6, 7, 8]
b_list = [11, 12, 13, 14, 15, 16, 17, 18]

c_list = merge(a_list, b_list)

print(c_list)


# Create a function that accepts the `data_text` parameter and then returns the following parameter information in the form of a dictionary (`dict`):
# 
# - `length`: the length of the given text,
# - `letters`: a list of characters in the word e.g.`['D', 'o', 'g'] `,
# - `big_letters`: parameter converted into small caps, e.g.` DOG`
# - `small_letters`: parameter changed to lowercase e.g.` dog`

# In[2]:


def datadict(data):
    print(dict([("Length: ", len(data)),
                ('letters', list(data)),
                ('big_letters', data.upper()),
                ('small_letters', data.lower())]))
    
    
data_text = "Ala ma kota"
datadict(data_text)


# Create a function that accepts `text` and` letter` as parameters, and then returns the result of removing all instances of the value in `letter` from the text` text`.

# In[3]:


def remove_letter(text, letter):
    for char in letter:
        text = text.replace(char, "")
    print(text)
    
let1 = "tmks"
let2 = " Aa"
let3 = "l m kot"
remove_letter(data_text, let1)
remove_letter(data_text, let2)
remove_letter(data_text, let3)


# Create a function that converts the temperature in degrees Celsius to Fahrenheit, Rankine, Kelvin. The conversion type should be passed in the parameter `temperature_type` and include incorrect values.

# In[5]:


def temperature_converter(temperature_type, temperature1):
    temperature_type = str(temperature_type)
    if temperature_type == "f":
        temperature2 = temperature1 * 1.8 + 32
        return temperature2
    elif temperature_type == "r":
        temperature2 = (temperature1 + 273.15) * 1.8
        return temperature2
    elif temperature_type == "k":
        temperature2 = temperature1 + 273.15
        return temperature2
    else:
        print("Error. Incorrect value.")


c = input("Temperature in Celsius: ")
celsius = float(c)

choose = input("Enter: f for Fahrenheit, r for Rankine or k for Kelvin \n Unit: \n")

print(temperature_converter(choose, celsius))


# Create a class `Calculator` that will have the functions` add`, `difference`,` multiply`, `divide`.

# In[19]:


class Calculator:
    def add(a,b):
        print(a+b)

    def difference(a,b):
        print(a-b)

    def multiply(a,b):
        print(a*b)

    def divide(a,b):
        print(a/b)

        
    a=12
    b=3
    
    add(a,b)
    difference(a,b)
    multiply(a,b)
    divide(a,b)


# Create a `Science Calculator` class that inherits from the` Calculator` class and add additional functions, e.g. exponentiation.

# In[35]:


import math
class ScienceCalculator(Calculator):
    def exponent(a,b):
        print(a**b)
    
    def root(a):
        print(math.sqrt(a))

    a = 3
    b = 5
    
    exponent(a,b)
    root(a)
    root(b)


# Create a function that prints the given text from the back, e.g. `kitty -> yttik`.

# In[38]:


def backwards(text):
    print(text[::-1])

text = "doge"
backwards(text)


# Create a class `FileManager` with a parameter in the constructor` file_name`. The class will contain two methods: `read_file` and` update_file`. The `update_file` function should contain the` text_data` parameter, which in effect should be appended at the end of the file. The `read_file` function should return the contents of the file.

# In[6]:


class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        with open(r"D:\Pobrane\Python\introduction-to-python-master\02 Python basics" + "\\" + self.file_name, "r", encoding = "utf-8", ) as file_reader:
            for row in file_reader:
                print(row, end = "")
        return

    def update_file(self, text_data):
        with open(r"D:\Pobrane\Python\introduction-to-python-master\02 Python basics" + "\\" + self.file_name, "a", encoding = "utf-8", ) as file_writer:
            file_writer.write(text_data)
        return


fil_man = FileManager("file.txt")
fil_man.update_file("Aaaaaaaaaaaaaaaaaaa\n")
fil_man.read_file()


# Create a new `virtualenv` (or conda environment) in the project folder and then install the module: https://github.com/yougov/chucknorris. Create a function that will connect to the downloaded module.

# In[9]:


###


# In[ ]:




