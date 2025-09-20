#!/usr/bin/env python3
"""
===============================================================================
        = W e l c o m e t o t h e P Y T H O N T U T O R A D V A N C E D =
===============================================================================

    This is a no-bullshit Python tutor ripped off from that VimTutor madness, but
    for Python newbies who think 'print("hello")' is rocket science. Cooked up
    because stock tutorials bore me to tears with their hand-holding crap. Lessons
    1-6: Basics you'll actually use without wanting to kernel-panic. Lesson 7:
    Where we get real—decorators, context managers, and other wizardry that makes
    your code not suck. Edit this file in your editor of choice (vim, duh), fill
    in the blanks as told, save, then run 'python this_file.py' to see if you're
    not a complete idiot. It'll execute everything and spit out results or errors
    (errors mean you fucked up—fix it). Each run starts fresh if you copy from
    original, but experiment or die bored.

    Takes 30-45 mins if you're not spacing out. Make a copy to trash; this one's
    your boot camp. Type the code, run it, feel the burn—or just read like a wimp
    and wonder why your scripts segfault.

    Hit your editor, scroll to Lesson 1.1, edit that shit, save, run from terminal.
    Let's make you not a scripting zombie.

    NOTE: Everything below is commented out. Uncomment sections as you go through
    lessons. Only your uncommented code will run—no spam, just your glorious
    output or spectacular crashes. Uncomment imports, prints, whatever. Start
    with Lesson 1.1: remove the # from the print line and fix it.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    VIM BASIC REVISION: SELECTING TEXT TO WRITE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        ** To save part of the file, type v motion :w FILENAME **

  1. Move the cursor to this line.

  2. Press v and move the cursor to the fifth item below. Notice that the
     text is highlighted.

  3. Press the : character. At the bottom of the screen :'<,'> will appear.

  4. Type w TEST , where TEST is a filename that does not exist yet. Verify
     that you see :'<,'>w TEST before you press <ENTER>.

  5. Vim will write the selected lines to the file TEST. Use :!dir or :!ls
     to see it. Do not remove it yet! We will use it in the next lesson.

    NOTE: Pressing v starts Visual selection. You can move the cursor around
    to make the selection bigger or smaller. Then you can use an operator
    to do something with the text. For example, d deletes the text.

    QUICK TIP FOR THIS TUTOR: After uncommenting and editing a lesson's code,
    select just that uncommented block (v, move to cover it), then :w! run.py
    to dump it to run.py. Then :!python run.py to execute it right in Vim.
    See your output or errors without leaving the editor. Efficient, no? Do this
    per lesson—keeps shit isolated, no global fuckups.

"""
# Uncomment and edit as you go—run the file after each lesson to verify.
# Errors? Good, learn from 'em. No errors? You're lying.

# ================== LESSON 1: TYPES =========================
# Lesson 1.1: PRINTING PYTHON TYPES
# 
# Types: Every single thing in Python is an object, and every object has a
# type—check it with type(some_shit), which spits back the class that owns it.
# And get this: types themselves are objects too, created by the metaclass type
# (yeah, it's turtles all the way down, you recursive nightmare).
# 
# Covering all built-in types: None, bool, int, float, complex, str, list,
# tuple, dict, set, frozenset, range, bytes, bytearray, memoryview, function,
# class
# -------------------------------------------------------------------------------- 
# x = type                                  # Type: type
# nothing = None                            # Type: NoneType
# is_sane = False                           # Type: bool
# age = 55                                  # Type: int
# pi = 3.14159                              # Type: float
# z = 3 + 4j                                # Type: complex
# name = "Linus"                            # Type: str
# bugs = [42, "panic", 0.1]                 # Type: list
# coords = (10,20)                          # Type: tuple
# prefs = {"os":"Linux"}                    # Type: dict
# idiots = {"user1","user2"}                # Type: set
# hell = frozenset(["debug", "monday"])     # Type: frozenset
# r = range(5)                              # Type: range
# b = b'hello'                              # Type: bytes
# ba = bytearray(b'hello')                  # Type: bytearray
# mv = memoryview(ba)                       # Type: memoryview
# 
# def foo(): pass                           
# func = foo                                # Type: Function 
#
# class Dog:                                # Type: type (yes, this is a type)
#     def __init__(self, name): self.name = name
#     def bark(self): print(f"{self.name} woofs!")
# 
# dog = Dog("Fido")                         # Type: Dog
# 
# # Print individually like this
# print(f"x\t:\t{x}\t{type(x).__name__}")
#
# # Or, loop over locals like this
# for variable_name, value in list(locals().items()):
#     if not variable_name.startswith('__'):
#         print(f"{variable_name}\t:\t{value}\t{type(value).__name__}")







