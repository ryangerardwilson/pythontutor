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
# 
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
# 
# # Sets (set, frozenset)
# s = {1, 2}
# s.__contains__(2)     # 2 in s
# s.__len__()           # len(s)
# it = s.__iter__()     # iter(s)
# s.__and__({2})        # s & {2}
# s.__or__({3})         # s | {3}
# # s.add(4) uses __hash__ on elements
# 
# # Numbers (int, float, complex)
# i = 42
# i.__add__(5)          # i + 5
# i.__sub__(10)         # i - 10
# i.__mul__(2)          # i * 2
# i.__truediv__(3)      # i / 3
# i.__floordiv__(3)     # i // 3
# i.__mod__(5)          # i % 5
# i.__pow__(2)          # i ** 2
# i.__neg__()           # -i
# i.__abs__()           # abs(i)
# i.__lt__(50)          # i < 50
# i.__eq__(42)          # i == 42
# i.__hash__()          # hash(i)
# i.__bool__()          # bool(i)
# 
# # Functions
# def func(x): pass
# func.__call__(5)      # func(5)
# 
# # Files
# with open('temp.txt', 'w') as f: pass  # f.__enter__(), f.__exit__()
# # for line in f: pass  # f.__iter__(), iterator.__next__()
# 
# # Others
# (42).__str__()        # str(42)
# [1].__repr__()        # repr([1])
# (42).__format__('x')  # format(42, 'x')







