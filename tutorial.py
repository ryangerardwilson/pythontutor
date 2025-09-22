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

    First off, if you're going to mess around with this in the Python REPL like a
    sane person, set it up properly with vi editing mode.

    - Step 1: Create or edit your ~/.pythonrc.py file (yeah, Python runs this on
    interactive startup). Fire up your editor—use vim, obviously—and add this:

    import readline
    readline.parse_and_bind('set editing-mode vi')

    - Step 2: Make sure this gets loaded every time you start Python interactively.
    Add this line to your ~/.bashrc (or .bash_profile if you're on some weird
    setup):

    export PYTHONSTARTUP=~/.pythonrc.py

    - Step 3: Then source your bashrc to apply it immediately: source ~/.bashrc

    Now, drop into the Python REPL (just type 'python' or 'python3' in your
    terminal), and start typing in these examples one by one.
"""
# ================== LESSON 1: TYPES ==================
# Lesson 1.1: PRINTING PYTHON TYPES
#
# Types: Every single thing in Python is an object, and every object has a
# type—check it with type(some_shit), which spits back the class that owns it.
# And get this: types themselves are objects too, created by the metaclass type
# (yeah, it's turtles all the way down, you recursive nightmare).
#
# --------------------------------------------------------------------------------
# 1. Define basic types, including the ironic type of type:
# >>> x = type
# >>> type(x) # Oh, the irony: <class 'type'>
# <class 'type'>
# >>> nothing = None
# >>> type(nothing) # NoneType
# <class 'NoneType'>
# >>> is_sane = False
# >>> type(is_sane) # bool
# <class 'bool'>
# >>> age = 55
# >>> type(age) # int
# <class 'int'>
# >>> pi = 3.14159
# >>> type(pi) # float
# <class 'float'>
# >>> z = 3 + 4j
# >>> type(z) # complex
# <class 'complex'>
# >>> name = "Linus"
# >>> type(name) # str
# <class 'str'>
#
# # 2. Collections:
# >>> bugs = [42, "panic", 0.1]
# >>> type(bugs) # list
# <class 'list'>
# >>> coords = (10, 20)
# >>> type(coords) # tuple
# <class 'tuple'>
# >>> prefs = {"os": "Linux"}
# >>> type(prefs) # dict
# <class 'dict'>
# >>> idiots = {"user1", "user2"}
# >>> type(idiots) # set
# <class 'set'>
# >>> hell = frozenset(["debug", "monday"])
# >>> type(hell) # frozenset
# <class 'frozenset'>
# >>> r = range(5)
# >>> type(r) # range
# <class 'range'>
#
# # 3. Binary stuff:
# >>> b = b'hello'
# >>> type(b) # bytes
# <class 'bytes'>
# >>> ba = bytearray(b'hello')
# >>> type(ba) # bytearray
# <class 'bytearray'>
# >>> mv = memoryview(ba)
# >>> type(mv) # memoryview
# <class 'memoryview'>
#
# # 4. Functions and classes:
# >>> def foo(): pass
# ...
# >>> func = foo
# >>> type(func) # function
# <class 'function'>
#
# >>> class Dog:
# ... def __init__(self, name): self.name = name
# ... def bark(self): print(f"{self.name} woofs!")
# ...
# >>> type(Dog) # type (the class itself)
# <class 'type'>
# >>> dog = Dog("Fido")
# >>> type(dog) # Dog (instance)
# <class '__main__.Dog'>
#
# # 5. Modules are types too—import one and weep at the consistency:
# >>> import math
# >>> m = math
# >>> type(m) # module
# <class 'module'>
#
# # 6. If you're too lazy to check one by one, dump 'em all (but you should've explored already):
# >>> for var, val in sorted(locals().items()):
# ... if not var.startswith('__'):
# ... print(f"{var}:\t{val}\t{type(val).__name__}")








# ============= LESSON 1.2: TYPES VERSUS SYNTAX  =====================
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
# 
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
# -------------------------------------------------------------------------------- 
# # While this will show the type
# >>> type(5)
# # This will throw an invalid syntax error, because + is not a type
# >>> type(+)
#   File "<stdin>", line 1
#     type(+)
#           ^
# SyntaxError: invalid syntax








# ============= LESSON 1.3: BUILT-IN INTROSPECTION TOOLS =====================
#
# Alright, you clueless kernel hackers masquerading as Python noobs, we've
# covered types and how they're not the same as the syntactic glue holding your
# crappy code together. Now, let's talk about actually poking around in
# Python's guts without breaking everything—using type(), help(), dir(), and
# since you whiny bastards asked, vars(), globals(), locals(), and id(). These
# are your basic introspection tools, because god forbid you read the docs like
# a normal person. They're built-ins, so no imports needed (except maybe
# inspect if you graduate to real debugging), and they'll save you from blindly
# guessing what the hell an object can do.
#
# Quick distinction, because I know you're too lazy to think:
# - type(obj): Tells you the class (type) of the object. Quick and dirty.
# - help(obj): Dumps docstrings and usage; paginates for long stuff—hit 
#   'q' to quit.
# - dir(obj): Lists attributes and methods—no details, just names.
# - vars(obj): Returns the __dict__ as a dict (attributes and values); fails on 
#   objects without one.
# - globals(): Current global namespace dict.
# - locals(): Current local namespace dict (same as globals() at top-level).
# - id(obj): Unique integer ID (memory address in CPython); check for aliases.
#
# Exiting help()? Hit 'q'. The rest don't trap you.
# --------------------------------------------------------------------------------
# >>> import math
# >>> type(math)
# <class 'module'>
# >>> dir(math)  # pi, sin, etc.
# ['__doc__', ... 'ulp']  # truncated for brevity
# >>> help(math)  # docs; q to quit
# Help on module math: ... (hit q)
# >>> vars(math)  # module dict
# {'__name__': 'math', ...}
# >>> id(math)
# 140000000000001  # varies







# ================== LESSON 2: THE PYTHON DATA MODEL =========================
# Ditch examples; learn by exploring in REPL. Master this, and the rest is
# pointless.
# 
#               LESSON 2.1: EXPLORING OBJECTS AND DUNDER METHODS IN THE REPL
#
# Start REPL: python
#
# 1. Create objects:
# >>> l = [1, 2, 3]
# >>> t = (1, 2, 3)
# >>> s = "abc"
# >>> d = {'a': 1}
# >>> r = range(5)
# >>> b = b'bytes'
# 
# 2. List attributes (dir(obj) returns all attrs/methods for obj—peek inside):
# >>> dir(l)  # See __dunders__
# 
# >>> help(l)                # List docs
# >>> help(str)              # String docs
# >>> help(dict)             # Dict docs
# 
# 4. Specific dunder docs:
# >>> help(list.__getitem__)
# 
# 5. Experiment (call dunders directly here only; use syntax in code):
# >>> l.__len__()                       # len(l)
# >>> l.__getitem__(1)                  # l[1]; try slice(1, None)
# >>> s.__contains__('b')               # 'b' in s
# >>> it = l.__iter__(); it.__next__()
# >>> l.__setitem__(0, 99)              # l[0]=99; fails on tuple
# >>> s.__add__("def")                  # s + "def"
# >>> s.__mul__(3)                      # s * 3








# ================== LESSON 2: THE PYTHON DATA MODEL =========================
# Lesson 2.2: Implementing Dunder Methods in Custom Classes

# Don't just copy built-ins like a moron—emulate them properly. RTFM at
# docs.python.org/3/reference/datamodel.html, you lazy bastard. The real
# learning happens in the REPL: Define classes, add dunders one by one, poke at
# 'em, see what breaks. That's how you grok why Python's object model isn't
# complete garbage.

# Fire up REPL (python in terminal). Type this crap in, experiment as you go.
# Add dunders incrementally—test after each, use dir(),
# print(pydoc.render_doc(your_class)) to inspect.

# 1. Start with a bare class—boring, but baseline:
# >>> class MyClass:
# ...     """This is my docstring, it will get printed pursuant to the
# ...        help() method or the chained .__doc__ method"""
# ...     pass
# >>> obj = MyClass()
# >>> dir(obj)  
# >>> help(MyClass)
# >>> print(MyClass.__doc__)

# 2. Add __init__ for state:
# >>> class MyClass:
# ...     def __init__(self): self.d = [1, 2, 3]  
# >>> obj = MyClass()
# >>> obj.d  

# 3. Implement __str__ for nice printing:
# >>> class MyClass:
# ...     def __init__(self): self.d = [1, 2, 3]  
# ...     def __str__(self): return "Nice object with data: " + str(self.d)
# >>> obj = MyClass()
# >>> print(obj)  

# 4. Add __len__:
# >>> class MyClass:
# ...     def __init__(self): self.d = [1, 2, 3]  
# ...     def __len__(self):
# ...         return len(self.d)
# >>> len(obj)  # Test. Fail? Redefine class.

# 5. __getitem__ for subscripting:
# >>> class MyClass:
# ...     def __init__(self): self.d = [1, 2, 3]  
# >>>     def __getitem__(self, k):
# ...         return self.d[k]
# >>> obj[1]  # 2. Try slices: obj[1:], obj[0:2]. Boom if no slice handling—read docs, handle isinstance(k, slice).

# 6. __setitem__ for assignment:
# >>> class MyClass:
# ...     def __init__(self): self.d = [1, 2, 3]  
# >>>     def __setitem__(self, k, v):
# ...         self.d[k] = v
# >>> obj[0] = 99; print(obj[0])  # Mutate and check.

# 7. __contains__ for 'in':
# >>> class MyClass:
# ...     def __init__(self): self.d = [1, 2, 3]  
# >>>     def __contains__(self, i):
# ...         return i in self.d
# >>> 2 in obj  # True.

