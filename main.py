#!/usr/bin/env python3
import tempfile
import subprocess
import os
import shutil

script_dir = os.path.dirname(os.path.realpath(__file__))
tutorial_path = os.path.join(script_dir, "tutorial.md")

if not os.path.exists(tutorial_path):
    print(
        f"No tutorial.md in {script_dir}? What kind of half-assed setup is this? Clone properly or GTFO."
    )
    exit(1)

with open(tutorial_path, "r", encoding="utf-8") as f:
    original_content = f.read()


def main():
    # Copy to temp so you can fuck it up without mercy. Fresh each time.
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".md", encoding="utf-8", delete=False
    ) as tmp:
        tmp.write(original_content)
        temp_file = tmp.name

    print(
        f"Opening {temp_file} in your editor. Edit the code per lessons, save, then from terminal: python {temp_file}"
    )
    print(
        "Quit editor when done with a lesson, run it, see output/errors. Repeat till not an idiot."
    )

    # Assume vim, because why not? Change if you hate yourself.
    editor = ["vi", temp_file]  # Or 'nano' if vim scares you, wimp.
    try:
        subprocess.call(editor)
    except FileNotFoundError:
        print(
            "Vim not there? Install it: sudo apt install vim. This ain't for mice-clickers."
        )
        os.unlink(temp_file)
        return 1

    print(
        "Editor closed. Now run 'python {}' from terminal to test your crap.".format(
            temp_file
        )
    )
    print("When bored, delete temp or run this script again for fresh start.")

    # Don't auto-run; let user do it manually for control.
    # Cleanup? Nah, leave it so they can run easily. User deletes when done.

    return 0


if __name__ == "__main__":
    exit(main())
