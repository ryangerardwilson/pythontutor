# PYTUTOR

## PART I: CONVENTIONAL CORE

### 1.1. Primitives, Types and Pure Syntax

    import math


    def conventioncal_core_primitives_and_types():

        # Primitives—the basic building blocks
        nothing = None 
        is_sane = False 
        age = 55 
        pi = 3.14159 
        z = 3 + 4j 
        name = "Linus"
        
        # Now other types
        bugs = [42, "panic", 0.1]
        coords = (10, 20)
        prefs = {"os": "Linux"}
        idiots = {"user1", "user2"}
        r = range(5)

        # Modules
        m = math
        # And the meta twist: type of type
        x = type
        
        print("Dump all:")
        for var, val in sorted(locals().items()):
            if not var.startswith('__'):
                print(f"{var}: {val} ({type(val).__name__})")


    def extended_primitives_and_types():
        
        hell = frozenset(["debug", "monday"])

        # Binary types
        b = b'hello'
        ba = bytearray(b'hello')
        mv = memoryview(ba)
        
        # Functions and classes
        def foo(): pass
        func = foo
        
        class Dog:
            def __init__(self, name): self.name = name
            def bark(self): print(f"{self.name} woofs!")
        
        dog = Dog("Fido")
        
      
    import math as m                 # import, as
    import asyncio
    from sys import version          # from ... import


    def pure_syntax():
        
        async def demo(x: int = 5):      # async, def, :, =, pass
            pass
        
        class Dummy:                     # class
            def method(self): return 42  # return
        
        try: 4 + 5                       # try
        except Exception as e: print(e)  # except, as
        finally: print(7)                # finally
        
        i, x = 5, 10                     # , and =
        for i in range(x):               # for, in
            if x > 0 and x != 0:
                continue                 # continue
            elif x <= 0:
                raise ValueError("Oops") # raise
            else: break                  # break
        
        while i < 3 or i == 2: i += 1    # while, <, or, ==
        
        with open('temp.txt','w') as f:  # with, as
            f.write(str(i))
        
        assert x is not None             # assert, is not
        f = lambda y: y+1                # lambda
        print(f"X: {x}")                 # f-string, {}
        
        del x                            # del
        
        g_var = 10
        def outer():
            global g_var; g_var += 1     # global
            nl = 5
            def inner():
                nonlocal nl; nl += 1     # nonlocal
                yield g_var              # yield
            return inner
        print(next(outer()()))
        
        def decorator(fn):
            return lambda *a,**k: fn(*a,**k)    # lambda
        @decorator                              # @ before the decorator
        def some_coroutine(): return "done"
        
        async def runner():
            await demo()                # await
            await asyncio.sleep(0)
            print("await")
        asyncio.run(runner())

    if __name__ == "__main__":
        conventional_core_primitives_and_types()
        extended_primitives_and_types()
        pure_syntax()


### 1.3. Built-in Introspection Tools

    import math

    def main():
        
        # type(obj): Tells you the class (type) of the object. Quick and dirty.
        print(type(math))  # <class 'module'>
        
        # dir(obj): Lists attributes and methods—no details, just names.
        print(dir(math))  # ['__doc__', ... 'ulp']  # truncated for brevity
        
        # help(obj): Dumps docstrings and usage; paginates for long stuff—hit 'q' to quit.
        # help(math)  # docs; q to quit (commented out to avoid interactive mode in script)
        
        # vars(obj): Returns the __dict__ as a dict (attributes and values); fails on objects without one.
        print(vars(math))  # {'__name__': 'math', ...}
        
        # globals(): Current global namespace dict.
        print(globals())  # Current globals
        
        # locals(): Current local namespace dict (same as globals() at top-level).
        print(locals())  # Current locals
        
        # id(obj): Unique integer ID (memory address in CPython); check for aliases.
        print(id(math))  # 140000000000001  # varies

    if __name__ == "__main__":
        main()

### 1.4 Loops

    def conventional_core_loops():

        # Basic while: Double 1-3
        num = 1
        while num <= 3:  # Loops as long as truthy.
            print(num * 2)
            num += 1  # Update or die trying.
        
        # Basic String Iteration: Char-by-Char Grind
        for char in "abc": print(char)

    def extension_loops():
        
        # Generators: Low-Mem Yields for the Memory-Stingy
        def doubled(n):
            num = 1
            while num <= n:
                yield num * 2
                num +=1
        
        for i in doubled(3):
            print(i)
        
        # Sum volumes for a 2x2x2 cube of units.
        total_volume = 0
        for length in range(1, 3):
            for width in range(1, 3):
                for height in range(1, 3):
                    vol = length * width * height
                    print(f"{length} x {width} x {height} = {vol}")
                    total_volume += vol
        print(f"Total volume of all boxes: {total_volume} cubic units")
        
        # Same as above, but using list comprehension.
        _ = [print(f"{length} x {width} x {height} = {length * width * height}")
             for length in range(1, 3)
             for width in range(1, 3)
             for height in range(1, 3)]
        total_volume = sum(length * width * height
                           for length in range(1, 3)
                           for width in range(1, 3)
                           for height in range(1, 3))
        print(f"Total volume of all boxes: {total_volume} cubic units")

    if __name__ == "__main__":
        conventional_core_loops()
        extension_loops()

