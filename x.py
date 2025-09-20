import math as m                 # import, as
import asyncio
from sys import version          # from ... import

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