# 8. __iter__ for looping:
# >>> class MyClass:
# ...     def __init__(self): self.d = [1, 2, 3]  
# >>>     def __iter__(self):
# ...         return iter(self.d)
# >>> for x in obj: print(x)  # Iterates over d.

# 9. Context manager: __enter__ and __exit__:
# >>> class MyClass:
# ...     def __init__(self): self.d = [1, 2, 3]  
# >>>     def __enter__(self):
# ...         self.backup = self.d.copy()  # Backup
# ...         return self
# >>>     def __exit__(self, *exc):
# ...         self.d = self.backup  # Restore
# ...         del self.backup
# ...         return False  # Propagate exceptions
# >>> with obj as mc:
# ...     mc[0] = 99
# ...     print(mc[0])  # 99
# >>> print(obj[0])  # Back to 1. Magic—no cleanup boilerplate.

# 10. __call__ to make obj callable:
# >>> class MyClass:
# ...     def __init__(self): self.d = [1, 2, 3]  
# >>>     def __call__(self, *a):
# ...         print("Called with:", a)
# >>> obj(42, "foo")  # Like a function.







# ================== LESSON 3: INTUITIVE CODING PATTERNS =========================
# Lesson 3.1: CRUD on sequences
# --------------------------------------------------------------------------------
# Sequences are ordered collections like lists, tuples, and strings. Sets are unordered but included here for CRUD ops.
# # LISTS (mutable sequences)
# >>> l = ['a', 'b', 'c']
# # read
# >>> l[0] # -- this calls l.__getitem__(0), grabbing the item at index 0
# 'a'
# >>> l[1:3] # -- this is slicing: starts at index 1 (inclusive), ends at 3 (exclusive), so grabs 'b' (index 1) and 'c' (index 2); calls l.__getitem__(slice(1,3))
# ['b', 'c']
# >>> 'b' in l # -- checks membership with l.__contains__('b')
# True
# # create (append/extend, but here we're using concatenation)
# >>> new = l + ['g']  # creates a new list; calls l.__add__(['g'])
# >>> new
# ['a', 'b', 'c', 'g']
# >>> l += ['h']  # modifies l in place; calls l.__iadd__(['h'])
# >>> l
# ['a', 'b', 'c', 'h']
# # update
# >>> l[0] = 'A'  # changes the item at index 0 in place; calls l.__setitem__(0, 'A')
# >>> l
# ['A', 'b', 'c', 'h']
# # delete
# >>> del l[3]  # removes item at index 3; calls l.__delitem__(3)
# >>> l
# ['A', 'b', 'c']
# >>> del l[1:3]  # removes slice from 1 to 3; calls l.__delitem__(slice(1,3))
# >>> l
# ['A']
#
# # TUPLES (immutable sequences -- no in-place mods, ops create new tuples)
# >>> t = ('a', 'b', 'c')
# # read
# >>> t[0] # -- t.__getitem__(0)
# 'a'
# >>> t[1:3] # -- slicing like lists; t.__getitem__(slice(1,3))
# ('b', 'c')
# >>> 'b' in t # -- t.__contains__('b')
# True
# # create
# >>> new = t + ('g',)  # creates new tuple; t.__add__(('g',))
# >>> new
# ('a', 'b', 'c', 'g')
# >>> t += ('h',)  # rebinds t to new tuple (no __iadd__ for immutables)
# >>> t
# ('a', 'b', 'c', 'h')
# # update -- can't, no __setitem__; fake with slicing/concat (new tuple)
# >>> t = ('a', 'b', 'c')  # reset
# >>> t[:1] + ('y',) + t[1:]  # new tuple; __getitem__ and __add__
# ('a', 'y', 'b', 'c')
# # delete -- can't in place, no __delitem__; fake with slicing (new tuple)
# >>> t[:1] + t[2:]  # "ac"; __getitem__ and __add__
# ('a', 'c')
#
# # STRINGS (immutable sequences -- similar to tuples)
# >>> s = "abc"
# # read
# >>> s[0] # -- s.__getitem__(0)
# 'a'
# >>> s[1:3] # -- slicing; s.__getitem__(slice(1,3))
# 'bc'
# >>> 'b' in s # -- s.__contains__('b')
# True
# # create
# >>> new = s + "e"  # new string; s.__add__("e")
# >>> new
# 'abce'
# >>> s += "d" # new string assigned back to s; effectively s = s.__add__("d") since no __iadd__ for immutables, but it rebinds
# >>> s
# 'abcd'
# # update (fake it with slicing, since no __setitem__ -- strings don't let you mutate)
# >>> s = "abc"  # reset for this example
# >>> s[:1] + 'y' + s[1:]  # creates new string "aybc" or whatever; uses __getitem__ for slices and __add__ for concat
# 'aybc'
# # delete (new string via slicing) - we don't use this for deleting items in lists, as it
# # creates a whole new object. But we make peace with this inefficiency for
# # strings, because strings are immutable and have no __delitem__
# >>> s = "abc"  # reset for this example
# >>> s[:1] + s[2:]  # "ac"; again, __getitem__ and __add__
# 'ac'
#
# # SETS (mutable but unordered -- no indexing/slicing, so CRUD is different)
# >>> se = {'a', 'b', 'c'}
# # read -- no indices, just membership/iteration
# >>> 'b' in se # -- se.__contains__('b')
# True
# # create
# >>> se.add('g')  # in place; no dunder, method call
# >>> se
# {'a', 'b', 'c', 'g'}
# >>> new = se | {'h'}  # new set; se.__or__({'h'})
# >>> new
# {'a', 'b', 'c', 'g', 'h'}
# >>> se |= {'i'}  # in place; se.__ior__({'i'})
# >>> se
# {'a', 'b', 'c', 'g', 'i'}
# # update -- no direct update since no keys/indices; remove then add
# >>> se.remove('a')  # remove 'a'
# >>> se.add('A')  # add 'A'
# >>> se
# {'A', 'b', 'c', 'g', 'i'}
# # delete
# >>> se.remove('i')  # removes if exists, else KeyError; no dunder, method
# >>> se
# {'A', 'b', 'c', 'g'}
# >>> se.discard('z')  # removes if exists, no error; method
# >>> se.pop()  # removes arbitrary element, returns it
# 'A'  # or whatever







# Lesson 3.2: CRUD on mappings
# --------------------------------------------------------------------------------
# Mappings are key-value collections like dicts.
# # DICTS (mutable mappings)
# >>> d = {'a': 1, 'b': 2, 'c': 3}
# # read
# >>> d['a'] # -- d.__getitem__('a')
# 1
# >>> 'b' in d # -- d.__contains__('b')
# True
# # create
# >>> d['g'] = 7  # adds new key-value; d.__setitem__('g', 7)
# >>> d
# {'a': 1, 'b': 2, 'c': 3, 'g': 7}
# >>> new = {**d, 'h': 8}  # new dict (or d | {'h': 8} in Python 3.9+; d.__or__({'h': 8}))
# >>> new
# {'a': 1, 'b': 2, 'c': 3, 'g': 7, 'h': 8}
# >>> d |= {'i': 9}  # in place (Python 3.9+; d.__ior__({'i': 9}))
# >>> d
# {'a': 1, 'b': 2, 'c': 3, 'g': 7, 'i': 9}
# # update
# >>> d['a'] = 10  # updates existing key; d.__setitem__('a', 10)
# >>> d
# {'a': 10, 'b': 2, 'c': 3, 'g': 7, 'i': 9}
# # delete
# >>> del d['i']  # removes key; d.__delitem__('i')
# >>> d
# {'a': 10, 'b': 2, 'c': 3, 'g': 7}
# >>> d.pop('g')  # removes and returns value; method
# 7
# >>> d
# {'a': 10, 'b': 2, 'c': 3}







# Lesson 3.3: LOOPS
# --------------------------------------------------------------------------------
# # Basic while: Double 1-3
# >>> num = 1
# >>> while num <= 3:  # Loops as long as truthy.
# ...     print(num * 2)
# ...     num += 1  # Update or die trying.
# ...
# 2
# 4
# 6

# # Basic String Iteration: Char-by-Char Grind
# >>> for char in "abc": print(char)
# ...
# a
# b
# c

# # Generators: Low-Mem Yields for the Memory-Stingy
# >>> def doubled(n):
# ...     num = 1
# ...     while num <= n:
# ...         yield num * 2
# ...         num +=1
# ...
# >>> for i in doubled(3):
# ...     print(i)
# ...
# 2
# 4
# 6

# # Sum volumes for a 2x2x2 cube of units.
# >>> total_volume = 0
# >>> for length in range(1, 3):
# ...     for width in range(1, 3):
# ...         for height in range(1, 3):
# ...             vol = length * width * height
# ...             print(f"{length} x {width} x {height} = {vol}")
# ...             total_volume += vol
# ...
# 1 x 1 x 1 = 1
# 1 x 1 x 2 = 2
# 1 x 2 x 1 = 2
# 1 x 2 x 2 = 4
# 2 x 1 x 1 = 2
# 2 x 1 x 2 = 4
# 2 x 2 x 1 = 4
# 2 x 2 x 2 = 8
# >>> print(f"Total volume of all boxes: {total_volume} cubic units")
# Total volume of all boxes: 27 cubic units