### 1.5. Decorators and Context Managers

    import time

    def main():
        
        # Decorator example: Timer wrapper
        def timer(func):
            def wrapper():
                start = time.time()
                func()
                print(time.time() - start)
            return wrapper
        
        @timer
        def slow():
            time.sleep(1)
            print("Done")
        
        slow()
        
        # Context Manager example: Timer class
        class Timer:
            def __enter__(self):
                self.start = time.time()
                return self
            def __exit__(self, *args):
                print(time.time() - self.start)
        
        with Timer():
            time.sleep(1)
            print("Slept")

    if __name__ == "__main__":
        main()


### 1.6. Function Params

    def main():
        
        # 1. In Function Definitions: Slurping Up Args Like a Kernel Buffer
        def kernel_func(required, *args, default='foo', **kwargs):
            print(f"Required: {required}")
            print(f"Args tuple: {args}")
            print(f"Default: {default}")
            print(f"Kwargs dict: {kwargs}")
        
        kernel_func(42, 'extra1', 'extra2', default='bar', surprise='boom')
        kernel_func(42, 'extra1', 'extra2', 'extra3', default='bar', surprise='boom', dudu='bubu')
        
        # 2. In Function Calls: Unpacking Like a Pro, Not a Penguin
        def idiot_func(a, b, c):
            print(a, b, c)
        
        pos_args = [1, 2, 3]
        kw_args = {'a': 4, 'b': 5, 'c': 6}
        idiot_func(*pos_args)  # 1 2 3
        idiot_func(**kw_args)  # 4 5 6

    if __name__ == "__main__":
        main()

### 1.7. Dunder Methods

    import pydoc

    def conventional_core_exploring_dunder_methods():
        
        # Create objects
        l = [1, 2, 3]
        t = (1, 2, 3)
        s = "abc"
        d = {'a': 1}
        r = range(5)
        b = b'bytes'
        
        # List attributes (dir(obj) returns all attrs/methods for obj—peek inside)
        print(dir(l))  # See __dunders__
        
        # help(l)                # List docs (commented to avoid flooding output)
        # help(str)              # String docs
        # help(dict)             # Dict docs
        
        # Specific dunder docs
        # help(list.__getitem__)  # Commented
        
        # Experiment (call dunders directly here only; use syntax in code)
        print(l.__len__())                       # len(l)
        print(l.__getitem__(1))                  # l[1]; try slice(1, None)
        print(s.__contains__('b'))               # 'b' in s
        it = l.__iter__(); print(it.__next__())
        l.__setitem__(0, 99)                     # l[0]=99; fails on tuple
        print(l)
        print(s.__add__("def"))                  # s + "def"
        print(s.__mul__(3))                      # s * 3


    def extension_implementing_dunder_methods_in_a_custom_class():
        
        # 1. Start with a bare class—boring, but baseline
        class MyClass:
            """This is my docstring, it will get printed pursuant to the
               help() method or the chained .__doc__ method"""
            pass
        obj = MyClass()
        print(dir(obj))
        # help(MyClass)  # Commented
        print(MyClass.__doc__)
        
        # 2. Add __init__ for state (redefine class)
        class MyClass:
            def __init__(self): self.d = [1, 2, 3]
        obj = MyClass()
        print(obj.d)
        
        # 3. Implement __str__ for nice printing (redefine)
        class MyClass:
            def __init__(self): self.d = [1, 2, 3]
            def __str__(self): return "Nice object with data: " + str(self.d)
        obj = MyClass()
        print(obj)
        
        # 4. Add __len__ (redefine)
        class MyClass:
            def __init__(self): self.d = [1, 2, 3]
            def __len__(self):
                return len(self.d)
        obj = MyClass()
        print(len(obj))  # Test
        
        # 5. __getitem__ for subscripting (redefine)
        class MyClass:
            def __init__(self): self.d = [1, 2, 3]
            def __getitem__(self, k):
                return self.d[k]
        obj = MyClass()
        print(obj[1])  # 2. Try slices: obj[1:], obj[0:2]
        
        # 6. __setitem__ for assignment (redefine)
        class MyClass:
            def __init__(self): self.d = [1, 2, 3]
            def __setitem__(self, k, v):
                self.d[k] = v
        obj = MyClass()
        obj[0] = 99; print(obj[0])  # Mutate and check
        
        # 7. __contains__ for 'in' (redefine)
        class MyClass:
            def __init__(self): self.d = [1, 2, 3]
            def __contains__(self, i):
                return i in self.d
        obj = MyClass()
        print(2 in obj)  # True
        
        # 8. __iter__ for looping (redefine)
        class MyClass:
            def __init__(self): self.d = [1, 2, 3]
            def __iter__(self):
                return iter(self.d)
        obj = MyClass()
        for x in obj: print(x)  # Iterates over d
        
        # 9. Context manager: __enter__ and __exit__ (redefine)
        class MyClass:
            def __init__(self): self.d = [1, 2, 3]
            def __enter__(self):
                self.backup = self.d.copy()  # Backup
                return self
            def __exit__(self, *exc):
                self.d = self.backup  # Restore
                del self.backup
                return False  # Propagate exceptions
        obj = MyClass()
        with obj as mc:
            mc[0] = 99
            print(mc[0])  # 99
        print(obj[0])  # Back to 1
        
        # 10. __call__ to make obj callable (redefine)
        class MyClass:
            def __init__(self): self.d = [1, 2, 3]
            def __call__(self, *a):
                print("Called with:", a)
        obj = MyClass()
        obj(42, "foo")  # Like a function

    if __name__ == "__main__":
        conventional_core_exploring_dunder_methods()
        extension_implementing_dunder_methods_in_a_custom_class()


