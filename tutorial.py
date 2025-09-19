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

# ===== LESSON 1: THE BASICS - SAY HELLO OR GTFO =====
# Lesson 1.1: PRINTING VARIABLES AND PYTHON DATA TYPES
# Variables: snake_case, no keywords. Dynamic typing—Python guesses, you verify
# with type(). Covering all built-ins: None, bool, int, float, complex, str, list,
# tuple, dict, set, frozenset, range, bytes, bytearray, memoryview, function,
# class
#
# Types: Every single thing in Python is an object, and every object has a
# type—check it with type(some_shit), which spits back the class that owns it.
# And get this: types themselves are objects too, created by the metaclass type
# (yeah, it's turtles all the way down, you recursive nightmare).
# 
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
# print(f"Nothing\t:\t{nothing}\t{type(nothing).__name__}")
#
# # Or, loop over locals like this
# for variable_name, value in list(locals().items()):
#     if not variable_name.startswith('__'):
#         print(f"{variable_name}\t:\t{value}\t{type(value).__name__}")
#
# mls1 = """This is a
# multiline 
# string"""
# print(mls1)
# 
# mls2 = ("And "
#         "this is a "
#         "single line string ")
# print(mls2)







# Lesson 1.2: BASIC MATH
# Compute 2 * (2 + 3) / 4 - 1 and print the result (should be 1.5)
# -------------------------------------------------------------------------------- 
# result = 2 * (2 + 3) / 4 - 1
# print(result)







# Lesson 1.3: STRINGS AND LISTS
# Make a list ['apple', 'banana', 'cherry'], add 'date' to end, print the list
# -------------------------------------------------------------------------------- 
# fruits = ['apple', 'banana', 'cherry']
# fruits.append('date')
# print(fruits)







# Lesson 1.4: IF STATEMENTS
# Set age = 25, if age >= 18 print "Adult", else "Kid"
# -------------------------------------------------------------------------------- 
# age = 25
# if age>=18:
#     print("Adult")
# else:
#     print("Kid")






# Lesson 1.5: WHILE LOOPS - BECAUSE SOMETIMES YOU DON'T KNOW WHEN TO QUIT, YOU
# GLUTTON FOR PUNISHMENT While: Loops till a condition's false. Init var,
# check, do stuff, update—or infinite loop and watch your machine melt.
# Example: Double 1-5, but with a twist: count down from 10, break early if
# even. Covers basics, break/continue too.  Pro tip: Always update inside, or
# you're debugging a toaster.
# 
# print("=== Basic while: Double 1-5 ===")
# num = 1
# while num <= 5:  # Loops as long as truthy.
#     print(num * 2)
#     num += 1  # Update or die trying.
# 
# print("\n=== While with break/continue: Countdown from 10, skip evens, stop at 5 ===")
# count = 10
# while count > 0:
#     if count % 2 == 0:  # Even? Skip.
#         count -= 1
#         continue
#     if count == 5:  # Hit 5? Bail.
#         break
#     print(f"Count: {count} (doubled: {count * 2})")
#     count -= 1
# print("Bailed at 5, you quitter.")
# 
# print("\n=== Infinite while? Don't. But here's a safe one with sentinel ===")
# # Read inputs till 'quit', echo doubled. (Simulated; real input() for you.)
# inputs = ['3', '7', 'quit']  # Pretend user crap.
# i = 0
# while True:
#     val = inputs[i]
#     i += 1
#     if val == 'quit':
#         break
#     print(int(val) * 2)