# # Same as above, but using list comprehension. Note we need 2 list
# # comprehension loops, despite the syntax being more concise
# >>> _ = [print(f"{length} x {width} x {height} = {length * width * height}")
# ...      for length in range(1, 3)
# ...      for width in range(1, 3)
# ...      for height in range(1, 3)]
# 1 x 1 x 1 = 1
# 1 x 1 x 2 = 2
# 1 x 2 x 1 = 2
# 1 x 2 x 2 = 4
# 2 x 1 x 1 = 2
# 2 x 1 x 2 = 4
# 2 x 2 x 1 = 4
# 2 x 2 x 2 = 8
# >>> total_volume = sum(length * width * height
# ...                    for length in range(1, 3)
# ...                    for width in range(1, 3)
# ...                    for height in range(1, 3))
# >>> print(f"Total volume of all boxes: {total_volume} cubic units")
# Total volume of all boxes: 27 cubic units







# ================== LESSON 3: INTUITIVE CODING PATTERNS =========================
# Lesson 3.4: DECORATORS and CONTEXT MANAGERS
# Look, in the real world, your functions aren't living in isolation—they're part
# of an ecosystem. Sometimes you need to add behavior around them without hacking
# up the original code like some amateur surgeon.
#
# Decorators: Syntactic sugar on higher-order functions to inject logging,
# timing, etc.  No direct dunder for function decorators—they're just closures.
# But if using a class as decorator, __init__ wraps the func, __call__ executes
# the wrapper.
#
# Context Managers: Force cleanup with 'with' blocks. What problem do they
# solve? Simple: programming is already a pain in the ass without you
# forgetting to clean up your crap. Resources like open files, database
# connections, or locks don't just vanish—they hang around leaking memory or
# causing deadlocks if you don't close 'em properly. Without context managers,
# you'd be stuck with ugly try-finally blocks everywhere to handle that
# cleanup, and let's be real, half you idiots would screw it up anyway,
# especially when exceptions blow everything to hell. Context managers solve
# this bullshit by wrapping your code in a 'with' statement that automagically
# sets up the resource (__enter__), runs your stuff, and tears it down
# (__exit__) no matter what—even if your code barfs an error. No more manual
# finally clauses, no leaks, just clean, idiot-proof code. Use 'em or keep
# writing kernel-panicky garbage.
#
# --------------------------------------------------------------------------------
# # Decorator example: Timer wrapper
# >>> import time
# >>> def timer(func):
# ...     def wrapper():
# ...         start = time.time()
# ...         func()
# ...         print(time.time() - start)
# ...     return wrapper
# ...
# >>> @timer
# ... def slow():
# ...     time.sleep(1)
# ...     print("Done")
# ...
# >>> slow()
# Done
# 1.00012345678  # or similar

# # Context Manager example: Timer class
# >>> import time
# >>> class Timer:
# ...     def __enter__(self):
# ...         self.start = time.time()
# ...         return self
# ...     def __exit__(self, *args):
# ...         print(time.time() - self.start)
# ...
# >>> with Timer():
# ...     time.sleep(1)
# ...     print("Slept")
# ...
# Slept
# 1.00012345678  # or similar







# ================== LESSON 4: PANDAS =========================
# Lesson 4.1: PRE-PANDAS - PART I - WARM UP
# --------------------------------------------------------------------------------

# Listen up, you aspiring data monkeys. Pandas DataFrames aren't some mystical
# voodoo—they're just glorified dictionaries and lists pumped up on NumPy
# steroids. If you don't grok the basics in pure Python, you'll treat Pandas
# like a black box and spew out crap code that leaks memory or crawls like a
# sloth in loops. This pre-crash course builds your intuition: wrangle data
# structures from scratch, manipulate them like a kernel hacker, and see how
# these patterns mirror what Pandas does efficiently. No fluff—bash this into
# your REPL, feel the burn, or go back to spreadsheets.

# 1. Sequences and Series-Like Structures (The 1D Backbone)

# Series analog: Lists as ordered, indexed, mutable data. Like Pandas Series
# without fancy labels—indexing via __getitem__, membership __contains__,
# iteration __iter__.  Zip: Iterator zipper for combining sequences, like
# aligning columns. Uses __iter__ and __next__.  Poor man's Series: Dict with
# labels as keys.  Why? Builds vector thinking for Series ops.

# >>> data = [10, 20, 30]  # Values
# >>> labels = ['a', 'b', 'c']  # Index
# >>> series_like = dict(zip(labels, data))  # Labeled data
# >>> series_like
# {'a': 10, 'b': 20, 'c': 30}
# >>> series_like['b']  # __getitem__
# 20
# >>> [val * 2 for val in data]  # Mapping, like Series.apply()
# [20, 40, 60]
# >>> 'b' in labels  # __contains__
# True

# 2. Multi-Dimensional Data: Lists of Lists and Dicts (DF Prototype)
# Row-major: Lists of lists for tables.
# Column-major: Dict of lists, keys as columns (Pandas DF internals).
# Transpose with zip(*data). CRUD: Append for rows, __setitem__ for updates.
# Why? Teaches alignment, indexing, shape—prevents "why does my DF explode?" idiocy.

# >>> table = [['name', 'age'], ['Alice', 30], ['Bob', 25]]  # Rows
# >>> columns = list(zip(*table))  # Transpose to columns
# >>> columns[1]  # Ages
# ('age', 30, 25)
# >>> dict_table = {'name': ['Alice', 'Bob'], 'age': [30, 25]}  # Columns
# >>> dict_table['age'][0] = 31  # Update: list.__setitem__
# >>> dict_table
# {'name': ['Alice', 'Bob'], 'age': [31, 25]}
# >>> [row for row in zip(*dict_table.values()) if row[1] > 25]  # Filter rows
# [('Alice', 31)]

# 3. Iteration and Comprehension Patterns (Workhorses)
# Zip for multi-iteration, like joining columns.
# Comprehensions for transform/filter.
# Enumerate for index-aware (iloc intuition).
# Why? Pandas apply/groupby/merge are efficient versions—think Pythonic before vectorized.

# >>> names = ['Alice', 'Bob']
# >>> ages = [30, 25]
# >>> for i, (name, age) in enumerate(zip(names, ages)):  # __iter__ on zip/enumerate
# ...     print(f"Row {i}: {name} is {age}")
# ...
# Row 0: Alice is 30
# Row 1: Bob is 25
# >>> {name: age * 2 for name, age in zip(names, ages)}  # Dict comp
# {'Alice': 60, 'Bob': 50}

# 4. Basic Aggregation and Slicing (No Loops Where Possible)
# Aggregates on sequences, zip for columns.
# Slicing multi-dim, like iloc.
# Defaultdict for grouping without KeyErrors (__missing__ magic).
# Why? df.sum() is this, but fast—avoid loop hell.

# >>> from collections import defaultdict
# >>> data = {'group': ['A', 'A', 'B'], 'value': [1, 2, 3]}
# >>> grouped = defaultdict(list)
# >>> for g, v in zip(data['group'], data['value']):
# ...     grouped[g].append(v)
# ...
# >>> grouped
# defaultdict(<class 'list'>, {'A': [1, 2], 'B': [3]})
# >>> {k: sum(v) for k, v in grouped.items()}  # Aggregate
# {'A': 3, 'B': 3}
# >>> data['value'][1:3]  # Slice: __getitem__(slice)
# [2, 3]

# 5. Edge Cases and Gotchas (Build Resilience)
# Zip truncates to shortest—pad if needed.
# Mutable vs immutable: Lists mutable, tuples not.
# Type consistency: Mix types? Fine in lists, but Pandas whines without object dtype.
# Why? Enforces clean data for Pandas.

# >>> list(zip([1, 2], [3]))  # Truncates
# [(1, 3)]
# >>> list(zip([1, 2, 3], [4, 5], fillvalue=None))  # itertools.zip_longest for padding
# Import itertools first, you idiot.
# >>> import itertools
# >>> list(itertools.zip_longest([1, 2, 3], [4, 5], fillvalue=None))
# [(1, 4), (2, 5), (3, None)]

# This is stone-age wrangling. Master it, or Pandas in the next sub-lesson will feel like cheating—but if you skip, your code will suck like most "data scientists'" garbage.









# Lesson 4.2: PRE-PANDAS PART II - MULTIDIMENSIONAL ARRAYS AND THEIR TRAVERSAL
# --------------------------------------------------------------------------------

# Listen up, you kernel-panicking code monkeys. If you think Pandas DFs are
# magic, wake up—they're built on multidimensional arrays, which in pure Python
# are just nested lists that suck for performance but build your intuition like
# 4.1. This lesson rips into traversing these beasts: rows, columns, zigzags,
# transposes, adjacent checks—like patching a filesystem without corrupting
# data. Why? Teaches you to manipulate grids without loops exploding your RAM,
# prepping for NumPy's vectorized glory in later crap. No fluff—bash these into
# REPL, fix the "problems" like a real hacker, or go back to single-dim lists
# and cry.

# We'll use nested lists as "arrays" (row-major), tie to 4.1's tables. Problems
# inspired by real-world idiocy: apartment buildings, bookshelves, restaurants,
# games, hikes. Master traversal, or your Pandas slices will segfault your
# brain.

# 1. Exploring Dimensions: Basics of Multi-Dim Arrays (Unit 1 Vibes)
# Nested lists as grids—index [row][col]. Update, identify, print like directory ops.
# Why? Builds shape awareness—prevents "why out of bounds?" idiocy.
# >>> building = [['Apt1', 'Alice'], ['Apt2', 'Bob'], ['Apt3', 'Empty']]  # Simple directory
# >>> building[1][1] = 'Charlie'  # Update Apartment Name in Building Directory
# >>> building
# [['Apt1', 'Alice'], ['Apt2', 'Charlie'], ['Apt3', 'Empty']]
# >>> unoccupied = [apt[0] for apt in building if apt[1] == 'Empty']  # Unoccupied Apartment Identifier
# >>> unoccupied
# ['Apt3']
# >>> first_floor = building[0]  # Assume rows as floors
# >>> print(first_floor[0])  # Print Apartment Codes on the First Floor
# Apt1
# >>> building.append(['Apt4', 'Dave'])  # Expand the Digital Apartment Building
# >>> building
# [['Apt1', 'Alice'], ['Apt2', 'Charlie'], ['Apt3', 'Empty'], ['Apt4', 'Dave']]
# >>> for apt in building: print(f"{apt[0]}: {apt[1]}")  # Apartment Building Management—full print
# Apt1: Alice
# Apt2: Charlie
# Apt3: Empty
# Apt4: Dave