# Lesson 1.2: Types versus Syntax
# 
# Python's got two big buckets: objects (which all have types, as we've beaten
# into your skull in the last lesson), and syntax (the control flow crap like
# keywords, operators, and punctuation that glues it all together without
# turning your code into a syntax-error shitstorm). 
# 
# - Objects/Types: The meat—ints, strings, classes, your barking dog instances,
# enums, functions, everything you can assign to a variable, pass around, or
# type()-check. These are runtime citizens, born from classes (which are types
# themselves, remember?).
#
# - Pure Syntactical Control Flow Voodoo: The skeleton—keywords ("for", "if",
# "def", "class"), operators ("+", "+=", "and", "in"), delimiters (colons,
# parens, commas), and indentation (yeah, that whitespace heresy). This shit
# doesn't exist at runtime; it's compile-time fairy dust that tells Python how
# to interpret and execute your objects. Try type(if) or type(+)—SyntaxError
# city, because they're not objects, they're grammar rules etched in stone by
# Guido's unholy hand.
# -------------------------------------------------------------------------------- 
# import math as m                 # import, as
# import asyncio
# from sys import version          # from ... import
# 
# async def demo(x: int = 5):      # async, def, :, =, pass
#     pass
# 
# class Dummy:                     # class
#     def method(self): return 42  # return
# 
# try: 4 + 5                       # try
# except Exception as e: print(e)  # except, as
# finally: print(7)                # finally
# 
# i, x = 5, 10                     # , and =
# for i in range(x):               # for, in
#     if x > 0 and x != 0: 
#         continue                 # continue
#     elif x <= 0: 
#         raise ValueError("Oops") # raise
#     else: break                  # break
# 
# while i < 3 or i == 2: i += 1    # while, <, or, ==
# 
# with open('temp.txt','w') as f:  # with, as
#     f.write(str(i))
# 
# assert x is not None             # assert, is not
# f = lambda y: y+1                # lambda
# print(f"X: {x}")                 # f-string, {}
# 
# del x                            # del
# 
# g_var = 10
# def outer():
#     global g_var; g_var += 1     # global
#     nl = 5
#     def inner():
#         nonlocal nl; nl += 1     # nonlocal
#         yield g_var              # yield
#     return inner
# print(next(outer()()))
# 
# def decorator(fn): 
#     return lambda *a,**k: fn(*a,**k)    # lambda
# @decorator                              # @ before the decorator
# def some_coroutine(): return "done"
# 
# async def runner(): 
#     await demo()                # await 
#     await asyncio.sleep(0)
#     print("await")
# asyncio.run(runner())            







# Lesson 1.3: Dunder Methods in Native Python Data Types
#
# Python's built-ins use dunders to integrate with syntax. Study them to avoid
# shitty implementations. Except for in this lesson, call syntax, not dunders
# directly.
# -------------------------------------------------------------------------------- 
# Sequences (list, tuple, str, bytes, range)
# l = [1, 2, 3]
# l.__getitem__(1)      # l[1]
# l.__setitem__(1, 99)  # l[1] = 99
# l.__delitem__(1)      # del l[1]
# l.__contains__(2)     # 2 in l
# l.__len__()           # len(l)
# it = l.__iter__()     # iter(l)
# it.__next__()         # next(it)
# l.__reversed__()      # reversed(l)
# s = "abc"
# s.__add__("def")      # s + "def"
# s.__mul__(3)          # s * 3
# s.__getitem__(slice(1, None))  # s[1:]
# 
# # Mappings (dict)
# d = {'a': 1}
# d.__getitem__('a')    # d['a']
# d.__setitem__('b', 2) # d['b'] = 2
# d.__delitem__('a')    # del d['a']
# d.__contains__('a')   # 'a' in d
# d.__len__()           # len(d)
# it = d.__iter__()     # iter(d) (keys)








