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
# Lesson 1.1: VARIABLES AND PYTHON DATA TYPES
# Variables: snake_case, no keywords. Dynamic typing—Python guesses, you verify
# with type(). Covering all built-ins: None, bool, int, float, complex, str, list,
# tuple, dict, set, frozenset, range, bytes, bytearray, memoryview, function
# 
# nothing = None
# is_sane = False
# age = 55
# pi = 3.14159
# z = 3 + 4j
# name = "Linus"
# bugs = [42, "panic", 0.1]
# coords = (10,20)
# prefs = {"os":"Linux"}
# idiots = {"user1","user2"}
# hell = frozenset(["debug", "monday"])
# r = range(5)
# b = b'hello'
# ba = bytearray(b'hello')
# mv = memoryview(ba)
# 
# # And a function, because why not
# def foo(): pass
# func = foo
# 
# # Print individually like this
# print(f"Nothing\t:\t{nothing}\t{type(nothing).__name__}")
# 
# # Or, loop over locals like this
# for variable_name, value in list(locals().items()):
#     if not variable_name.startswith('__'):
#         print(f"{variable_name}\t:\t{value}\t{type(value).__name__}")







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







# Lesson 1.5: FOR LOOPS
# Loop over [1,2,3,4,5], print each * 2
# -------------------------------------------------------------------------------- 
# for num in [1,2,3,4,5]:
#     print(num * 2)







# Lesson 1.6: DEFINE A FUNCTION
# Def greet(name): return f"Hello, {name}!"
# Then call greet("Linus") and print it
# Functions? Yeah, because hardcoding everything is for amateurs. Don't screw this up.
# -------------------------------------------------------------------------------- 
# def greet(name):
#     return f"Hello, {name}!"
# 
# print(greet("Linus"))







# Lesson 1.7: TRY-EXCEPT
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







# ========================= LESSON 3: DATA SCIENCE =========================
#
# Databases: don't fuck around with magic. Raw SQL, because ORMs are for lazy
# idiots.
#
# Lesson 3.1: BUILD THE TABLE PROPERLY - NO HAND-HOLDING
# --------------------------------------------------------------------------------
# pip install sqlalchemy mysql-connector-python pandas Table: id auto-inc,
# mobile, data (TEXT for JSON), timestamps that work.  JSON gen: dead simple,
# now with random crap so it's not the same boring shit every run.
#
# import pandas as pd from sqlalchemy import create_engine import os from
# datetime import datetime, timedelta import json import random  # For
# randomizing, because static data is for morons.
# 
# import os
# import json
# import random
# import pandas as pd
# from sqlalchemy import create_engine
# from datetime import datetime, timedelta
# 
# user = 'root'
# password = 'password12345'
# host = 'localhost'
# database = 'test'
# 
# engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')
# 
# def gen_json(id: int) -> dict:
#     names = ['Alice', 'Bob', 'Charlie', 'Dana', 'Eve']
#     user_name = random.choice(names) + f'_{id}'
#     score = random.randint(50, 200)
#     active = random.choice([True, False])
#     num_items = random.randint(2, 5)
#     items = [f"item{random.randint(1,10)}_{i}" for i in range(1, num_items+1)]
#     return {
#         "user": user_name,
#         "score": score,
#         "active": active,
#         "items": items
#     }
# 
# with engine.connect() as conn:
#     conn.execute("DROP TABLE IF EXISTS testtable")
#     conn.execute("""
#         CREATE TABLE testtable (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             mobile VARCHAR(20) NOT NULL,
#             data TEXT,
#             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#             updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
#         )
#     """)
#     mobiles = ['+1-555-1234', '+1-555-5678', '+1-555-9012']
#     values = [(mobiles[i-1], json.dumps(gen_json(i))) for i in range(1,4)]
#     conn.executemany("INSERT INTO testtable (mobile, data) VALUES (%s, %s)", values)
#     conn.commit()







# Lesson 3.2: FETCH TO DF - CACHE IT, DON'T BE STUPID
# --------------------------------------------------------------------------------
# One-hour cache. Query if stale.
#
# import os 
# import pandas as pd 
# from sqlalchemy import create_engine 
# from datetime import datetime, timedelta 
#
# user = 'root'
# password = 'password12345'
# host = 'localhost'
# database = 'test'
#
# engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')
#
# cache_file = 'data_cache.csv'
# cache_h = 1
# 
# def get_df() -> pd.DataFrame:
#     if os.path.exists(cache_file):
#         age = datetime.now() - datetime.fromtimestamp(os.path.getmtime(cache_file))
#         if age < timedelta(hours=cache_h): return pd.read_csv(cache_file)
#     with engine.connect() as conn:
#         df = pd.read_sql_query("SELECT * FROM testtable", conn)
#     df.to_csv(cache_file, index=False)
#     return df
# 
# df = get_df()
# print(df)

















