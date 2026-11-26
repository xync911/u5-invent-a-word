"""Copy entry.txt to the output directory for the make.fun entry.

The entry invents one new English word that does not exist yet
and defines it in one clear line of at most 140 characters.
Snaccident: the moment you open the fridge for one snack and
accidentally eat dinner, dessert, and tomorrow's lunch. The word
names a small daily disaster everyone has lived through.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
# The entry text is copied verbatim; the judge reads it exactly as written.
# Verify the copy is byte-identical to the source.
assert open(SRC, "rb").read() == open(OUT, "rb").read(), "output differs from entry.txt"
