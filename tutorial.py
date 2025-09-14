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

# Lesson 1.1: VARIABLES - STORE YOUR CRAP
# Create a variable 'name' with your name as string, then print "My name is {name}"
# name = "Linus"
# print(f"My name is {name}")







# Lesson 1.2: BASIC MATH
# Compute 2 * (2 + 3) / 4 - 1 and print the result (should be 1.5)
# result = 2 * (2 + 3) / 4 - 1
# print(result)






# Lesson 1.3: STRINGS AND LISTS
# Make a list ['apple', 'banana', 'cherry'], add 'date' to end, print the list
# fruits = ['apple', 'banana', 'cherry']
# fruits.append('date')
# print(fruits)








# Lesson 1.4: IF STATEMENTS
# Set age = 25, if age >= 18 print "Adult", else "Kid"
# age = 25
# if age>=18:
#     print("Adult")
# else:
#     print("Kid")






# Lesson 1.5: FOR LOOPS
# Loop over [1,2,3,4,5], print each * 2
# for num in [1,2,3,4,5]:
#     print(num * 2)









# Lesson 1.6: DEFINE A FUNCTION
# Def greet(name): return f"Hello, {name}!"
# Then call greet("Linus") and print it
# Functions? Yeah, because hardcoding everything is for amateurs. Don't screw this up.
# 
# def greet(name):
#     return f"Hello, {name}!"
# 
# print(greet("Linus"))














# Lesson 1.7: TRY-EXCEPT
# Try to divide 10/0, catch ZeroDivisionError, print "Can't divide by zero, idiot"
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Can't divide by zero, idiot")








# Lesson 1.8: SIMPLE CLASS
# Class Dog: def __init__(self, name): self.name = name
# def bark(self): print(f"{self.name} says woof!")
# Then dog = Dog("Fido"), dog.bark()
# Oh, classes now? Because your code wasn't bloated enough with global variables. Just don't make it a mess like some kernel modules I've seen.
# 
# class Dog:
#     def __init__(self, name):
#         self.name = name
# 
#     def bark(self):
#         print(f"{self.name} says woof!")
# 
# dog = Dog("Fido")
# dog.bark()








# Lesson 1.9: DECORATORS - WRAP YOUR FUNCTIONS LIKE A PRO
# Def timer(func): import time; start=time.time(); func(); print(time.time()-start)
# @timer def slow(): time.sleep(1); print("Done")
# slow()
# Decorators? Fancy wrapping paper for your sloppy functions. At least this one times how long your crap takes to run—probably forever if you're debugging.
# 
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













# Lesson 1.10: GENERATORS - LAZY LISTS, SAVE MEMORY
# Def fib(n): a=0;b=1; while a<n: yield a; a,b = b, a+b
# Then for i in fib(10): print(i)
# Generators? Finally, something that doesn't waste memory like your bloated C++ code. Lazy evaluation—because who needs to compute everything upfront when you can pretend you're efficient?
# 
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








# Lesson 1.12: CONTEXT MANAGERS - WITH BLOCKS, CLEANUP AUTOMAGIC
# Class Timer: def __enter__(self): self.start=time.time(); return self
# def __exit__(self, *args): print(time.time()-self.start)
# with Timer(): time.sleep(1); print("Slept")
# Context managers? Finally, a way to force your code to clean up after itself without you forgetting like a braindead intern. Automagic cleanup—because who has time for try-finally bullshit?
# 
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






