### 1.8. CRUD on Sequences

    def main():
        
        # LISTS (mutable sequences)
        l = ['a', 'b', 'c', 'd', 'e']
        # read
        print(l[0])  # 'a'
        print(l[1:3])  # ['b', 'c']
        print(l[::-1])  # ['e', 'd', 'c', 'b', 'a']
        print(l[::-2])  # ['e', 'c', 'a']
        print('b' in l)  # True
        # create (append/extend, but here we're using concatenation)
        new = l + ['g']
        print(new)  # ['a', 'b', 'c', 'd', 'e', 'g']
        l += ['h']
        print(l)  # ['a', 'b', 'c', 'd', 'e', 'h']
        # update
        l[0] = 'A'
        print(l)  # ['A', 'b', 'c', 'd', 'e', 'h']
        l[1:3] = ['Y', 'Z']
        print(l)  # ['A', 'Y', 'Z', 'd', 'e', 'h']
        # delete
        del l[3]
        print(l)  # ['A', 'Y', 'Z', 'e', 'h']
        del l[1:3]
        print(l)  # ['A', 'e', 'h']
        
        # TUPLES (immutable sequences -- no in-place mods, ops create new tuples)
        t = ('a', 'b', 'c', 'd', 'e')
        # read
        print(t[0])  # 'a'
        print(t[1:3])  # ('b', 'c')
        print(t[::-1])  # ('e', 'd', 'c', 'b', 'a')
        print(t[::-2])  # ('e', 'c', 'a')
        print('b' in t)  # True
        # create
        new = t + ('g',)
        print(new)  # ('a', 'b', 'c', 'd', 'e', 'g')
        t += ('h',)
        print(t)  # ('a', 'b', 'c', 'd', 'e', 'h')
        # update -- can't, fake with slicing/concat (new tuple)
        t = ('a', 'b', 'c')  # reset
        print(t[:1] + ('y',) + t[1:])  # ('a', 'y', 'b', 'c')
        # delete -- can't in place, fake with slicing (new tuple)
        print(t[:1] + t[2:])  # ('a', 'c')
        
        # STRINGS (immutable sequences -- similar to tuples)
        s = "abcde"
        # read
        print(s[0])  # 'a'
        print(s[1:3])  # 'bc'
        print(s[::-1])  # 'edcba'
        print(s[::-2])  # 'eca'
        print('b' in s)  # True
        # create
        new = s + "g"
        print(new)  # 'abcdeg'
        s += "h"
        print(s)  # 'abcdeh'
        # update (fake it with slicing, since no __setitem__)
        s = "abc"  # reset
        print(s[:1] + 'y' + s[1:])  # 'aybc'
        # delete (new string via slicing)
        s = "abc"  # reset
        print(s[:1] + s[2:])  # 'ac'
        
        # SETS (mutable but unordered -- no indexing/slicing, so CRUD is different)
        se = {'a', 'b', 'c'}
        # read -- no indices, just membership/iteration
        print('b' in se)  # True
        # create
        se.add('g')
        print(se)  # {'a', 'b', 'c', 'g'}
        new = se | {'h'}
        print(new)  # {'a', 'b', 'c', 'g', 'h'}
        se |= {'i'}
        print(se)  # {'a', 'b', 'c', 'g', 'i'}
        # update -- no direct update since no keys/indices; remove then add
        se.remove('a')
        se.add('A')
        print(se)  # {'A', 'b', 'c', 'g', 'i'}
        # delete
        se.remove('i')
        print(se)  # {'A', 'b', 'c', 'g'}
        se.discard('z')
        print(se.pop())  # Arbitrary element

    if __name__ == "__main__":
        main()


### 1.9. CRUD on Mappings

    def main():
        
        # DICTS (mutable mappings)
        d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        # read
        print(d['a'])  # 1
        print('b' in d)  # True
        # create
        d['g'] = 7
        print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'g': 7}
        new = {**d, 'h': 8}
        print(new)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'g': 7, 'h': 8}
        d |= {'i': 9}
        print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'g': 7, 'i': 9}
        # update
        d['a'] = 10
        print(d)  # {'a': 10, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'g': 7, 'i': 9}
        # delete
        del d['i']
        print(d)  # {'a': 10, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'g': 7}
        print(d.pop('g'))  # 7
        print(d)  # {'a': 10, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

    if __name__ == "__main__":
        main()



## PART II: PANDAS