# Lesson 1.4: Python's Dunder Methods Dunders let classes emulate built-ins.
# Use semantically; read docs.python.org/3/reference/datamodel.html.
# --------------------------------------------------------------------------------
# import asyncio
# 
# class MyClass:
#     # Creation/Destruction
#     # Enables syntax: obj = MyClass(...) (invokes __new__ to create the instance)
#     def __new__(cls, *args):
#         # __new__ is the actual constructor: allocates memory and creates the
#         # object instance before __init__ runs. Here, we're just deferring to
#         # the superclass to do the heavy lifting.
#         return super().__new__(cls)
# 
#     # Enables syntax: obj = MyClass(...) (called after __new__ to initialize)
#     def __init__(self, v, x=1, y=2):
#         # __init__ initializes the already-created object: sets up attributes
#         # like self.v. It's not the constructor, despite what some sloppy
#         # tutorials say.
#         self.v = v
#         self.x = x  # For vector ops
#         self.y = y  # For vector ops
#         self.d = [1, 2, 3]  # For container ops, hardcoded for demo
#         self.resource = open('tempfile.txt', 'w')  # Pretend resource to clean up
# 
#     # Enables syntax: del obj (or when reference count drops to zero, triggering GC)
#     def __del__(self):
#         # __del__ is the destructor: called when the object is about to be
#         # garbage-collected. This one's a no-op, which is fine unless you need
#         # to clean up resources—don't rely on it for critical stuff, Python's
#         # GC isn't deterministic.
#         if hasattr(self, 'resource') and self.resource:
#             self.resource.close()
#             print(f"Cleaned up resource for object with v={self.v}")
# 
#     # Representation
#     # Enables syntax: print(obj) or str(obj)
#     def __str__(self):
#         return "Nice"
# 
#     # Enables syntax: repr(obj) or interactive shell display
#     def __repr__(self):
#         return f"MyClass(v={self.v})"
# 
#     # Enables syntax: f"{obj:spec}" (formatted string literals)
#     def __format__(self, s):
#         return f"Fmt {s}"
# 
#     # Attributes
#     # Enables syntax: obj.nonexistent_attr (for undefined attributes)
#     def __getattr__(self, n):
#         return 42
# 
#     # Enables syntax: obj.attr = value (called for all attribute assignments)
#     def __setattr__(self, n, v):
#         super().__setattr__(n, v)
# 
#     # Containers
#     # Enables syntax: len(obj)
#     def __len__(self):
#         return len(self.d)
# 
#     # Enables syntax: obj[key] (getitem access)
#     def __getitem__(self, k):
#         return self.d[k]
# 
#     # Enables syntax: obj[key] = value (setitem assignment)
#     def __setitem__(self, k, v):
#         self.d[k] = v
# 
#     # Enables syntax: item in obj (membership test)
#     def __contains__(self, i):
#         return i in self.d
# 
#     # Enables syntax: for x in obj: ... (iteration)
#     def __iter__(self):
#         return iter(self.d)
# 
#     # Operators
#     # Enables syntax: obj1 + obj2 (addition)
#     def __add__(self, o):
#         # Returns a new MyClass with dummy v=0, because we're forcing this mess
#         return MyClass(0, self.x + o.x, self.y + o.y)
# 
#     # Enables syntax: obj1 == obj2 (equality comparison)
#     def __eq__(self, o):
#         return self.x == o.x and self.y == o.y
# 
#     # Enables syntax: obj1 < obj2 (less-than comparison)
#     def __lt__(self, o):
#         return self.x**2 + self.y**2 < o.x**2 + o.y**2
# 
#     # Contexts
#     # Enables syntax: with obj: ... (enter context)
#     def __enter__(self):
#         return self
# 
#     # Enables syntax: with obj: ... (exit context, handles exceptions)
#     def __exit__(self, *e):
#         return True
# 
#     # Others
#     # Enables syntax: obj(...) (calling instance like a function)
#     def __call__(self, *a):
#         pass
# 
#     # Enables syntax: hash(obj) (for use in sets/dicts)
#     def __hash__(self):
#         return 42
# 
#     # Enables syntax: bool(obj) or if obj: ... (truth value testing)
#     def __bool__(self):
#         return True
# 
#     # Async (3.5+)
#     # Enables syntax: async for x in obj: ... (async iteration start)
#     def __aiter__(self):
#         self._i = 0  # Reset counter for async iteration
#         return self
# 
#     # Enables syntax: async for x in obj: ... (async next item)
#     async def __anext__(self):
#         if self._i < 3:
#             await asyncio.sleep(0.1)  # Simulate some async work, like I/O
#             val = self._i
#             self._i += 1
#             return val
#         else:
#             raise StopAsyncIteration
# 
# # Usage examples, adjusted for the monolith
# obj = MyClass(42)  # Creates obj: calls __new__ then __init__
# del obj  # Explicitly deletes reference; __del__ might get called soonish,
#          # but don't count on timing
# 
# o = MyClass(42)
# print(o); repr(o); f"{o:x}"
# 
# a = MyClass(42)
# a.foo; a.bar = 99
# 
# c = MyClass(42)
# len(c); c[1]; c[1]=99; 99 in c; for x in c: pass
# 
# v1, v2 = MyClass(0, 1, 2), MyClass(0, 3, 4)  # Dummy v=0 for vector focus
# v1 + v2; v1 == v2; v1 < v2
# 
# with MyClass(42): pass
# 
# func = MyClass(42); func(1)
# 
# h = MyClass(42); bool(h); hash(h)
# 
# # Proper async usage example
# async def main():
#     async_iter = MyClass(42)
#     async for x in async_iter:
#         print(f"Async yielded: {x}")
# 
# if __name__ == "__main__":
#     asyncio.run(main())  # Run the async main; outputs 0,1,2 with delays