# 2. Columnar ZigZag and Reverse Traversal (Unit 2 Shenanigans)
# Traverse columns, reverse, zigzag—like scanning bookshelves without dropping books.
# Why? Teaches non-linear traversal—useful for matrices in games/ML without full loops.
# >>> bookshelf = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matrix as shelves
# >>> reversed_books = [row[::-1] for row in bookshelf]  # Reverse the Bookshelf Traversal Pattern
# >>> reversed_books
# [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
# >>> for i in range(len(bookshelf)):  # Repairing/Adding Direction Switch
# ...     if i % 2 == 0:
# ...         print(bookshelf[i])  # Left to right
# ...     else:
# ...         print(bookshelf[i][::-1])  # Right to left—zigzag
# ...
# [1, 2, 3]
# [6, 5, 4]
# [7, 8, 9]
# >>> columns = list(zip(*bookshelf))  # Vertical Library Traverse—columns
# >>> for col in columns: print(col)
# (1, 4, 7)
# (2, 5, 8)
# (3, 6, 9)
# >>> zig = []  # Zigzag Bookshelf Traversal—full collect
# >>> for i, row in enumerate(bookshelf):
# ...     zig.extend(row if i % 2 == 0 else row[::-1])
# ...
# >>> zig
# [1, 2, 3, 6, 5, 4, 7, 8, 9]

# 3. Transposing Matrices (Unit 3 Transpose Hell)
# Flip rows/columns—like rearranging seats without chaos.
# Why? Data reshaping intuition—Pandas pivot/transpose builds on this.
# >>> seating = [[1, 2, 3], [4, 5, 6]]  # Restaurant seats
# >>> transpose = list(zip(*seating))  # Transpose the Restaurant Seating Arrangement
# >>> transpose
# [(1, 4), (2, 5), (3, 6)]
# >>> reverse_trans = list(zip(*seating[::-1]))  # Transpose in Reverse Order
# >>> reverse_trans
# [(4, 1), (5, 2), (6, 3)]
# >>> one_line_trans = [list(row) for row in zip(*seating)]  # One Line Transpose
# >>> one_line_trans
# [[1, 4], [2, 5], [3, 6]]
# >>> square = [[1, 2], [3, 4]]  # Reflect Over Secondary Diagonal
# >>> reflect = [[square[j][i] for j in range(len(square)-1, -1, -1)] for i in range(len(square))]
# >>> reflect
# [[4, 2], [3, 1]]  # Or proper reflect logic

# 4. Checking Adjacent Cells in 2D Arrays (Unit 4 Game Board Crap)
# Check neighbors—up/down/left/right, like board games without off-board crashes.
# Why? Graph-like traversal intuition—ML/Pandas adjacent ops.
# >>> board = [['.', 'X', '.'], ['.', '.', 'X'], ['X', '.', '.']]  # Game board
# >>> def has_horizontal_move(i, j):  # Horizontal Move Identification
# ...     if j > 0 and board[i][j-1] == 'X': return True
# ...     if j < len(board[0])-1 and board[i][j+1] == 'X': return True
# ...     return False
# ...
# >>> has_horizontal_move(0, 0)
# False
# >>> landing = [(i,j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == '.' and any(board[x][y] == 'X' for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)] if 0<=x<len(board) and 0<=y<len(board[0]))]  # Spotting Landing Area—adj to X
# >>> landing
# [(0,0), (0,2), (1,0), (1,1), (2,1)]
# >>> def strategic(i, j): return sum(1 for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)] if 0<=i+dx<len(board) and 0<=j+dy<len(board[0]) and board[i+dx][j+dy] == '.')  # Assessing Strategic Placement—empty adj
# >>> strategic(1,1)
# 3
# >>> def next_move(i, j):  # Magical Chessboard Next Move—find adj X or something
# ...     for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
# ...         x, y = i+dx, j+dy
# ...         if 0<=x<len(board) and 0<=y<len(board[0]) and board[x][y] == 'X':
# ...             return (x,y)
# ...
# >>> next_move(0,0)
# None
# >>> def count_corner_e(sub):  # Counting Corner 'E's in Submatrices—assume 'E' for empty
# ...     return sum(1 for r in [0, len(sub)-1] for c in [0, len(sub[0])-1] if sub[r][c] == 'E')
# ...
# # Example sub = board[0:2][0:2] etc.

# 5. Navigating Adjacent Cells in Grid (Unit 5 Hike Bullshit)
# Traverse adj with diagonals, elevation logic—like pathfinding without getting lost.
# Why? BFS/DFS intuition for grids—Pandas spatial crap.
# >>> grid = [[1,2,3], [4,5,6], [7,8,9]]  # Elevation grid
# >>> directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]  # Enhance with Diagonals
# >>> def neighbors(i, j):
# ...     return [(i+dx, j+dy) for dx,dy in directions if 0<=i+dx<len(grid) and 0<=j+dy<len(grid[0])]
# ...
# >>> neighbors(1,1)
# [(0,1), (2,1), (1,0), (1,2), (0,0), (0,2), (2,0), (2,2)]
# >>> def correct_explore(i, j):  # Mountain Peak Exploration Correction
# ...     visited = set()
# ...     stack = [(i,j)]
# ...     while stack:
# ...         x,y = stack.pop()
# ...         if (x,y) not in visited:
# ...             visited.add((x,y))
# ...             stack.extend(neighbors(x,y))
# ...     return visited
# ...
# >>> correct_explore(0,0)
# {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
# >>> def next_higher(i, j):  # Navigate to Next Higher Peak
# ...     curr = grid[i][j]
# ...     higher = max((grid[x][y], (x,y)) for x,y in neighbors(i,j) if grid[x][y] > curr)[1]
# ...     return higher
# ...
# >>> next_higher(0,0)  # Assume finds (2,2) or path
# (1,1)  # Example
# >>> def select_next(i, j):  # Selection Logic for Next Position
# ...     candidates = [(grid[x][y], (x,y)) for x,y in neighbors(i,j) if grid[x][y] > grid[i][j]]
# ...     if candidates:
# ...         return max(candidates)[1]
# ...     return None
# ...
# >>> select_next(0,0)
# (2,2)  # Max elevation
# >>> def ascend_mountain(start):  # Ascending the Mountain Challenge
# ...     path = [start]
# ...     curr = start
# ...     while (next := select_next(*curr)):
# ...         path.append(next)
# ...         curr = next
# ...     return path
# ...
# >>> ascend_mountain((0,0))
# [(0,0), (2,2)]  # Path to peak

# There, now traverse multi-dim without making me puke. Builds on 4.1—grids as nested, but ready for NumPy. Traverse badly now, and your code deserves a kernel oops. Hack on, or go fix Windows NT.








# Lesson 4.3: PRE-PANDAS PART 3 - HASHMAPS AND THEIR USE FOR EFFICIENT DATA ACCESS
# --------------------------------------------------------------------------------

# Hashmaps? In Python, that's dicts, you idiots—O(1) access that crushes lists
# for lookups, like a filesystem cache without seek time. This lesson drills
# into using 'em for counting, aggregating, real-world crap—like library
# catalogs without scanning every book. Why? Efficient data access is
# kernel-level; slow lookups make your code crawl like bloatware. Builds on 4.1
# dict_table—now for counting/agg. No fluff—bash, update, check like a hacker,
# or go use arrays for lookups and cry.

# Dicts as hashmaps—keys hash to buckets, fast get/set. Problems: libraries,
# inventories—update, count, agg.

# 1. Essentials of HashMaps (Unit 1 Library BS)
# Basics: Update, access, check—__setitem__, __getitem__, __contains__.
# Why? O(1) efficiency—beats 4.1 list searches.
# >>> catalog = {'Book1': 'Available', 'Book2': 'Borrowed'}  # Library Catalog
# >>> catalog['Book1'] = 'Borrowed'  # Update the Library Catalog Entry
# >>> catalog
# {'Book1': 'Borrowed', 'Book2': 'Borrowed'}
# >>> if 'Book3' not in catalog: catalog['Book3'] = 'Available'  # Library Catalog Error Correction—add missing
# >>> catalog
# {'Book1': 'Borrowed', 'Book2': 'Borrowed', 'Book3': 'Available'}
# >>> 'Book2' in catalog and catalog['Book2'] == 'Available'  # Check Book Availability
# False
# >>> catalog['Book4'] = 'New'; print(catalog['Book4'])  # Update and Access Elements
# New
# >>> catalog.update({'Book5': 'Available'})  # Updating a Library Catalog
# >>> catalog
# {'Book1': 'Borrowed', 'Book2': 'Borrowed', 'Book3': 'Available', 'Book4': 'New', 'Book5': 'Available'}