### 2.1. Pre-Pandas - Part I - Zip Like a Kernel Hacker

    def main():
        
        # Basic zip: Pairing two lists like a boss
        names = ['Alice', 'Bob', 'Charlie']
        ages = [30, 25, 35]
        zipped = zip(names, ages)
        print(list(zipped))  # [('Alice', 30), ('Bob', 25), ('Charlie', 35)]
        
        # Uneven lengths? Zip don't care, stops at the short one—no crashes, no drama
        heights = [170, 180]  # Shorter than names
        zipped_uneven = zip(names, ages, heights)
        print(list(zipped_uneven))  # [('Alice', 30, 170), ('Bob', 25, 180)]
        
        # Unzipping: To unzip, we need to type cast the thing that we zipped, as a list
        # - and then, follow it up with a * argument in zip, to unpack and reverse what
        # we had intially had zipped.
        pairs = list(zip(names, ages))
        unzipped_names, unzipped_ages = zip(*pairs)
        print(unzipped_names)  # ('Alice', 'Bob', 'Charlie')
        print(unzipped_ages)  # (30, 25, 35)
        
        # Real-world hack: Transposing a matrix without loops that crawl like molasses
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        transposed = list(zip(*matrix))
        print(transposed)  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
        
        # Without zip? You'd write this garbage loop—error-prone and slow as hell
        transposed_manual = []
        for i in range(len(matrix[0])):
            col = []
            for row in matrix:
                col.append(row[i])
            transposed_manual.append(tuple(col))
        print(transposed_manual)  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

    if __name__ == "__main__":
        main()


### 2.2. Pre-Pandas - Part II - 1D vs Multi-Dimensional Data

    def main():
        
        # 1. Mappings (like Dicts) for One-Dimensional Data
        data = [10, 20, 30]  # Values
        labels = ['a', 'b', 'c']  # Index
        labelled_data = dict(zip(labels, data))
        print(labelled_data)  # {'a': 10, 'b': 20, 'c': 30}
        
        # 2. Multi-Dimensional Data: Nested Lists vs. Dicts of Lists (DF Prototype)
        # Nested lists (row-oriented, headers first):
        col_labels = ['name', 'age']  # Column labels
        row1 = ['Alice', 30]         # Row data
        row2 = ['Bob', 25]
        table = [col_labels, row1, row2]
        print(table)  # [['name', 'age'], ['Alice', 30], ['Bob', 25]]
        
        # Dict of lists (column-oriented, via zip):
        dict_table = {label: list(values) for label, values in zip(col_labels, zip(row1, row2))}
        print(dict_table)  # {'name': ['Alice', 'Bob'], 'age': [30, 25]}

    if __name__ == "__main__":
        main()