# Lesson 1.6: FOR LOOPS - ITERATE OR PERISH, YOU REPETITIVE BASTARD For: Loops
# over iterables (lists, range, etc.). Cleaner than while for known sequences.
# Covers: basic list, range (lazy nums), list comps (condensed power),
# enumerate (idx hack), zip (mash iterables), generators (low-mem yields). All
# double 1-5.
# 
# print("=== Basic for over list ===")
# for num in [1,2,3,4,5]:  # Grabs each item.
#     print(num * 2)
# 
# print("\n=== Range ===")
# for num in range(1,6):  # Efficient seq: start, stop (exclusive), step=1.
#     print(num * 2)
# 
# print("\n=== List Comp ===")
# [print(num * 2) for num in range(1,6)]  # [expr for item in iter]; list-building ninja.
# 
# print("\n=== Enumerate ===")
# for idx, num in enumerate(range(1,6), start=0):  # (idx, item) tuples. No manual counting.
#     print(f"Idx {idx}: {num * 2}")
# 
# print("\n=== Zip ===")
# evens = [2,4,6,8,10]
# for doubled in zip(range(1,6), evens):  # Pairs into tuples; shortest rules.
#     print(doubled[1])
# 
# print("\n=== Generator ===")
# for doubled in (num * 2 for num in range(1,6)):  # (expr for item in iter): Yields lazy, saves RAM.
#     print(doubled)
#
# print("\n=== Generator function ===")
# def doubled(n):
#     num = 1
#     while num <= n:
#         yield num * 2
#         num +=1
#
# for i in doubled(5):
#     print(i)






# Lesson 1.7: CHAINING FOR LOOPS - NEST 'EM LIKE A RUSSIAN DOLL, YOU RECKLESS
# HIERARCHY WHORE For loops ain't just for wimps iterating singly; chain the
# bastards into nests for multi-dimensional madness. Outer loop bosses the big
# picture, inners grind the guts. But beware: O(n*m*k) complexity can fuck
# your runtime harder than a kernel panic. We'll do a 2D grid (matrix
# multiplication lite), then a 3-level beast for volume calcs. No while loops
# here—fors are cleaner for known depths, you lazy sod.
# 
# print("=== Basic 2-Level Nest: 3x3 Grid of Doubled Products ===")
# # Outer: rows. Inner: cols. Print a table of row*col*2
# for row in range(1, 4):
#     print(f"Row {row}:", end=" ")
#     for col in range(1, 4):
#         print(f"{(row * col * 2):2d}", end=" ")
#     print()
# 
# print("\n=== 3-Level Nest: Volume of Boxes (l*w*h) ===")
# # Now triple-chain: lengths, widths, heights. Sum volumes for a 2x2x2 cube of units.
# # Nested loops to grind out each box, pretty-printed like a goddamn artisan.
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
# print(f"Total volume of all boxes: {total_volume} cubic units, you volume-hoarding prick.")
# 
# print("\n=== Nested Loops for Products Grid ===")
# # Ditch that lazy list comp—grind it with loops for a crisp 2x3 table of row*col.
# print("Row\\Col | 1   2   3")
# print("--------+---------")
# for row in range(1, 3):
#     print(f"  {row}    |", end=" ")
#     for col in range(1, 4):
#         prod = row * col
#         print(f"{prod:>3} ", end="")
#     print()
# 
# print("\n=== Nested Loops for Masochists: 2x3x4x5 Product Hell ===")
# # Quad-nest the bastards—r*c*h*d, but slice it into a pretty multi-line dump 'cause flat lists are for pussies.
# print("r\\c/h/d | Products (sampled hell)")
# print("---------+-------------------")
# count = 0
# for r in range(1, 3):
#     for c in range(1, 4):
#         for h in range(1, 5):
#             for d in range(1, 6):
#                 prod = r * c * h * d
#                 if count % 6 == 0:  # Line-break every 6 to not barf on the terminal.
#                     print(f"{r:1}x{c:1}x{h:1}x{d:1} |", end=" ")
#                 print(f"{prod:4}", end=" ")
#                 count += 1
#                 if count % 6 == 0:
#                     print()
#             if count % 6 != 0:
#                 print()
# 
# print("\n=== Nested Loops for Volumes: Custom Rows/Cols/Depths ===")
# # Loops over lists? Hell yeah—r*c*d volumes, tabulated like a proctologist's chart.
# rows = [1, 2]
# cols = [3, 4, 5]
# depths = [6, 7]
# print("R\\C/D  |", " ".join(f"{c:>3}" for c in cols))
# print("-------+--------------------------------")
# for r in rows:
#     line = f"{r:1}     |"
#     for c in cols:
#         subline = ""
#         vols = []
#         for d in depths:
#             vol = r * c * d
#             vols.append(vol)
#             subline += f"{vol:3} "
#         line += subline.strip() + " |"
#     print(line)
# 
# print("\n=== Break/Escape the Nest: Early Outs ===")
# # Bail-out nest: outer hunts, inner multiplies—break when >10, flag the chaos.
# found = False
# print("Outer | Inner Products (bail at >10)")
# print("------+--------------------------------")
# for outer in range(1, 6):
#     print(f"{outer:>5} |", end="")
#     all_fine = True
#     for inner in range(1, 6):
#         prod = outer * inner
#         if prod > 10:
#             print(f" {inner}: {prod} - TOO BIG, GTFO!", end="")
#             all_fine = False
#             break
#         else:
#             print(f" {inner}: {prod:>2}", end="   ")
#     if all_fine:
#         print(" - All inners were fine, the wimps.")
#     else:
#         print()
#     if found:
#         break
#     if not all_fine:
#         found = True