# 2. Mastering Element Counting (Unit 2 Count Crap)
# Use dict for frequencies—get/defaultdict for efficient.
# Why? Aggregates without loops recounting—fast as hash.
# >>> from collections import defaultdict
# >>> counter = defaultdict(int)
# >>> for char in 'library': counter[char] += 1  # Explore Dictionary Methods for Counting
# >>> counter
# defaultdict(<class 'int'>, {'l': 1, 'i': 1, 'b': 1, 'r': 2, 'a': 1, 'y': 1})
# >>> books = ['Book1', 'Book1', 'Book2']  # Correct the Book Counter Code
# >>> book_count = {}
# >>> for book in books:
# ...     book_count[book] = book_count.get(book, 0) + 1
# ...
# >>> book_count
# {'Book1': 2, 'Book2': 1}
# >>> library_tracker = defaultdict(int)
# >>> library_tracker['Book3'] += 3  # Update Book Counts in Library Tracker
# >>> library_tracker
# defaultdict(<class 'int'>, {'Book3': 3})
# >>> sentence = 'library sentence'  # Counting Letter Frequency
# >>> letter_count = {c: sentence.count(c) for c in set(sentence)}
# >>> letter_count
# {' ': 1, 'a': 1, 'b': 1, 'c': 1, 'e': 3, 'i': 1, 'l': 1, 'n': 2, 'r': 1, 's': 1, 't': 2, 'y': 1}
# >>> collection = ['Book1', 'Book2', 'Book1']  # Counting Book Copies
# >>> copies = defaultdict(int)
# >>> for b in collection: copies[b] += 1
# >>> copies
# defaultdict(<class 'int'>, {'Book1': 2, 'Book2': 1})

# 3. Aggregating Essentials (Unit 3 Inventory Agg)
# Dict for sums, avgs, max—reduce loops.
# Why? Efficient stats—Pandas groupby builds on this.
# >>> inventory = {'Apple': 5, 'Banana': 3, 'Cherry': 7}
# >>> avg = sum(inventory.values()) / len(inventory)  # Calculate Average Quantity
# >>> avg
# 5.0
# >>> max_qty = max(inventory.values())  # Inventory Maximum Quantity Correction
# >>> max_qty
# 7
# >>> stats = {'total': sum(inventory.values()), 'max': max(inventory.values()), 'min': min(inventory.values())}  # Add Inventory Statistics
# >>> stats
# {'total': 15, 'max': 7, 'min': 3}
# >>> {k: 'above' if v > avg else 'below' for k,v in inventory.items()}  # Stock Level Comparison to Average
# {'Apple': 'below', 'Banana': 'below', 'Cherry': 'above'}
# >>> max_item = max(inventory, key=inventory.get)  # Grocery Shop Max Count Finder
# >>> max_item
# 'Cherry'

# 4. HashMaps in Action: Real-World Problems (Unit 4 Library Action)
# Borrow logic, bugs, status, word count—applied dicts.
# Why? Solves lookups/updates fast—real efficiency.
# >>> system = {'Book1': {'stock': 2, 'borrowed': 0}}  # Update Library System Borrowing
# >>> if system['Book1']['stock'] > system['Book1']['borrowed']: system['Book1']['borrowed'] += 1
# >>> system
# {'Book1': {'stock': 2, 'borrowed': 1}}
# >>> catalog_bug = {'Book2': 'Available'}  # Spot Bug in Catalog Management—assume check key exists
# >>> if 'Book3' in catalog_bug: del catalog_bug['Book3']  # No error
# >>> inventory_status = {'Book4': 5}
# >>> inventory_status['Book4'] -= 1  # Update Inventory and Check Status
# >>> 'Low' if inventory_status['Book4'] < 3 else 'OK'
# 'OK'
# >>> text = 'add word count'  # Add Word Count Functionality
# >>> word_count = {}
# >>> for word in text.split(): word_count[word] = word_count.get(word, 0) + 1
# >>> word_count
# {'add': 1, 'word': 1, 'count': 1}
# >>> 'Book1' in catalog and catalog['Book1'] == 'Available'  # Check Availability—reuse from 1

# There, now hashmaps won't make you look like a newbie. Builds on 4.1—dicts for access, ready for Pandas internals. Use lists for lookups now, and your code deserves a panic. Hack on, or go maintain Perl.







# Lesson 4.4: PANDAS BASICS - NOW WITH STEROIDS
# --------------------------------------------------------------------------------

# Alright, you kernel-panicking script kiddies, if you survived the stone-age
# crap in 4.1 without segfaulting your brain, congrats—you're ready for Pandas.
# This isn't some bloated framework; it's Python on steroids for data
# wrangling, built on NumPy arrays that make your lists look like amateur hour.
# DataFrames? Just your dict-of-lists from 4.1, but vectorized, indexed like a
# boss, and without the loop-induced slowness that makes me want to rewrite
# your code in C. Series? Your poor man's labeled list, but with math ops that
# don't suck.

# We'll tie this back to 4.1 patterns: creating, indexing, filtering,
# aggregating. But now, Pandas does the heavy lifting—vectorized, no explicit
# loops unless you're an idiot. Forget dunders here; Pandas overloads 'em
# internally (__getitem__ for slicing, etc.), but you don't touch that unless
# you're hacking the source. Import pandas as pd, or I'll judge you.

# Why bother? Because looping over data in pure Python is for masochists.
# Pandas vectorizes ops, aligns indices automagically, and handles missing data
# without exploding. Screw this up, and your "data science" will be as reliable
# as a Windows kernel. Bash this in REPL; experiment or die bored.

# 1. Series: Labeled 1D Data (Upgrade Your Lists/Dicts)
# Like your series_like dict in 4.1, but with index alignment and vector ops.
# >>> import pandas as pd
# >>> s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])  # From list + labels, like zip(dict)
# >>> s
# a    10
# b    20
# c    30
# dtype: int64
# >>> s['b']  # Indexing like dict.__getitem__
# 20
# >>> s * 2  # Vectorized mapping, no list comp needed
# a    20
# b    40
# c    60
# dtype: int64
# >>> 'b' in s.index  # Membership, like __contains__ on keys
# True

# 2. DataFrames: 2D Tables (Your Dict-Table on Crack)
# Column-major like your dict_table: Columns as Series.
# Row-major from lists? Use from_records or whatever, but dicts are cleaner.
# >>> df = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [30, 25]})  # Dict of lists, direct from 4.1
# >>> df
#     name  age
# 0  Alice   30
# 1    Bob   25
# >>> df['age']  # Column access: Returns Series, like dict.__getitem__
# 0    30
# 1    25
# Name: age, dtype: int64
# >>> df.loc[0, 'age'] = 31  # Update cell, like list.__setitem__ but labeled
# >>> df
#     name  age
# 0  Alice   31
# 1    Bob   25

# 3. Slicing and Filtering (No More Zip Shenanigans)
# iloc for position (like list indices), loc for labels (like dict keys).
# Boolean filtering: Vectorized, beats your list comps.
# >>> df.iloc[1:3]  # Positional slice, like list.__getitem__(slice)
#     name  age
# 1    Bob   25
# >>> df.loc[df['age'] > 25]  # Filter rows, like your zip comp but efficient
#     name  age
# 0  Alice   31
# >>> df['age'] > 25  # Boolean Series, for masking
# 0     True
# 1    False
# Name: age, dtype: bool

# 4. Aggregation and Grouping (Bye, Defaultdict Loops)
# groupby like your manual grouping, but with agg funcs vectorized.
# sum, mean, etc.—no explicit sums.
# >>> df_group = pd.DataFrame({'group': ['A', 'A', 'B'], 'value': [1, 2, 3]})  # Like your data dict
# >>> df_group.groupby('group').sum()  # Group and aggregate, crushes your for-loop defaultdict
#        value
# group
# A          3
# B          3
# >>> df_group['value'].mean()  # Simple agg on Series
# 2.0

# 5. Edge Cases (Don't Be Stupid)
# Mismatched indices? Pandas aligns or NaNs 'em—better than zip truncating.
# Mixed types? It'll upcast to object, but keep columns consistent or suffer performance hell.
# Missing data: Use pd.NA or None; Pandas handles 'em gracefully, unlike your lists exploding.
# >>> s2 = pd.Series([40, 50], index=['c', 'd'])
# >>> s + s2  # Aligns on index, adds NaN where missing
# a     NaN
# b     NaN
# c    50.0
# d     NaN
# dtype: float64








# Lesson 4.5: INSPECTING DATAFRAMES - DON'T BE BLIND, YOU MORON
# --------------------------------------------------------------------------------

# Listen up, you kernel-panicking code monkeys. You've wrangled your DataFrame
# like some half-assed filesystem, but if you can't inspect the damn thing
# without staring at raw print vomit, you're as useful as a Windows driver in
# Linux. Inspecting means peeking without exploding your terminal—head/tail for
# overviews, iloc/loc for rows, at/iat for cells, and pretty-printing JSON crap
# if your data's polluted with strings. Why? Because debugging blind is for
# idiots who enjoy segfaults. Builds on 4.3 NumPy leverage—views are efficient,
# no copies unless you mutate. Tie to 4.4 loops: Inspect without them, or your
# code sucks harder than systemd bloat.

# Import pd/json, bash in REPL, experiment or go fix your distro. Print
# smart—pandas sets display options, but override if your DF's a monster.

# 1. Overview: Don't Dump the Whole Mess
# print(df) spews everything—fine for toys, crap for big data. Use head/tail/sample instead.
# >>> import pandas as pd
# >>> df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'], 'age': [30, 25, 35], 'data': ['{"key": "value"}', '{"foo": "bar"}', '{"baz": 42}']})
# >>> df  # Or print(df)—full view, but truncates wide/tall DFs
#       name  age             data
# 0    Alice   30  {"key": "value"}
# 1      Bob   25    {"foo": "bar"}
# 2  Charlie   35      {"baz": 42}
# >>> df.head(2)  # First n rows—like tail -n but top
#     name  age             data
# 0  Alice   30  {"key": "value"}
# 1    Bob   25    {"foo": "bar"}
# >>> df.tail(1)  # Last n—debug appends
#       name  age         data
# 2  Charlie   35  {"baz": 42}
# >>> df.sample(2)  # Random rows—spot check without bias
#     name  age             data
# 1    Bob   25    {"foo": "bar"}
# 0  Alice   30  {"key": "value"}  # Random, yours may differ