### 2.3. Pre-Pandas Part III - Multidimensional Arrays and Their Traversal

    def main():
        
        # 1. Exploring Dimensions: Basics of Multi-Dim Arrays
        building = [['Apt1', 'Alice'], ['Apt2', 'Bob'], ['Apt3', 'Empty']]  # Simple directory
        building[1][1] = 'Charlie'  # Update Apartment Name in Building Directory
        print(building)  # [['Apt1', 'Alice'], ['Apt2', 'Charlie'], ['Apt3', 'Empty']]
        unoccupied = [apt[0] for apt in building if apt[1] == 'Empty']  # Unoccupied Apartment Identifier
        print(unoccupied)  # ['Apt3']
        first_floor = building[0]  # Assume rows as floors
        print(first_floor[0])  # Apt1
        building.append(['Apt4', 'Dave'])  # Expand the Digital Apartment Building
        print(building)  # [['Apt1', 'Alice'], ['Apt2', 'Charlie'], ['Apt3', 'Empty'], ['Apt4', 'Dave']]
        for apt in building: print(f"{apt[0]}: {apt[1]}")  # Apartment Building Management—full print
        
        # 2. Columnar ZigZag and Reverse Traversal
        bookshelf = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matrix as shelves
        reversed_books = [row[::-1] for row in bookshelf]  # Reverse the Bookshelf Traversal Pattern
        print(reversed_books)  # [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
        for i in range(len(bookshelf)):  # Repairing/Adding Direction Switch
            if i % 2 == 0:
                print(bookshelf[i])  # Left to right
            else:
                print(bookshelf[i][::-1])  # Right to left—zigzag
        zig = []
        for i, row in enumerate(bookshelf):
            zig.extend(row if i % 2 == 0 else row[::-1])
        print(zig)  # [1, 2, 3, 6, 5, 4, 7, 8, 9]
        
        # 3. Transposing Matrices
        seating = [[1, 2, 3], [4, 5, 6]]  # Restaurant seats
        transpose = list(zip(*seating))  # Transpose the Restaurant Seating Arrangement
        print(transpose)  # [(1, 4), (2, 5), (3, 6)]
        reverse_trans = list(zip(*seating[::-1]))  # Transpose in Reverse Order
        print(reverse_trans)  # [(4, 1), (5, 2), (6, 3)]
        one_line_trans = [list(row) for row in zip(*seating)]  # One Line Transpose
        print(one_line_trans)  # [[1, 4], [2, 5], [3, 6]]
        square = [[1, 2], [3, 4]]  # Reflect Over Secondary Diagonal
        reflect = [[square[j][i] for j in range(len(square)-1, -1, -1)] for i in range(len(square)-1, -1, -1)]
        print(reflect)  # [[4, 2], [3, 1]]
        
        # 4. Checking Adjacent Cells in 2D Arrays
        board = [
          ['.', 'X', '.'],
          ['.', '.', 'X'],
          ['X', '.', '.']]
        def has_horizontal_move(i, j):  # Horizontal Move Identification
            if j > 0 and board[i][j-1] == 'X': return True
            if j < len(board[0])-1 and board[i][j+1] == 'X': return True
            return False
        print(has_horizontal_move(0, 0))  # True
        landing = [(i,j)
            for i in range(len(board))
            for j in range(len(board[0]))
            if board[i][j] == '.' and any(board[x][y] == 'X'
            for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
            if 0<=x<len(board) and 0<=y<len(board[0]))
         ]
        print(landing)  # [(0, 0), (0, 2), (1, 0), (1, 1), (2, 1), (2, 2)]
        def strategic(i, j):
            return sum(1
                 for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]
                 if 0<=i+dx<len(board) and 0<=j+dy<len(board[0]) and board[i+dx][j+dy] == '.'
             )
        print(strategic(1,1))  # 2
        def next_move(i, j):  # Magical Chessboard Next Move—find adj X or something
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                x, y = i+dx, j+dy
                if 0<=x<len(board) and 0<=y<len(board[0]) and board[x][y] == 'X':
                    return (x,y)
        print(next_move(0,0))  # (0, 1)
        print(next_move(0,2))  # (1, 2)
        
        # 5. Navigating Adjacent Cells in Grid
        grid = [[1,2,3], [4,5,6], [7,8,9]]  # Elevation grid
        directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]  # Enhance with Diagonals
        def neighbors(i, j):
            return [(i+dx, j+dy) for dx,dy in directions if 0<=i+dx<len(grid) and 0<=j+dy<len(grid[0])]
        print(neighbors(1,1))  # [(0,1), (2,1), (1,0), (1,2), (0,0), (0,2), (2,0), (2,2)]
        def correct_explore(i, j):  # Mountain Peak Exploration Correction
            visited = set()
            stack = [(i,j)]
            while stack:
                x,y = stack.pop()
                if (x,y) not in visited:
                    visited.add((x,y))
                    stack.extend(neighbors(x,y))
            return visited
        print(correct_explore(0,0))  # {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
        def next_higher(i, j):  # Navigate to Next Higher Peak
            curr = grid[i][j]
            candidates = [(grid[x][y], (x,y)) for x,y in neighbors(i,j) if grid[x][y] > curr]
            if candidates:
                return max(candidates)[1]
            return None
        print(next_higher(0,0))  # Example output, may vary based on logic
        def select_next(i, j):  # Selection Logic for Next Position
            candidates = [(grid[x][y], (x,y)) for x,y in neighbors(i,j) if grid[x][y] > grid[i][j]]
            if candidates:
                return max(candidates)[1]
            return None
        print(select_next(0,0))  # (2,2)
        def ascend_mountain(start):  # Ascending the Mountain Challenge
            path = [start]
            curr = start
            while (next_pos := select_next(*curr)):
                path.append(next_pos)
                curr = next_pos
            return path
        print(ascend_mountain((0,0)))  # [(0,0), (2,2)]

    if __name__ == "__main__":
        main()