# Lesson 1.5: CRUD Operations on Native Python Sequences Covering lists
# (mutable—actually useful), strings/tuples (immutable—wasteful for mutations).
# CRUD: Create (add), Read (access), Update (modify), Delete (remove).
# Immutables force new objects on C/U/D—lame perf hit, but that's Python for
# you.
# --------------------------------------------------------------------------------
# LISTS: Mutable sequences—proper for dynamic collections.
fruits = ['apple', 'banana', 'cherry']
print(fruits)  
# READ: Indexing (0-based, negative reverse), slicing, membership
print(fruits[0])     # 'apple' (index access)
print(fruits[-1])    # 'cherry'
print(fruits[1:3])   # ['banana', 'cherry'] (slice)
print('banana' in fruits)  # True (membership)
# CREATE: append (end), insert (position), extend (multiple), +/+= (concat, new or in-place)
fruits.append('date')         # Add to end (in-place)
print(fruits)                 # ['apple', 'banana', 'cherry', 'date']
fruits.insert(1, 'apricot')   # Insert at index 1 (in-place)
print(fruits)                 # ['apple', 'apricot', 'banana', 'cherry', 'date']
fruits.extend(['elderberry', 'fig'])  # Add iterable (in-place)
print(fruits)                 # ['apple', 'apricot', 'banana', 'cherry', 'date', 'elderberry', 'fig']
new_fruits = fruits + ['grape']  # Concat to new list
print(new_fruits)             # ... + 'grape'
fruits += ['honeydew']        # In-place extend
print(fruits)                 # ... + 'honeydew'
# UPDATE: Assign via index/slice
fruits[0] = 'avocado'         # Single item
print(fruits)                 # ['avocado', ...]
fruits[1:3] = ['blueberry', 'blackberry']  # Slice replace (can change length)
print(fruits)                 # ['avocado', 'blueberry', 'blackberry', ...]
# DELETE: pop (index, returns), remove (value), del (index/slice), clear (all)
popped = fruits.pop(2)        # Remove/return index 2
print(popped)                 # 'blackberry'
print(fruits)                 # ['avocado', 'blueberry', ...]
fruits.remove('cherry')       # First value occurrence
print(fruits)                 # Without 'cherry'
del fruits[3]                 # By index
print(fruits)                 # Without index 3
del fruits[1:3]               # Slice
print(fruits)                 # Shorter
fruits.clear()                # Nuke all
print(fruits)                 # []

# STRINGS: Immutable sequences—mutations create new strings. Allocation hell.
# Create a string
greeting = "hello world"
print(greeting)  # 'hello world'
# READ: Indexing, slicing, membership (returns substrings)
print(greeting[0])    # 'h'
print(greeting[-1])   # 'd'
print(greeting[6:11]) # 'world'
print('world' in greeting)  # True
# CREATE: +/+= (concat), join (from iterable)
greeting += "!"               # New string: 'hello world!'
print(greeting)
new_greeting = greeting + " again"  # Another new
print(new_greeting)           # 'hello world! again'
words = ['hello', 'world']
joined = ' '.join(words)      # New from iterable
print(joined)                 # 'hello world'
# UPDATE: replace (value), slicing + concat (manual)
updated = greeting.replace('world', 'universe')  # New string
print(updated)                # 'hello universe!'
updated = greeting[:5] + ' Python' + greeting[5:]  # Slice rebuild
print(updated)                # 'hello Python world!'
# DELETE: replace to empty, slicing exclude
removed = greeting.replace('world', '')  # New, removes 'world'
print(removed)                # 'hello !' (space remains)
removed = greeting[:6] + greeting[11:]  # Slice skip
print(removed)                # 'hello !'

# TUPLES: Immutable like strings, for fixed data. Same new-object nonsense for C/U/D.
# Create a tuple
coords = (1, 2, 3)
print(coords)  # (1, 2, 3)
# READ: Indexing, slicing, membership (new tuples for slices)
print(coords[1])    # 2
print(coords[0:2])  # (1, 2)
print(2 in coords)  # True
# CREATE: +/+= (concat to new)
new_coords = coords + (4,)    # New tuple
print(new_coords)             # (1, 2, 3, 4)
# UPDATE: Slicing + concat (new tuple)
updated = coords[:1] + (99,) + coords[2:]  # Rebuild
print(updated)                # (1, 99, 3)
# DELETE: Slicing exclude (new tuple)
removed = coords[:1] + coords[2:]  # Skip index 1
print(removed)                # (1, 3)







