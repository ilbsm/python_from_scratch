""" This is the Python crash course by P. Dabrowski-Tumanski for internal use of ILBSM, CENT UW.
The course consist of a few parts, each in different python file. I count on the intelligence of the reader, as this is
mostly a set of examples, which should guide a Python3 adept, how to understand and write Python functions. BTW, this is
a block comment.
"""

# 0. Introduction
""" Python3 is a script language. There is no compilation, you may just write a code and run in through the interpreter.
E.g. you can save the text between the --- lines into a file test.py:
-----------
a=1
b=2
print(a+b)
-----------
and then run python3 test.py in a console, or by clicking "play" button in PyCharm. The result should be obvious.
In Python, you can also of course define functions. We can then define function 'addition' by:

def addition(a,b):
return a + b

If running a file with such content, nothing will happen, as the function addition is not called. In general, one Python
file can be just a set of functions. And if nothing is specified apart from these functions, nothing will happen. These 
functions may be e.g. imported by some other part of your program, but about in in the importing.py file. But you may
specify, that apart from the functions prepared to be imported, there may be some special action of the program, if it 
is invoked directly. E.g. look at the code below:"""


def say_hello():
    print("Hello!")


""" and to the end of this file. The lines above define a simple function. The lines in the end of the file  tell 
Python, that if this file is executed, out of all functions only the 'say_hello()' will be invoked (note the indent!)
Check it, run this file.
And that is the general idea for this tutorial. It is a set of comments and commands. Whenever you want to run specific 
function, just change the 'say_hello()' function into the chosen function.
Have fun!
"""


# 1. Data structures
""" In pure Python the variables do not have declare types. It is enough to write:"""
variable = 1
""" To declare an integer variable. You can also create a float number:"""
float_variable = 1.0
# or
second_float_variable = float(1.0)
""" You can check the type of the variable with function type(), e.g."""


def check_type(var):
    print(type(var))
    return


""" Check it on variables 'variable', or 'float_variable' (i.e. change 'say_hello()' into 'check_type(variable)'. You 
usually do not care for the length of the variable which can be stored. It is rather large number (check how large on 
the internet if interested). Apart from numbers, you can store strings, or bools:"""

string_variable = "This is string"
bool_variable = "True"

"""You can also store arrays of anything, or mixed types. E.g:"""

array_variable = [1, 2, 3, 4, "Friday", 2.44, True, None]

""" is a perfectly fine array. You can access its values in a normal way:"""


def print_array_parts(array):
    print(array[0])
    return

""" You can also have array of arrays: """

second_array = [["first", "second", "third"], [1, 2, 3]]

""" You can also define the dictionaries, e.g. something like arrays, but indexed with nearly anything, e.g. strings:"""
my_week = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}

""" The dictionary has keys ('Monday', 'Tuesday', etc, and corresponding values):"""


def dictionary_info(my_dict):
    print(my_dict.keys())
    print(my_dict.values())
    for key in my_dict.keys():
        print(my_dict[key])
    return


""" Try to run 'dictionary_info(my_week)' and see what happens.
Finally for us, you can also create sets, which store unique elements. They can be very helpful e.g. when you want to remove
    duplicates from the list (but far not only!):"""

set_variable = {1, 2, 3, 4}
duplicated_list = [1, 2, 3, 4, 1, 2, 3, 1, 1, 4, 4]


def remove_duplicates(array):
    print(list(set(array)))
    return


""" As you may see, here we first transform list into a set with a function set(). This results in a set of unique 
elements. Next, we just create a list from it."""

# 2. Loops and if/else
""" You may have noticed the first loop. We have looped over all keys in the dictionary. We can perform loops over any 
iterable structures, e.g. over the lists:"""


def iterate_over(array):
    for element in array:
        print(element)
    return


""" Try this e.g. on the 'duplicated list' array. 
You can also go over the indices of the array:"""


def iterate_over_indices(array):
    for i in range(len(array)):
        print(array[i])
    return


""" This will give exactly the same result, however, is less "Pythonic" than the 'iterate_over' function.
Standard while(condition) loop is also working, as well as the directives 'break', which gets us out of the loop, or 
'continue', which moves to the next iteration. E.g."""


def exemplary_while():
    a = 0
    while a > -1:
        if a == 2:
            print(a)
        elif a == 3:
            print("I got 3!")
        else:
            continue
        # the condition in while will be always fulfilled, therefore we add break:
        if a == 7:
            break
    return


"""Note, that in Python we do not have the brackets like '{', to denote where the loop starts, and where it finishes.
The role of the brackets is fulfilled by appropriate indentation (usually four spaces).
With the last example, you also saw the structure for if/else/elif (which in other languages is written 'else if').
This should be understandable.
Standard operators for if/else hold, like <, >, ==, != etc."""

# 3. More on defining functions
""" As you have already seen, functions are declared by the construction 'def function_name(args): ... return
The function may return anything, and any number of these anything. For example:"""


def results(a, b):
    sum = a + b
    difference = a - b
    product = a*b
    power = a**b
    quotient = a/b
    return sum, difference, product, power, quotient


""" When invoking such function, you may specify, what argument you are using:"""


def run_results():
    val1 = 10
    val2 = 3
    print(results(val1, val2))
    print(results(a=val2, b=val1))
    return


""" When defining functions, you may specify some default parameters:"""


def division_modulo(a, b=2):
    return a % b


def run_division_modulo():
    print(division_modulo(7))           # b will be equal default (2)
    print(division_modulo(7, 3))        # b will be equal 3
    print(division_modulo(b=7, a=3))    # b will be equal 7
    return

# 4. Useful built-in functions

""" There are a lot of useful built-in functions:"""


def try_functions():
    # numbers
    a = -7.33333
    print(abs(a))
    print(round(a))

    # arrays
    array = [1, 12, 1, -2.24, 0, 22]
    print(min(array), sum(array), max(array))
    print(sorted(array))
    array.append(12)
    print(array)
    print(array.count(12))
    print(array.remove(1))
    print(list(reversed(array)))    # reversing the list

    # strings
    string = "  ThiS iS my UGLY stRiNG...."
    print(string.lower())
    print(string.upper())
    print(string.strip())
    print(string.strip('.'))
    print(string.split())
    print(string.replace('S', 's'))
    return

# 5. Oneliners
""" Python is a language where everything should be simple, but also compact. So many things can be shortened, even
into one-liner. For example, to flatten a list, usually we should do two loops:"""

initial_list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

def flatten_list_long(array):
    result = []
    for sublist in array:
        for element in sublist:
            result.append(element)
    return result

def flatten_list_pythonic(array):
    return [element for sublist in array for element in sublist]


""" swapping variables """


def swap():
    a = 2
    b = 3
    print(a, b)
    a, b = b, a
    print(a, b)


""" Select only positive values """

def selection():
    array = list(range(-6, 10))
    print([a for a in array if a > 0])
    return

def select_range():
    array = [i for i in range(100)]
    print([i for i in array if 50 < i < 75])



# 6. Excersises
""" TBD """




if __name__ == '__main__':
    say_hello()