### 2.4. Pre-Pandas Part IV - Hashmaps and Their Use for Efficient Data Access

    from collections import defaultdict

    def main():
        
        # 1. Essentials of HashMaps (Unit 1 Library BS)
        catalog = {'Book1': 'Available', 'Book2': 'Borrowed'}  # Library Catalog
        catalog['Book1'] = 'Borrowed'  # Update the Library Catalog Entry
        print(catalog)  # {'Book1': 'Borrowed', 'Book2': 'Borrowed'}
        if 'Book3' not in catalog: catalog['Book3'] = 'Available'  # Library Catalog Error Correction—add missing
        print(catalog)  # {'Book1': 'Borrowed', 'Book2': 'Borrowed', 'Book3': 'Available'}
        print('Book2' in catalog and catalog['Book2'] == 'Available')  # False
        catalog['Book4'] = 'New'
        print(catalog['Book4'])  # New
        catalog.update({'Book5': 'Available'})  # Updating a Library Catalog
        print(catalog)  # {'Book1': 'Borrowed', 'Book2': 'Borrowed', 'Book3': 'Available', 'Book4': 'New', 'Book5': 'Available'}
        
        # 2. Mastering Element Counting (Unit 2 Count Crap)
        counter = defaultdict(int)
        for char in 'library': counter[char] += 1  # Explore Dictionary Methods for Counting
        print(counter)  # defaultdict(<class 'int'>, {'l': 1, 'i': 1, 'b': 1, 'r': 2, 'a': 1, 'y': 1})
        books = ['Book1', 'Book1', 'Book2']  # Correct the Book Counter Code
        book_count = {}
        for book in books:
            book_count[book] = book_count.get(book, 0) + 1
        print(book_count)  # {'Book1': 2, 'Book2': 1}
        library_tracker = defaultdict(int)
        library_tracker['Book3'] += 3  # Update Book Counts in Library Tracker
        print(library_tracker)  # defaultdict(<class 'int'>, {'Book3': 3})
        sentence = 'library sentence'  # Counting Letter Frequency
        letter_count = {c: sentence.count(c) for c in set(sentence)}
        print(letter_count)  # {' ': 1, 'a': 1, 'b': 1, 'c': 1, 'e': 3, 'i': 1, 'l': 1, 'n': 2, 'r': 1, 's': 1, 't': 2, 'y': 1}
        collection = ['Book1', 'Book2', 'Book1']  # Counting Book Copies
        copies = defaultdict(int)
        for b in collection: copies[b] += 1
        print(copies)  # defaultdict(<class 'int'>, {'Book1': 2, 'Book2': 1})
        
        # 3. Aggregating Essentials (Unit 3 Inventory Agg)
        inventory = {'Apple': 5, 'Banana': 3, 'Cherry': 7}
        avg = sum(inventory.values()) / len(inventory)  # Calculate Average Quantity
        print(avg)  # 5.0
        max_qty = max(inventory.values())  # Inventory Maximum Quantity Correction
        print(max_qty)  # 7
        stats = {'total': sum(inventory.values()), 'max': max(inventory.values()), 'min': min(inventory.values())}  # Add Inventory Statistics
        print(stats)  # {'total': 15, 'max': 7, 'min': 3}
        print({k: 'above' if v > avg else 'below' for k,v in inventory.items()})  # {'Apple': 'below', 'Banana': 'below', 'Cherry': 'above'}
        max_item = max(inventory, key=inventory.get)  # Grocery Shop Max Count Finder
        print(max_item)  # 'Cherry'
        
        # 4. HashMaps in Action: Real-World Problems (Unit 4 Library Action)
        system = {'Book1': {'stock': 2, 'borrowed': 0}}  # Update Library System Borrowing
        if system['Book1']['stock'] > system['Book1']['borrowed']: system['Book1']['borrowed'] += 1
        print(system)  # {'Book1': {'stock': 2, 'borrowed': 1}}
        catalog_bug = {'Book2': 'Available'}  # Spot Bug in Catalog Management—assume check key exists
        if 'Book3' in catalog_bug: del catalog_bug['Book3']  # No error
        inventory_status = {'Book4': 5}
        inventory_status['Book4'] -= 1  # Update Inventory and Check Status
        print('Low' if inventory_status['Book4'] < 3 else 'OK')  # 'OK'
        text = 'add word count'  # Add Word Count Functionality
        word_count = {}
        for word in text.split(): word_count[word] = word_count.get(word, 0) + 1
        print(word_count)  # {'add': 1, 'word': 1, 'count': 1}
        print('Book1' in catalog and catalog['Book1'] == 'Available')  # False

    if __name__ == "__main__":
        main()


### 2.5. Pandas Basics - Now with Steroids

    import pandas as pd

    def main():
        
        # 1. Series: Labeled 1D Data (Upgrade Your Lists/Dicts)
        s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])  # From list + labels, like zip(dict)
        print(s)
        print(s['b'])  # 20
        print(s * 2)  # Vectorized mapping, no list comp needed
        print('b' in s.index)  # True
        
        # 2. DataFrames: 2D Tables (Your Dict-Table on Crack)
        df = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [30, 25]})  # Dict of lists, direct from 4.1
        print(df)
        print(df['age'])
        df.loc[0, 'age'] = 31  # Update cell, like list.__setitem__ but labeled
        print(df)
        
        # 3. Slicing and Filtering (No More Zip Shenanigans)
        print(df.iloc[1:])  # Positional slice, like list.__getitem__(slice)
        print(df.loc[df['age'] > 25])  # Filter rows, like your zip comp but efficient
        print(df['age'] > 25)  # Boolean Series, for masking
        
        # 4. Aggregation and Grouping (Bye, Defaultdict Loops)
        df_group = pd.DataFrame({'group': ['A', 'A', 'B'], 'value': [1, 2, 3]})  # Like your data dict
        print(df_group.groupby('group').sum())  # Group and aggregate, crushes your for-loop defaultdict
        print(df_group['value'].mean())  # 2.0
        
        # 5. Edge Cases (Don't Be Stupid)
        s2 = pd.Series([40, 50], index=['c', 'd'])
        print(s + s2)  # Aligns on index, adds NaN where missing

    if __name__ == "__main__":
        main()