# Lesson 1.4: Python Dunders
# Emulate built-ins; see docs.python.org/3/reference/datamodel.html.
# --------------------------------------------------------------------------------
# class MyClass:
#     def __init__(self):
#         self.d = [1, 2, 3]  # Demo container
# 
#     # Str: print(obj) or str(obj)
#     def __str__(self):
#         return "Nice"
# 
#     # Len: len(obj)
#     def __len__(self):
#         return len(self.d)
# 
#     # Getitem: obj[key]
#     def __getitem__(self, k):
#         return self.d[k]
# 
#     # Setitem: obj[key] = v
#     def __setitem__(self, k, v):
#         self.d[k] = v
# 
#     # Contains: item in obj
#     def __contains__(self, i):
#         return i in self.d
# 
#     # Iter: for x in obj
#     def __iter__(self):
#         return iter(self.d)
# 
#     # Enter: with obj (setup)
#     def __enter__(self):
#         self.backup = self.d.copy()  # Backup state
#         return self
# 
#     # Exit: with obj (teardown, handles exc)
#     def __exit__(self, *exc):
#         self.d = self.backup  # Restore
#         del self.backup
#         return False  # Propagate exc
# 
#     # Call: obj(...)
#     def __call__(self, *a):
#         pass
# 
# # Usage: Temp mods auto-revert, no manual cleanup needed.
# obj = MyClass()
# with obj as mc:
#     mc[0] = 99  # Temp change
# print(obj.d)  # Back to [1, 2, 3] after with







# Lesson 1.6: CRUD on Lists and Strings 
# --------------------------------------------------------------------------------
# # LISTS
# l = ['a', 'b', 'c']
# # READ
# l[0]  # 'a'
# l[1:3] # ['b', 'c']
# 'b' in l # True
# # CREATE
# new = l + ['g']
# l += ['h']
# # UPDATE
# l[0] = 'A'
# # DELETE
# del l[3]
# del l[1:3]
# 
# # STRINGS (immutable, new on ops)
# s = "abc"
# # READ
# s[0]  # 'a'
# # CREATE
# new = s + "e"
# s += "d" # new
# # UPDATE (new)
# s[:1] + 'y' + s[1:]
# # DELETE (new)
# s[:1] + s[2:]







# Lesson 1.7: LOOPS 
# -------------------------------------------------------------------------------- 
# # Basic while: Double 1-5 
# num = 1
# while num <= 5:  # Loops as long as truthy.
#     print(num * 2)
#     num += 1  # Update or die trying.
# 
# # Basic String Iteration: Char-by-Char Grind
# for char in "12345":
#     print(char)
#
# # Generators: Low-Mem Yields for the Memory-Stingy
# def doubled(n):
#     num = 1
#     while num <= n:
#         yield num * 2
#         num +=1
#
# for i in doubled(5):
#     print(i)
#
# # Sum volumes for a 2x2x2 cube of units.
# total_volume = 0
# print("  +---+---+")
# print("  | L | W | H | Vol |")
# print("  +---+---+---+-----+")
# for length in range(1, 3):
#     for width in range(1, 3):
#         for height in range(1, 3):
#             vol = length * width * height
#             print(f"  | {length:1} | {width:1} | {height:1} | {vol:3} |")
#             total_volume += vol
# print("  +---+---+---+-----+")
# print(f"Total volume of all boxes: {total_volume} cubic units")







# Lesson 1.8: DECORATORS - WRAP YOUR FUNCTIONS LIKE A PRO
# Look, in the real world, your functions aren't living in isolation—they're part 
# of an ecosystem. Sometimes you need to add behavior around them without hacking 
# up the original code like some amateur surgeon. 
# 
# That's where decorators come in: they're syntactic sugar on top of higher-order 
# functions, letting you inject logging, timing, authentication, or whatever crap 
# you need without turning your function into a bloated monster. Why bother? 
#
# Because rewriting every function to include the same boilerplate is for idiots 
# who like copy-paste errors and maintenance hell. Decorators keep things DRY 
# (Don't Repeat Yourself, you slacker), modular, and readable. Imagine debugging 
# a kernel module without this— you'd be chasing ghosts for weeks. This timer's a 
# simple example: it wraps your func to measure execution time, so you can spot the 
# slow-ass bottlenecks before they tank your app. 
# 
# Without it, you're flying blind, wondering why your program's "just slow." Use it, 
# or suffer.
#
# What the hell does this decorator actually do in the example? Simple: 
# - @timer takes your slow() function and replaces it with a wrapper that sneaks in 
#   a timer. 
# - When you call slow(), you're not really calling slow() anymore—you're calling the 
#   wrapper. That bastard starts the clock with time.time(), runs your original slow() 
#   function (which sleeps for a second and prints "Done"), then stops the clock and 
#   prints the elapsed time. 
# - Magic? Nah, just clean code that doesn't pollute your function with timing crap. 
#   If slow() took 1 second, you'll see something like 1.00012345678 printed after "Done". 
#   Boom—instant profiling without rewriting a damn thing.
# -------------------------------------------------------------------------------- 
# import time
# 
# def timer(func):
#     def wrapper():
#         start = time.time()
#         func()
#         print(time.time() - start)
#     return wrapper
# 
# @timer
# def slow():
#     time.sleep(1)
#     print("Done")
# 
# slow()