# 2. Specific Rows: Slice Without the Bloat
# iloc for position (like NumPy slices), loc for labels—returns Series or DF.
# >>> df.iloc[1]  # Row by index—Series view, efficient
# name              Bob
# age                25
# data    {"foo": "bar"}
# Name: 1, dtype: object
# >>> df.iloc[1:3]  # Slice rows—DF subset
#       name  age         data
# 1      Bob   25  {"foo": "bar"}
# 2  Charlie   35    {"baz": 42}
# >>> df.loc[0:1]  # Label slice—inclusive end
#     name  age             data
# 0  Alice   30  {"key": "value"}
# 1    Bob   25    {"foo": "bar"}
# >>> print(df.loc[2].to_string())  # Neat print row—string format
# name    Charlie
# age          35
# data    {"baz": 42}

# 3. Specific Cells: Poke Without Looping
# at/iat for scalar access—faster than [] for singles.
# >>> df.at[0, 'name']  # Label access—scalar
# 'Alice'
# >>> df.iat[2, 2]  # Position—faster for raw
# '{"baz": 42}'
# >>> df['age'][1]  # Column then index—works, but at/iat cleaner for cells

# 4. Pretty-Print JSON in Cells: Don't Stare at String Vomit
# If cell's JSON string, parse and dump indented—like debugging a config without pain.
# >>> import json
# >>> cell = df.at[0, 'data']  # Grab cell
# >>> print(json.dumps(json.loads(cell), indent=4))  # Parse, pretty-print
# {
#     "key": "value"
# }
# >>> for idx, row in df.iterrows():  # If batch (avoid if possible)
# ...     if isinstance(row['data'], str):
# ...         try:
# ...             pretty = json.dumps(json.loads(row['data']), indent=4)
# ...             print(f"Row {idx}: {pretty}")
# ...         except json.JSONDecodeError:
# ...             print(f"Row {idx}: Invalid JSON crap")
# ...
# Row 0: {
#     "key": "value"
# }
# Row 1: {
#     "foo": "bar"
# }
# Row 2: {
#     "baz": 42
# }
# >>> df['pretty_data'] = df['data'].apply(lambda x: json.dumps(json.loads(x), indent=4) if isinstance(x, str) else x)  # Vectorized column add
# >>> print(df['pretty_data'][2])  # Inspect new column
# {
#     "baz": 42
# }

# 5. Meta Inspection: Know Your DF's Guts
# info/describe for structure/stats—beats manual counts.
# >>> df.info()  # Dtypes, memory, non-null—like ls -l on columns
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 3 entries, 0 to 2
# Data columns (total 4 columns):
#  #   Column       Non-Null Count  Dtype
# ---  ------       --------------  -----
#  0   name         3 non-null      object
#  1   age          3 non-null      int64
#  2   data         3 non-null      object
#  3   pretty_data  3 non-null      object
# dtypes: int64(1), object(3)
# memory usage: 224.0+ bytes
# >>> df.describe()  # Stats on numerics—like your aggs
#             age
# count   3.000000
# mean   30.000000
# std     5.000000
# min    25.000000
# 25%    27.500000
# 50%    30.000000
# 75%    32.500000
# max    35.000000
# >>> df.shape  # Rows, cols—like len on multi-dim
# (3, 4)
# >>> df['age'].unique()  # Uniques—like set on column
# array([30, 25, 35])
# >>> df['name'].value_counts()  # Counts—spot duplicates
# name
# Alice      1
# Bob        1
# Charlie    1
# Name: count, dtype: int64








# Lesson 4.6: PANDAS ADVANCED - STOP BEING A DATA TOURIST
# --------------------------------------------------------------------------------

# You think you're hot shit now with basic Pandas from 4.2? Wake up, you
# kernel-wannabes—this is where the rubber meets the road. Building on your
# stone-age wrangling in 4.1 and the steroid injection in 4.2, we're diving
# into advanced crap that turns your DataFrames from toys into weapons. Merging
# like zip on crack, reshaping without transpose hacks, deep groupby without
# defaultdict loops, applying funcs vectorized, and wrestling missing data
# without your code imploding. Why? Because real data is messy, unaligned
# garbage, and if you don't master this, your "analysis" will be as stable as a
# Windows NT kernel.

# Tie back: These ops extend your 4.1 patterns—zip becomes merge, comps become
# apply, grouping gets smarter. Pandas handles it efficiently, but grok the
# intuition or you'll write slow, unmaintainable bloat. No dunders to poke;
# Pandas abstracts 'em. Import pd, bash in REPL, experiment like a real hacker
# or go back to Fortran.

# 1. Merging/Joining: Align Data Like Zip, But Smarter
# Like zipping columns in 4.1, but for whole DFs with keys, handling mismatches without truncating like a moron.
# >>> import pandas as pd
# >>> df1 = pd.DataFrame({'key': ['a', 'b', 'c'], 'value1': [1, 2, 3]})
# >>> df2 = pd.DataFrame({'key': ['b', 'c', 'd'], 'value2': [4, 5, 6]})
# >>> pd.merge(df1, df2, on='key')  # Inner join, like zip on matching keys
#   key  value1  value2
# 0   b       2       4
# 1   c       3       5
# >>> pd.merge(df1, df2, on='key', how='left')  # Left join: Keep all from left (df1), match right where possible, NaN else
#   key  value1  value2
# 0   a       1     NaN
# 1   b       2     4.0
# 2   c       3     5.0
# >>> pd.merge(df1, df2, on='key', how='outer')  # Outer, fills NaN like padded zip_longest
#   key  value1  value2
# 0   a     1.0     NaN
# 1   b     2.0     4.0
# 2   c     3.0     5.0
# 3   d     NaN     6.0

# 2. Reshaping: Pivot/Melt Like Transposing, Without the Pain
# Pivot: Spread long data wide, like turning rows to columns. Melt: Opposite, for stacking.
# Beats your zip(*table) transpose hacks—handles indices properly.
# >>> df_long = pd.DataFrame({'date': ['2023-01', '2023-01', '2023-02'], 'item': ['A', 'B', 'A'], 'value': [10, 20, 30]})
# >>> df_long.pivot(index='date', columns='item', values='value')  # Wide format
# item      A     B
# date
# 2023-01  10    20
# 2023-02  30   NaN
# >>> df_wide = pd.DataFrame({'date': ['2023-01', '2023-02'], 'A': [10, 30], 'B': [20, None]})
# >>> pd.melt(df_wide, id_vars='date', value_vars=['A', 'B'])  # Back to long
#      date variable  value
# 0  2023-01        A   10.0
# 1  2023-02        A   30.0
# 2  2023-01        B   20.0
# 3  2023-02        B    NaN

# 3. Groupby In Depth: Aggregate Like Your Defaultdict, But Vectorized
# Multi-agg, custom funcs—crushes your manual loops.
# >>> df_group = pd.DataFrame({'group': ['A', 'A', 'B'], 'value': [1, 2, 3]})
# >>> df_group.groupby('group').agg({'value': ['sum', 'mean']})  # Multiple aggs
#        value
#          sum  mean
# group
# A          3   1.5
# B          3   3.0
# >>> df_group.groupby('group').apply(lambda g: g['value'].sum() * 2)  # Custom, like comp on grouped.items()
# group
# A    6
# B    6
# dtype: int64

# 4. Applying Functions: Vectorized Mapping, Beyond Simple Ops
# Apply to Series/DF, axis for rows/columns—like your list comps but efficient.
# >>> df = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [30, 25]})
# >>> df['age'].apply(lambda x: x * 2)  # Series apply, like [val*2 for val in data]
# 0    60
# 1    50
# Name: age, dtype: int64
# >>> df.apply(lambda row: f"{row['name']} is {row['age']}", axis=1)  # Row-wise, like your enumerate(zip)
# 0    Alice is 30
# 1      Bob is 25
# dtype: object

# 5. Handling Missing Data: NaNs Without Your Code Barfing
# Fill, drop, interpolate—better than your manual checks in 4.1 edges.
# >>> df_missing = pd.DataFrame({'col1': [1, None, 3], 'col2': [4, 5, None]})
# >>> df_missing.fillna(0)  # Fill NaNs, like replacing None in lists
#    col1  col2
# 0   1.0   4.0
# 1   0.0   5.0
# 2   3.0   0.0
# >>> df_missing.dropna()  # Drop rows with NaN, like filtering non-None
#    col1  col2
# 0   1.0   4.0
# >>> df_missing['col1'].interpolate()  # Linear fill, fancy for sequences
# 0    1.0
# 1    2.0
# 2    3.0
# Name: col1, dtype: float64







# Lesson 4.7: APPENDING COLUMNAR DATA - ADD COLUMNS WITHOUT BLOATING
# --------------------------------------------------------------------------------

# Appending data to a DF? If you're tacking on rows like a bad log rotator,
# you're inviting perf hell—DFs aren't lists, they copy on grow. But adding
# columns? That's columnar magic, vectorized and efficient, like slapping a new
# Series on your dict_table from 4.1. This lesson hammers it: Add columns via
# assignment (diff example), append rows if must (but use concat), tie to NumPy
# for raw appends. Why? Real data grows; do it wrong, and your DF balloons RAM
# like a leaky allocator. Builds on 4.3 leverage—vector ops keep it fast, no
# loops.