### 2.6. Inspecting DataFrames

    import pandas as pd
    import json

    def main():
        
        # 1. Overview: Don't Dump the Whole Mess
        df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'], 'age': [30, 25, 35], 'data': ['{"key": "value"}', '{"foo": "bar"}', '{"baz": 42}']})
        print(df)
        print(df.head(2))
        print(df.tail(1))
        print(df.sample(2))  # Random, output may vary
        
        # 2. Specific Rows: Slice Without the Bloat
        print(df.iloc[1])
        print(df.iloc[1:3])
        print(df.loc[0:1])
        print(df.loc[2].to_string())
        
        # 3. Specific Cells: Poke Without Looping
        print(df.at[0, 'name'])  # 'Alice'
        print(df.iat[2, 2])  # '{"baz": 42}'
        print(df['age'][1])  # 25
        
        # 4. Pretty-Print JSON in Cells: Don't Stare at String Vomit
        cell = df.at[0, 'data']  # Grab cell
        print(json.dumps(json.loads(cell), indent=4))
        for idx, row in df.iterrows():  # If batch (avoid if possible)
            if isinstance(row['data'], str):
                try:
                    pretty = json.dumps(json.loads(row['data']), indent=4)
                    print(f"Row {idx}: {pretty}")
                except json.JSONDecodeError:
                    print(f"Row {idx}: Invalid JSON crap")
        df['pretty_data'] = df['data'].apply(lambda x: json.dumps(json.loads(x), indent=4) if isinstance(x, str) else x)  # Vectorized column add
        print(df['pretty_data'][2])
        
        # 5. Meta Inspection: Know Your DF's Guts
        df.info()
        print(df.describe())
        print(df.shape)  # (3, 4)
        print(df['age'].unique())  # array([30, 25, 35])
        print(df['name'].value_counts())

    if __name__ == "__main__":
        main()


### 2.7. Pandas Advanced - Stop Being a Data Tourist

    import pandas as pd

    def main():
        
        # 1. Merging/Joining: Align Data Like Zip, But Smarter
        df1 = pd.DataFrame({'key': ['a', 'b', 'c'], 'value1': [1, 2, 3]})
        df2 = pd.DataFrame({'key': ['b', 'c', 'd'], 'value2': [4, 5, 6]})
        print(pd.merge(df1, df2, on='key'))  # Inner join
        print(pd.merge(df1, df2, on='key', how='left'))
        print(pd.merge(df1, df2, on='key', how='outer'))
        
        # 2. Reshaping: Pivot/Melt Like Transposing, Without the Pain
        df_long = pd.DataFrame({'date': ['2023-01', '2023-01', '2023-02'], 'item': ['A', 'B', 'A'], 'value': [10, 20, 30]})
        print(df_long.pivot(index='date', columns='item', values='value'))  # Wide format
        df_wide = pd.DataFrame({'date': ['2023-01', '2023-02'], 'A': [10, 30], 'B': [20, None]})
        print(pd.melt(df_wide, id_vars='date', value_vars=['A', 'B']))  # Back to long
        
        # 3. Groupby In Depth: Aggregate Like Your Defaultdict, But Vectorized
        df_group = pd.DataFrame({'group': ['A', 'A', 'B'], 'value': [1, 2, 3]})
        print(df_group.groupby('group').agg({'value': ['sum', 'mean']}))
        print(df_group.groupby('group').apply(lambda g: g['value'].sum() * 2))
        
        # 4. Applying Functions: Vectorized Mapping, Beyond Simple Ops
        df = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [30, 25]})
        print(df['age'].apply(lambda x: x * 2))
        print(df.apply(lambda row: f"{row['name']} is {row['age']}", axis=1))
        
        # 5. Handling Missing Data: NaNs Without Your Code Barfing
        df_missing = pd.DataFrame({'col1': [1, None, 3], 'col2': [4, 5, None]})
        print(df_missing.fillna(0))
        print(df_missing.dropna())
        print(df_missing['col1'].interpolate())

    if __name__ == "__main__":
        main()


### 2.8. Appending Columnar Data - Add Columns Without Bloating

    import pandas as pd
    import numpy as np

    def main():
        
        # 1. Adding Columns: Vectorized Assignment, Like Dict Setitem
        df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
        df['diff'] = df['col1'] - df['col2']  # Add diff column—vectorized, no loop
        print(df)
        df['ratio'] = df['col1'] / df['col2']  # Another—handles types, NaNs
        print(df)
        
        # 2. From Functions/NumPy: Apply or Direct
        df['sqrt_col1'] = np.sqrt(df['col1'])  # Ufunc direct—fast, preserves index
        print(df)
        df['category'] = df['diff'].apply(lambda x: 'neg' if x < 0 else 'pos')  # Apply for custom
        print(df)
        
        # 3. Appending Rows: Concat or Loc, But Avoid Loops
        new_row = pd.DataFrame({'col1': [4], 'col2': [7]})
        df = pd.concat([df, new_row], ignore_index=True)  # Append row DF—resets index
        print(df)
        df.loc[len(df)] = [5, 8, -3, 0.625, np.sqrt(5), 'neg']  # Append list to loc—matches columns
        print(df)
        
        # 4. Bulk Appends: From NumPy or Lists
        new_data = np.array([10, 20, 30, 40, 50])
        df['new_col'] = new_data  # Array to column—must match length
        print(df)
        rows = [{'col1': i, 'col2': i*2} for i in range(3)]  # Like 4.1 comp
        new_df = pd.DataFrame(rows)
        df = pd.concat([df, new_df], ignore_index=True)
        print(df)

    if __name__ == "__main__":
        main()