# Lesson 1.9: CONTEXT MANAGERS - WITH BLOCKS, CLEANUP AUTOMAGIC 
# Finally, a way to force your code to clean up after itself without you
# forgetting like a braindead intern. Automagic cleanup—because who has time
# for try-finally bullshit?
# -------------------------------------------------------------------------------- 
# import time
# 
# class Timer:
#     def __enter__(self):
#         self.start = time.time()
#         return self
# 
#     def __exit__(self, *args):
#         print(time.time() - self.start)
# 
# with Timer():
#     time.sleep(1)
#     print("Slept")
# 







"""

# Lesson 3: Common Programming Snippets

# 3.1: Multidimensional Arrays and Their Traversal

Brush up on your knowledge of multidimensional arrays and their traversal techniques. This course will equip you with the skills to manipulate multidimensional arrays, transposing rows and columns, and iterating over nested elements.

Course details

Unit 1
5 practices
57 min
Exploring the Dimensions: A Beginner's Guide to Multidimensional Arrays in Python
Preview
Update Apartment Name in Building Directory
Unoccupied Apartment Identifier
Print Apartment Codes on the First Floor
Expand the Digital Apartment Building
Apartment Building Management in Python

Unit 2
5 practices
57 min
Columnar ZigZag and Reverse Traversal of Matrices
Preview
Reverse the Bookshelf Traversal Pattern in Python
Repairing the Library Bookshelf Traversal
Add Direction Switch Logic to Bookshelf Traversal
Vertical Library Traverse Challenge
Zigzag Bookshelf Traversal Challenge

Unit 3
5 practices
57 min
Transposing Matrices in Python
Preview
Restaurant Seating Arrangement Transposition
Transpose the Seating Chart in Reverse Order
Transpose the Restaurant Seating Arrangement in One Line
Reflecting a Square Matrix Over Secondary Diagonal
Transpose the Restaurant Seating Arrangement

Unit 4
5 practices
57 min
Checking Adjacent Cells in 2D Arrays in Python
Preview
Horizontal Move Identification in a Game Board
Spotting the Landing Area
Assessing Strategic Placement on a Game Board
Magical Chessboard: Discovering the Next Move
Counting Corner 'E's in Submatrices

Unit 5
5 practices
57 min
Navigating Adjacent Cells in a Grid: An Exercise in 2D Traversal
Preview
Enhance Hiking Trail Path Finder with Diagonal Movements
Mountain Peak Exploration Code Correction
Add a Function to Navigate to the Next Higher Peak
Add Selection Logic for the Next Hiking Position Based on Elevation
Ascending the Mountain - Grid Traversal Challenge




# 3.2: HashMaps and Their Use for Efficient Data Access

Enhance your comprehension and use of hashmap data structures while focusing on its application in counting and aggregation tasks. This exploration will deepen your understanding of their efficient data access and manipulation capabilities.

Course details

Unit 1
5 practices
57 min
Essentials of HashMaps in Python
Preview
Update the Library Catalog Entry
Library Catalog Error Correction
Check Book Availability in Library Catalog
Update and Access Elements in a Library Catalog Dictionary
Updating a Library Catalog Using HashMaps in Python

Unit 2
5 practices
57 min
Mastering Element Counting with Python HashMaps
Preview
Explore Dictionary Methods for Efficient Counting
Correct the Book Counter Code
Update Book Counts in Library Tracker
Counting Letter Frequency in a Library Sentence
Counting Book Copies in a Collection Using HashMaps

Unit 3
5 practices
57 min
Aggregating Essentials: Mastering HashMaps in Python
Preview
Calculate the Average Quantity in Inventory
Inventory Maximum Quantity Calculation Correction
Add Inventory Statistics Calculation to Grocery Shop System
Inventory Stock Level Comparison to Average
Grocery Shop Inventory Maximum Count Finder

Unit 4
5 practices
57 min
HashMaps in Action: Solving Real-World Problems in Python
Preview
Update Library System to Handle Borrowing Logic
Spot the Bug in Library Catalog Management
Update Library Inventory and Check Stock Status
Add Word Count Functionality to the HashMap
Check Book Availability in Library Catalog











# 3.3: Splitting Advanced Tasks into Smaller Pieces

Learn how to break down complex tasks into manageable sub-tasks. This course will help you master the skills necessary to effectively structure, divide, and implement each part of advanced coding problems. You'll also focus on merging sub-task solutions into a cohesive whole.

Course details

Unit 1
3 practices
39 min
Efficient Data Processing in Social Networking Logs Analysis
Preview
Email Organizer
Online Programming Competition Analysis
Book Borrowing Duration Analysis In Library Logs

Unit 2
3 practices
39 min
Exploring Diagonal Matrix Traversal Techniques
Preview
Zigzag Matrix Traversal and Negative Number Indices
Spiral Traversal and Vowel Positions in a Grid
Prime Number Identification in Matrix Zigzag Traversal

Unit 3
3 practices
39 min
Combining Submatrices for Unified Solutions
Preview
Interleaving Columns from Submatrices
Boundary Layer Extraction and Concatenation from Two Matrices
Swapping Submatrices Within a 2D Matrix

Unit 4
3 practices
39 min
Parsing Complex Strings into Nested Dictionaries and Updating Values
Preview
Parsing and Updating a Nested JSON Object in Python
User Data Processing and Updating via Nested String Conversion
Parsing and Updating Nested User Data












# 3.4: Writing Optimal Algos Using HashMaps, HashSets, and TwoPointer
# techniques

Delve into the essentials of optimal programming algorithms involving HashMaps, HashSets, and two-pointer techniques. Enhance your skills in data structure optimization and streamline problem-solving methods.

Course details

Unit 1
3 practices
39 min
Complexity Analysis: A Quick Reminder
Preview
Summing Integers Between Two Numbers
Finding Minimum Absolute Difference in an Array
Closest Pair Mapping in Arrays

Unit 2
3 practices
39 min
Optimizing Performance with HashSets in Python
Preview
Finding Common Characters with Sets
Efficient Presence Checking in Celestial Body Lists
Movie Recommendation Algorithm with Sets

Unit 3
3 practices
39 min
Optimizing Array Analysis with HashMaps
Preview
String Partitioning by Unique Characters
Character Removal for Minimal Word Count
Finding the Minimum Distance Between Word Occurrences in a List

Unit 4
3 practices
39 min
Efficient Pair Sum Identification with the Two-Pointer Technique
Preview
Identifying Pairs with Zero Sum Using Two-Pointer Technique
Finding Maximum Sum Subarray Using Two-pointer Technique
Finding the Longest Subarray with a Specified Sum Using Two-Pointer Technique

Unit 5
3 practices
39 min
Manipulating Arrays with Hashing and Two Pointers Technique
Preview
Array Transformation Based on Closest Half-value Criterion
Finding the Most Influential Person in a Network
Longest Substring with At Most K Distinct Characters








# 3.5: Maximizing Efficiency in Problem Solving Techniques


This comprehensive course incorporates unique problem-solving approaches and analyzing techniques that extend beyond core programming. Topics include optimizing brute force methods, dealing with combinatorial problems, and utilizing heaps and sorted lists effectively.

Course details

Unit 1
3 practices
39 min
Estimating Algorithm Processing Time and Optimizing Brute-Force Solutions by Picking Optimal Variable for Brute Force
Preview
Finding a Pair with Target Sum Using Hashmap Optimization
Player Score Lookup Through ID Queries
Finding Pair Sums in Two Arrays

Unit 2
3 practices
39 min
Optimizing Range Query Solutions with Precalculation Techniques
Preview
Maximal Cumulative Sum in Array for Given Queries
Finding the Length of a Substring After Removing Certain Characters
Finding Divisors of the Closest Perfect Square

Unit 3
3 practices
39 min
Combinatorial Pair Analysis in Large Datasets
Preview
Counting Distinct Pairs with Absolute Difference More Than 10
Counting Pairs with Equal Values in an Array
Three-Letter Combination Count from String

Unit 4
3 practices
39 min
Efficient Median Calculation for Array Prefixes Using Heaps
Preview
Implementing Heap Operations on a Set of Numbers
Heap Manipulation for Data Querying
Finding the floor(k/3)-th Smallest Number in Each Prefix

Unit 5
3 practices
39 min
Efficient Set Operations with Sorted Data Structures
Preview
Finding Smallest Absolute Distance Between Added Numbers
Managing Operations on A Sorted List
Interval Management with SortedLists in Python

"""
