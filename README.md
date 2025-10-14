# PythonTutor Advanced

This repo ain't your grandma's Python tutor—it's an opinionated gut-punch
variant cooked up to teach workflows that actually matter when you're not just
doodling "print('hello')". Basics? Straight rip from common sense, because
types are types. But then it dives into the data model, intuitive patterns, and
Pandas for data wrangling without malloc-induced aneurysms. If you're still
using Perl for scripting in 2025, GTFO and learn Python already—it's the user-
space language, you kernel poser.

## Requirements
- Python 3.x (duh, if you're on Omarchy, it's already there—pacman -S python if
  you're that incompetent.)
- Vim (because nano is for wimps who can't escape properly. On Omarchy: sudo
  pacman -S vim. This ain't VS Code territory.)

## Getting Started
1. **Clone this crap:**

    git clone https://github.com/yourusername/pythontutor.git
    cd pythontutor

2. **Run the damn thing:**

    python main.py

- It'll bitch if `tutorial.py` is missing (it shouldn't—fix your clone, idiot).
- Fires up Vim on a temp copy of the tutor. Hack away: uncomment lessons, fill
in blanks, screw up like a pro. - Quit Vim (`:q` or `ZZ`, if you don't know,
you're not ready for Python). - Your botched edits? Stay in the temp file.
Original remains untouched. - No Vim? It'll scream at you to install it, then
bail.

3. **Pro Tip:** Use a virtualenv if you're paranoid about Python (on Omarchy,
just `python -m venv env && source env/bin/activate`). But seriously, run
it—it's moron-resistant.

## What's in the Box?
- `tutorial.py`: The meat. Lessons 1.x: basic Python crap like types, loops,
  functions—stuff that keeps you from being a total poser. 2.x: Data model
wizardry. 3.x: Patterns without the bloat. 4.x: Pandas for data that doesn't
suck.
- `main.py`: The launcher. Copies `tutorial.py` to temp, spawns Vim, waits for
  you to quit, then tells you to run like an adult. No auto-execution—do the
work, build character.

## Why Bother?  Because stock Python tutorials stop at "hello world" and leave
you looping your way to valgrind therapy. This one teaches you to *code* in
Python without RSI from bad habits. Pandas? For wrangling data like a pro
without reinventing NumPy wheels. Battle-tested for scripts that don't crash on
Wednesdays. Experiment, or don't—Python doesn't give a fuck, but your
tracebacks will.

## Credits
- Original Python vibes: Guido van Rossum (bless him for making scripting less
  masochistic).
- Opinionated overhaul: Ryan Gerard Wilson (ryangerardwilson.com). If it sucks,
  blame him. If it's gold, thank me for the README.

## License MIT, or whatever—fork it, break it, just don't sue me when your code
raises exceptions.