### 2.9. Looping Over Rows and Columns - Don't, Unless You're an Idiot

    import pandas as pd

    def main():
        
        # 1. Why Loop? (Spoiler: You Shouldn't)
        df = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [30, 25], 'score': [85, 90]})
        print(df['age'] + 1)  # Vectorized—no loop needed
        
        # 2. Looping Over Columns: Grab Series Like Dict Keys
        for col in df.columns:  # Column names, like dict.keys()
            print(col)
        for col in df:  # Same as above, lazy alias
            if df[col].dtype in ['int64', 'float64']:
                print(df[col].mean())  # Skip non-numeric
        
        # 3. Looping Over Rows: Series or Tuples, But Why?
        for idx, row in df.iterrows():  # Index and Series—slow
            print(f"Row {idx}: {row['name']} is {row['age']}")
        for row in df.itertuples():  # Namedtuple—faster
            print(f"{row.name} scored {row.score}")
        raw = df.to_numpy()  # From 4.3: Raw array for "easier" loops
        for row in raw:  # Loop rows: array slices
            print(row[0], row[1])  # Access by position
        
        # 4. When Loops "Make Sense": Custom Non-Vectorizable Crap
        print(df.apply(lambda row: f"{row['name']} ({row['age']})", axis=1))  # Vectorized row op
        # Forced loop example (bad):
        for idx, row in df.iterrows():
            df.loc[idx, 'info'] = f"{row['name']} info"  # Mutate in loop—slow
        print(df)
        
        # 5. Gotchas: Perf Hell and Mutations
        # %timeit examples commented out as they require IPython
        # %timeit for _, row in df.iterrows(): pass  # Slow
        # raw = df.to_numpy()
        # %timeit for row in raw: pass  # Faster, but avoid

    if __name__ == "__main__":
        main()


### 2.10. NumPy Deep Dive - The Array Engine Under Pandas

    import numpy as np

    def main():
        
        # 1. Creating Arrays: From Your Crappy Lists/Dicts
        arr = np.array([10, 20, 30])  # 1D from list
        print(arr)
        mat = np.array([['Alice', 30], ['Bob', 25]])  # 2D mixed? object dtype
        print(mat)
        print(np.zeros((2, 3)))
        print(np.arange(10))
        
        # 2. Indexing/Slicing: Fancy Stuff Beats Your __getitem__
        print(arr[1])  # 20
        print(mat[:, 1])  # array([30, 25], dtype=object)
        mask = arr > 15  # Bool array
        print(mask)
        print(arr[mask])  # array([20, 30])
        print(mat[1, 0])  # 'Bob'
        
        # 3. Broadcasting: Smart Alignment, No Zip Hacks
        print(arr + 5)
        col = np.array([[1], [2]])  # Column vector
        row = np.array([3, 4, 5])  # Row vector
        print(col + row)
        
        # 4. Ufuncs/Math: Vectorized Ops Crush Your Comps
        print(np.sin(arr))
        print(np.sum(mat[:, 1].astype(int)))  # 55
        print(np.mean(arr))  # 20.0
        print(np.dot(np.array([1, 2]), np.array([3, 4])))  # 11
        
        # 5. Reshaping/Views: Manipulate Without Copies
        flat = np.arange(6)
        matrix = flat.reshape(2, 3)  # Reshape view
        print(matrix)
        print(matrix.T)
        print(np.concatenate([arr, arr]))
        
        # Edge Cases
        arr_copy = arr.copy()  # Explicit copy
        arr_copy[0] = 99
        print(arr)  # Original unchanged

    if __name__ == "__main__":
        main()


### 2.11. Leveraging NumPy on Pandas - Don't Waste the Damn Engine

    import pandas as pd
    import numpy as np

    def main():
        
        # 1. Accessing Raw NumPy Arrays: Peel the Labels, Get the Speed
        s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
        print(s.values)
        print(type(s.values))
        df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
        print(df.to_numpy())
        raw = df.to_numpy()
        raw[:, 1] *= 2  # Mutate raw column—reflects in DF
        print(df)
        for row in raw:  # Easier? Marginally
            print(row)
        for j in range(raw.shape[1]):  # Columns: Slice views
            print(raw[:, j])
        
        # 2. Vectorized Ops with Ufuncs: NumPy Magic on Pandas Objects
        print(np.sin(s))
        print(np.add(df['col1'], df['col2']))
        print(np.mean(df, axis=0))
        mask = df > 2  # Bool DF
        print(mask)
        
        # 3. Broadcasting in Action: Align Without Pain
        print(s + 5)
        print(df + np.array([10, 20]))  # Row broadcast
        s2 = pd.Series([1, 2, 3], index=['b', 'c', 'd'])
        print(s + s2)
        
        # 4. Performance Optimization: Avoid Loops, Let NumPy Rip
        large_df = pd.DataFrame(np.random.rand(1000, 1000))  # Big DF
        print(large_df.apply(np.sum, axis=0))  # Example, truncated
        print(np.sum(large_df.to_numpy(), axis=0))  # Raw NumPy
        # %timeit large_df + 1  # Commented
        
        # 5. Interop and Gotchas: Mix Without Exploding
        print(np.corrcoef(df.to_numpy(), rowvar=False))
        mixed = pd.Series([1, 'two', 3])  # Mixed types? object dtype
        print(mixed.values)

    if __name__ == "__main__":
        main()