# Import pd/np, bash in REPL, experiment or go patch Perl. Columns add
# in-place; rows often copy—pre-allocate if looping appends (but don't loop,
# idiot).

# 1. Adding Columns: Vectorized Assignment, Like Dict Setitem
# New column from ops on existing—pure NumPy under hood, aligned by index.
# >>> import pandas as pd
# >>> df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
# >>> df['diff'] = df['col1'] - df['col2']  # Add diff column—vectorized, no loop
# >>> df
#    col1  col2  diff
# 0     1     4    -3
# 1     2     5    -3
# 2     3     6    -3
# >>> df['ratio'] = df['col1'] / df['col2']  # Another—handles types, NaNs
# >>> df
#    col1  col2  diff     ratio
# 0     1     4    -3  0.250000
# 1     2     5    -3  0.400000
# 2     3     6    -3  0.500000

# 2. From Functions/NumPy: Apply or Direct
# Custom column? Vectorized apply or NumPy ufunc—beats 4.1 comps.
# >>> import numpy as np
# >>> df['sqrt_col1'] = np.sqrt(df['col1'])  # Ufunc direct—fast, preserves index
# >>> df
#    col1  col2  diff     ratio  sqrt_col1
# 0     1     4    -3  0.250000   1.000000
# 1     2     5    -3  0.400000   1.414214
# 2     3     6    -3  0.500000   1.732051
# >>> df['category'] = df['diff'].apply(lambda x: 'neg' if x < 0 else 'pos')  # Apply for custom
# >>> df
#    col1  col2  diff     ratio  sqrt_col1 category
# 0     1     4    -3  0.250000   1.000000      neg
# 1     2     5    -3  0.400000   1.414214      neg
# 2     3     6    -3  0.500000   1.732051      neg

# 3. Appending Rows: Concat or Loc, But Avoid Loops
# Rows append copies DF—inefficient for loops (use list then pd.DataFrame).
# Like adding to 4.1 lists, but Pandas aligns columns.
# >>> new_row = pd.DataFrame({'col1': [4], 'col2': [7]})
# >>> df = pd.concat([df, new_row], ignore_index=True)  # Append row DF—resets index
# >>> df
#    col1  col2  diff     ratio  sqrt_col1 category
# 0     1     4  -3.0  0.250000   1.000000      neg
# 1     2     5  -3.0  0.400000   1.414214      neg
# 2     3     6  -3.0  0.500000   1.732051      neg
# 3     4     7   NaN       NaN        NaN      NaN
# >>> df.loc[len(df)] = [5, 8, -3, 0.625, np.sqrt(5), 'neg']  # Append list to loc—matches columns
# >>> df
#    col1  col2  diff     ratio  sqrt_col1 category
# 0     1     4  -3.0  0.250000   1.000000      neg
# 1     2     5  -3.0  0.400000   1.414214      neg
# 2     3     6  -3.0  0.500000   1.732051      neg
# 3     4     7   NaN       NaN        NaN      NaN
# 4     5     8  -3.0  0.625000   2.236068      neg

# 4. Bulk Appends: From NumPy or Lists
# Leverage 4.3: Add columns from arrays—fast assign.
# >>> new_data = np.array([10, 20, 30, 40, 50])
# >>> df['new_col'] = new_data  # Array to column—must match length
# >>> df
# ...  # new_col added
# # Row bulk: Collect in list, then concat once—beats loop appends
# >>> rows = [{'col1': i, 'col2': i*2} for i in range(3)]  # Like 4.1 comp
# >>> new_df = pd.DataFrame(rows)
# >>> df = pd.concat([df, new_df], ignore_index=True)

# 5. Gotchas: Inefficiency and Alignment
# Appending rows in loop? Copies each time—OOM on large. Pre-allocate or list-build.
# Column add mismatches length? Error—align or fill NaN.
# Mixed dtypes? Falls to object—slow, like 4.3 warnings.
# >>> df['short_col'] = [1, 2]  # Length mismatch? Boom—ValueError







# Lesson 4.8: LOOPING OVER ROWS AND COLUMNS - DON'T, UNLESS YOU'RE AN IDIOT
# --------------------------------------------------------------------------------

# Listen up, you kernel-wannabe script kiddies. If you're looping over a
# DataFrame like some amateur patching a filesystem with duct tape, you're
# doing it wrong—Pandas is built for vectorized ops that crush loops in speed
# and sanity. Why the hell would you loop? Maybe for custom crap that defies
# vectorization, or because you're too lazy to think Pythonic. But 99% of the
# time, it's a sign your code sucks and will kernel-panic on big data. This
# lesson beats the intuition into you: rows as Series/tuples (extending 4.1's
# zips/enumerates), columns as Series (like your dict_table accesses). Tie to
# 4.3: Use .to_numpy() for raw loops if you must, but vectorize or GTFO. Builds
# on NumPy engine—loops negate the point, like running a distro without
# optimizations.

# Import pd, bash in REPL, experiment or go optimize BASIC. Looping methods add
# overhead; avoid like bad drivers.

# 1. Why Loop? (Spoiler: You Shouldn't)
# Vectorize with ops/apply—loops are slow Python, NumPy under Pandas flies in C.
# >>> import pandas as pd
# >>> df = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [30, 25], 'score': [85, 90]})
# >>> df['age'] + 1  # Vectorized—no loop needed
# 0    31
# 1    26
# Name: age, dtype: int64

# 2. Looping Over Columns: Grab Series Like Dict Keys
# Columns are Series—iterate names or access directly. Like 4.1 dict_table keys.
# >>> for col in df.columns:  # Column names, like dict.keys()
# ...     print(col)
# ...
# name
# age
# score
# >>> for col in df:  # Same as above, lazy alias
# ...     print(df[col].mean())  # Access Series, compute—still, vectorize aggregates!
# ...
# nan  # name is str
# 27.5
# 87.5
# >>> df['age'].values  # Raw NumPy for column loop—faster if must iterate values
# array([30, 25])

# 3. Looping Over Rows: Series or Tuples, But Why?
# iterrows(): Yields index, Series—overhead city.
# itertuples(): Faster, namedtuples—less crap.
# Like 4.1 enumerate(zip)—but Pandas aligns.
# >>> for idx, row in df.iterrows():  # Index and Series—slow, creates new Series each time
# ...     print(f"Row {idx}: {row['name']} is {row['age']}")
# ...
# Row 0: Alice is 30
# Row 1: Bob is 25
# >>> for row in df.itertuples():  # Namedtuple—faster, access row.name, row.age
# ...     print(f"{row.name} scored {row.score}")
# ...
# Alice scored 85
# Bob scored 90
# >>> raw = df.to_numpy()  # From 4.3: Raw array for "easier" loops—views, contiguous
# >>> for row in raw:  # Loop rows: array slices, no overhead—still dumb vs vector
# ...     print(row[0], row[1])  # Access by position
# ...
# Alice 30
# Bob 25

# 4. When Loops "Make Sense": Custom Non-Vectorizable Crap
# E.g., row-wise strings—but try apply first.
# >>> df.apply(lambda row: f"{row['name']} ({row['age']})", axis=1)  # Vectorized row op—no explicit loop
# 0    Alice (30)
# 1      Bob (25)
# dtype: object
# # Forced loop example (bad):
# >>> for idx, row in df.iterrows():
# ...     df.loc[idx, 'info'] = f"{row['name']} info"  # Mutate in loop—slow as hell on large DF
# ...
# >>> df
#     name  age  score         info
# 0  Alice   30     85  Alice info
# 1    Bob   25     90    Bob info

# 5. Gotchas: Perf Hell and Mutations
# Loops create temp objects—scale sucks. Mutate in loop? Use loc/iloc, but vector assign better.
# Raw NumPy loops "easier" for speed (no Series), but lose labels—reconstruct if needed.
# >>> %timeit for _, row in df.iterrows(): pass  # Time it—slow
# 123 µs ± 4.56 µs per loop
# >>> raw = df.to_numpy()
# >>> %timeit for row in raw: pass  # Faster loop, but still avoid
# 12.3 µs ± 0.45 µs per loop








# Lesson 4.9: NUMPY DEEP DIVE - THE ARRAY ENGINE UNDER PANDAS
# --------------------------------------------------------------------------------

# What the hell is Pandas without NumPy? It's built on these arrays, you
# idiots—faster than your lists, vectorized like a GPU kernel, and the backbone
# for all your DF ops. This lesson rips the hood off: arrays as multi-dim
# sequences (extending 4.1's lists-of-lists), broadcasting like smart zipping,
# and ufuncs that vectorize without your crappy comps. Why? If you don't grok
# NumPy, your Pandas code will be slow garbage, leaking perf like a bad memory
# allocator. Tie to 4.1: DFs are just labeled NumPy under the hood—your
# pure-Python intuition gets supercharged here.

# NumPy arrays crush native lists: Contiguous memory, fixed dtypes, no object
# overhead—math ops fly in compiled C, not slow Python loops. Broadcasting
# auto-aligns shapes, ufuncs do element-wise magic. Screw this up, and your
# "data wrangling" will kernel-panic on real datasets.

# Import np, bash in REPL, experiment or go back to Perl. No dunders to poke
# directly; NumPy overloads 'em (__add__ for + , etc.).