# Lesson 1.7: WHILE LOOPS - BECAUSE SOMETIMES YOU DON'T KNOW WHEN TO QUIT, YOU
# GLUTTON FOR PUNISHMENT While: Loops till a condition's false. Init var,
# check, do stuff, update—or infinite loop and watch your machine melt.
# Example: Double 1-5, but with a twist: count down from 10, break early if
# even. Covers basics, break/continue too.  Pro tip: Always update inside, or
# you're debugging a toaster.
# -------------------------------------------------------------------------------- 
# print("=== Basic while: Double 1-5 ===")
# num = 1
# while num <= 5:  # Loops as long as truthy.
#     print(num * 2)
#     num += 1  # Update or die trying.
# 
# print("\n=== NESTED WHILE DEMO ===\n")
# 
# count = 10
# while count > 0:
#     if count % 2 == 0:     # skip evens
#         count -= 1
#         continue
#     if count == 5:         # stop at 5
#         print("+----------------------------+")
#         print("|  Countdown stopped at 5!  |")
#         print("+----------------------------+\n")
#         break
# 
#     print(f"[COUNTDOWN] {count:2d} | doubled -> {count*2:2d}")
# 
#     # Nested loop: process inputs until 'quit'
#     inputs, i = ['3', '7', 'quit'], 0
#     print("  +-- Entering inner loop --+")
#     while True:
#         val = inputs[i]; i += 1
#         if val == 'quit':
#             print("  +-- Inner loop ended (saw 'quit') --+\n")
#             break
#         print(f"    input: {val:>2} -> doubled: {int(val)*2:2d}")
# 
#     count -= 1







# Lesson 1.8: FOR LOOPS AND ITERABLE DATA TYPES 
# Covers: basic list, range (lazy nums), list comps (condensed power),
# enumerate (idx hack), zip (mash iterables), generators (low-mem yields). All
# double 1-5.
# -------------------------------------------------------------------------------- 
# # Basic String Iteration: Char-by-Char Grind
# for char in "12345":
#     print(char)
# # Tuple: Immutable List Wannabe
# for num in (1, 2, 3, 4, 5):
#     print(num)
# # Dict Keys: Key-Value Tease Without Values
# my_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
# for key in my_dict:
#     print(key)
# # Set: Unordered Uniqueness Mess
# for num in {1, 2, 3, 4, 5}:
#     print(num)
# # Frozenset: Frozen Set, Because Mutability is for Wimps
# for num in frozenset({1, 2, 3, 4, 5}):
#     print(num)
# # Enumerate: Index Hack on Any Iterable
# # Need indices without ranges? Enumerate wraps any iterable, starting from 0.
# Here's on a string "abcde" (your 1-5 length proxy):
# for idx, char in enumerate("abcde"):
#     print(idx, char)
# # Zip: Mash Multiple Iterables Like a Bad Merge Conflict
# # Zip combines iterables element-wise. Pair a string "12345" with a tuple
# ('a','b','c','d','e'):
# for num, letter in zip("12345", ('a', 'b', 'c', 'd', 'e')):
#     print(num, letter)
# # Generators: Low-Mem Yields for the Memory-Stingy
# # Generators are iterables that yield on the fly. Define one that yields 1-5
# (no range, just a loop, but wait—crap, to avoid while, we'll fake it with a
# generator expression over a string or something dumb):
# # Generator Example 1
# def gen_1_to_5():
#     for char in "12345":
#         yield int(char)
# 
# for num in gen_1_to_5():
#     print(num)
# 
# # Generator Example 2
# def doubled(n):
#     num = 1
#     while num <= n:
#         yield num * 2
#         num +=1
#
# for i in doubled(5):
#     print(i)







# Lesson 1.8: CHAINING FOR LOOPS - NEST 'EM LIKE A RUSSIAN DOLL, YOU RECKLESS
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







# Lesson 1.9: DECORATORS - WRAP YOUR FUNCTIONS LIKE A PRO
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







# Lesson 1.10: GENERATORS - LAZY LISTS, SAVE MEMORY Def fib(n): a=0;b=1; while
# a<n: yield a; a,b = b, a+b Then for i in fib(10): print(i) Generators?
# Finally, something that doesn't waste memory like your bloated C++ code. Lazy
# evaluation—because who needs to compute everything upfront when you can
# pretend you're efficient?
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







# Lesson 1.11: CONTEXT MANAGERS - WITH BLOCKS, CLEANUP AUTOMAGIC 
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