# Lesson 1.8: DEFINE A FUNCTION
# Def greet(name): return f"Hello, {name}!"
# Then call greet("Linus") and print it
# Functions? Yeah, because hardcoding everything is for amateurs. Don't screw this up.
# -------------------------------------------------------------------------------- 
# def greet(name):
#     return f"Hello, {name}!"
# 
# print(greet("Linus"))







# Lesson 1.9: TRY-EXCEPT
# Try to divide 10/0, catch ZeroDivisionError, print "Can't divide by zero, idiot"
# -------------------------------------------------------------------------------- 
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Can't divide by zero, idiot")







# ===== LESSON 2: CLASSES, DECORATORS, GENERATORS, AND CONTEXT MANAGERS =====

# Lesson 2.1: SIMPLE CLASS
# Class Dog: def __init__(self, name): self.name = name
# def bark(self): print(f"{self.name} says woof!")
# Then dog = Dog("Fido"), dog.bark()
# Oh, classes now? Because your code wasn't bloated enough with global variables. Just don't make it a mess like some kernel modules I've seen.
# -------------------------------------------------------------------------------- 
# class Dog:
#     def __init__(self, name):
#         self.name = name
# 
#     def bark(self):
#         print(f"{self.name} says woof!")
# 
# dog = Dog("Fido")
# dog.bark()







# Lesson 2.2: DECORATORS - WRAP YOUR FUNCTIONS LIKE A PRO
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







# Lesson 2.3: GENERATORS - LAZY LISTS, SAVE MEMORY
# Def fib(n): a=0;b=1; while a<n: yield a; a,b = b, a+b
# Then for i in fib(10): print(i)
# Generators? Finally, something that doesn't waste memory like your bloated C++ code. Lazy evaluation—because who needs to compute everything upfront when you can pretend you're efficient?
# -------------------------------------------------------------------------------- 
# def fib(n):
#     a = 0
#     b = 1
#     while a < n:
#         yield a
#         a, b = b, a + b
# 
# for i in fib(10):
#     print(i)
# 







# Lesson 2.4: CONTEXT MANAGERS - WITH BLOCKS, CLEANUP AUTOMAGIC
# Class Timer: def __enter__(self): self.start=time.time(); return self
# def __exit__(self, *args): print(time.time()-self.start)
# with Timer(): time.sleep(1); print("Slept")
# Context managers? Finally, a way to force your code to clean up after itself without 
# you forgetting like a braindead intern. Automagic cleanup—because who has time for 
# try-finally bullshit?
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