# 1. Creating Arrays: From Your Crappy Lists/Dicts
# Like series_like or table in 4.1, but n-dim and efficient.
# >>> import numpy as np
# >>> arr = np.array([10, 20, 30])  # 1D from list, like data in 4.1
# >>> arr
# array([10, 20, 30])
# >>> mat = np.array([['Alice', 30], ['Bob', 25]])  # 2D mixed? Falls to object dtype—slow, keep homogeneous!
# >>> mat
# array([['Alice', 30],
#        ['Bob', 25]], dtype=object)
# >>> np.zeros((2, 3))  # Zero array, shape like your multi-dim
# array([[0., 0., 0.],
#        [0., 0., 0.]])
# >>> np.arange(10)  # Like range, but array—better than lists for sequences
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# 2. Indexing/Slicing: Fancy Stuff Beats Your __getitem__
# Position-based like iloc intuition from 4.1, but with bool masks and multi-dim.
# >>> arr[1]  # Single index
# 20
# >>> mat[:, 1]  # Column slice, like zip(*table)[1] but efficient
# array([30, 25], dtype=object)
# >>> mask = arr > 15  # Bool array, like your filter comps
# >>> mask
# array([False,  True,  True])
# >>> arr[mask]  # Filtered view— no copy unless you want
# array([20, 30])
# >>> mat[1, 0]  # Row-col access
# 'Bob'

# 3. Broadcasting: Smart Alignment, No Zip Hacks
# Auto-expands shapes for ops—beats padding in 4.1 edges.
# >>> arr + 5  # Scalar broadcasts to array shape
# array([15, 25, 35])
# >>> col = np.array([[1], [2]])  # Column vector
# >>> row = np.array([3, 4, 5])  # Row vector
# >>> col + row  # Broadcasts to 2x3 matrix—no manual loops/zips
# array([[4, 5, 6],
#        [5, 6, 7]])

# 4. Ufuncs/Math: Vectorized Ops Crush Your Comps
# Element-wise, axis aggs—like your mappings/aggregates but fast.
# >>> np.sin(arr)  # Ufunc on array—no loop needed
# array([-0.54402111,  0.99343516, -0.98803162])  # or whatever
# >>> np.sum(mat[:, 1].astype(int))  # Sum column, cast dtype first
# 55
# >>> np.mean(arr)  # Mean, like your sum/len but vectorized
# 20.0
# >>> np.dot(np.array([1, 2]), np.array([3, 4]))  # Dot product, matrix math intuition
# 11

# 5. Reshaping/Views: Manipulate Without Copies
# Like transpose in 4.1, but views save memory—no deep copies unless modified.
# >>> flat = np.arange(6)
# >>> matrix = flat.reshape(2, 3)  # Reshape view
# >>> matrix
# array([[0, 1, 2],
#        [3, 4, 5]])
# >>> matrix.T  # Transpose, like zip(*)
# array([[0, 3],
#        [1, 4],
#        [2, 5]])
# >>> np.concatenate([arr, arr])  # Concat like + on lists, but axis control
# array([10, 20, 30, 10, 20, 30])

# Edge Cases: Dtype mismatches? Upcasts or errors—keep homogeneous. Views modify originals—copy if needed. Big arrays? Watch RAM, or your machine kernels.
# >>> arr_copy = arr.copy()  # Explicit copy
# >>> arr_copy[0] = 99
# >>> arr  # Original unchanged
# array([10, 20, 30])

# There, now you get why NumPy is the unsung hero—your 4.1 patterns on steroids, prepping for Pandas DFs not sucking. Loop over arrays manually now, and I'll disown you like a bad driver patch. Hack on, or go optimize BASIC code.







# Lesson 4.10: LEVERAGING NUMPY ON PANDAS - DON'T WASTE THE DAMN ENGINE
# --------------------------------------------------------------------------------

# You idiots finally grokked NumPy in 4.2 as the turbocharged array beast under
# Pandas? Good, because Pandas isn't reinventing the wheel—it's slapping labels
# and fancy methods on NumPy arrays like a smart wrapper that doesn't suck.
# Series? Just a 1D NumPy array with an index. DataFrames? Dict of aligned
# Series, all riding NumPy for storage and ops. Why leverage this? Because
# ignoring it means you're writing slow, loop-riddled crap when you could
# vectorize everything and let the C backend fly. This lesson shows practical
# ways to exploit this: access raw arrays for NumPy magic, mix ufuncs without
# breaking a sweat, optimize perf without reinventing kernels, and interop like
# a boss. Build on 4.1's intuition and 4.2's arrays—your pure-Python patterns
# get a steroid boost here. Screw it up, and your "data code" will crawl like a
# bad filesystem on spinning rust.

# And yeah, about .to_numpy() making it "easier" to loop over rows/columns?
# Listen, if you're looping over a DF, you're already doing it wrong—like
# patching a kernel with bubblegum. Pandas is built for vectorized ops, not
# your idiotic for-loops that make me want to nuke the whole thing. But if you
# insist on being a masochist, .to_numpy() spits out a raw 2D NumPy array,
# which is contiguous in memory and typed, so Python loops over it might be
# marginally faster than iterating DF rows (which are Series objects, with
# overhead). For rows: array[i] gives a row slice (view, efficient). For
# columns: array[:, j] slices a column. Still, it's dumb—use Pandas'
# itertuples() or iterrows() if you must loop, but really, vectorize or GTFO.
# NumPy lets you do fancy indexing/masks without loops anyway. Don't make me
# regret explaining this.

# Import pd and np, bash in REPL, experiment or go back to writing COBOL.
# Pandas delegates to NumPy for math (__array_ufunc__ hooks, etc.), so most
# NumPy funcs "just work" on Pandas objects—vectorized, aligned, no manual
# zips.

# 1. Accessing Raw NumPy Arrays: Peel the Labels, Get the Speed
# .values or .to_numpy() gives you the underlying array—manipulate with NumPy, no Pandas overhead for raw compute.
# >>> import pandas as pd
# >>> import numpy as np
# >>> s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])  # From 4.2 basics
# >>> s.values  # Raw NumPy array, like your data list but typed
# array([10, 20, 30])
# >>> type(s.values)
# <class 'numpy.ndarray'>
# >>> df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
# >>> df.to_numpy()  # 2D array, like your table but contiguous
# array([[1, 4],
#        [2, 5],
#        [3, 6]])
# >>> raw = df.to_numpy()
# >>> raw[:, 1] *= 2  # Mutate raw column—reflects in DF if not copied!
# >>> df  # col2 doubled, because views where possible
#    col1  col2
# 0     1     8
# 1     2    10
# 2     3    12
# # Looping example (don't do this, but...):
# >>> for row in raw:  # Easier? Marginally—raw rows are arrays, no Series conversion
# ...     print(row)
# ...
# [1 8]
# [ 2 10]
# [ 3 12]
# >>> for j in range(raw.shape[1]):  # Columns: Slice views, fast access
# ...     print(raw[:, j])
# ...
# [1 2 3]
# [ 8 10 12]

# 2. Vectorized Ops with Ufuncs: NumPy Magic on Pandas Objects
# Pandas passes ufuncs to NumPy—element-wise, aligned by index, beats your 4.1 comps.
# >>> np.sin(s)  # Ufunc on Series—returns Series, labels preserved
# a   -0.544021
# b    0.993435
# c   -0.988032
# dtype: float64  # or similar
# >>> np.add(df['col1'], df['col2'])  # Add columns, like zip + but vectorized
# 0     5
# 1     7
# 2     9
# dtype: int64
# >>> np.mean(df, axis=0)  # Agg per column, like your sums but axis-aware
# col1    2.0
# col2    5.0
# dtype: float64
# >>> mask = df > 2  # Bool DF, like your filters—NumPy under hood
# >>> mask
#     col1   col2
# 0  False   True
# 1  False   True
# 2   True   True

# 3. Broadcasting in Action: Align Without Pain
# NumPy's broadcasting works on Pandas—scalars/vectors expand, indices align automagically.
# >>> s + 5  # Scalar broadcasts, like your 4.2 example but labeled
# a    15
# b    25
# c    35
# dtype: int64
# >>> df + np.array([10, 20])  # Row broadcast—adds to columns
#    col1  col2
# 0    11    24
# 1    12    25
# 2    13    26
# >>> s2 = pd.Series([1, 2, 3], index=['b', 'c', 'd'])
# >>> s + s2  # Index alignment with NaN—better than 4.1 zip truncate
# a     NaN
# b    21.0
# c    23.0
# d     NaN
# dtype: float64

# 4. Performance Optimization: Avoid Loops, Let NumPy Rip
# Use .apply with NumPy funcs if needed, but prefer native—loops are for losers.
# >>> large_df = pd.DataFrame(np.random.rand(1000, 1000))  # Big DF on NumPy
# >>> large_df.apply(np.sum, axis=0)  # Row-wise sum via apply—still vectorized under
# 0      501.23  # or whatever
# ...    ...
# dtype: float64
# >>> np.sum(large_df.to_numpy(), axis=0)  # Raw NumPy faster for pure compute
# array([501.23, ...])  # Same result, less overhead
# >>> %timeit large_df + 1  # Time it—Pandas/NumPy crushes Python loops
# 1.23 ms ± 45.6 µs per loop  # Fast as hell
# # Compare to pure Python loop on list-of-lists: Orders slower, you idiot

# 5. Interop and Gotchas: Mix Without Exploding
# Pass Pandas to NumPy funcs, but watch dtypes/index loss. Mutate views carefully—copies if safe.
# >>> np.corrcoef(df.to_numpy(), rowvar=False)  # Corr matrix on DF array
# array([[1., 1.],
#        [1., 1.]])  # Perfect corr in this toy
# >>> mixed = pd.Series([1, 'two', 3])  # Mixed types? Pandas object dtype—NumPy falls back, slow!
# >>> mixed.values
# array([1, 'two', 3], dtype=object)
# # Gotcha: Modifying view modifies DF—use .copy() if safety
# >>> raw = df['col1'].values
# >>> raw[0] = 99
# >>> df['col1'][0]  # Changed!
# 99




























"""








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
