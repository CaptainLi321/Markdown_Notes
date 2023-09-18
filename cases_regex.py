import os
import sys
import re
import pyperclip
arg = pyperclip.paste()
argstr = ""
for i in arg:
    argstr += i
out = argstr

out = re.sub("\r", "", out)

out = re.sub("{", r"\\begin", out)
out = re.sub("}", r"\\end", out)
out = re.sub(r"\\begin", r"\\begin{cases}",  out)
out = re.sub(r"\\end", r"\\end{cases}", out)

out = re.sub(r"\n", r"\\\\\\\\\n", out)
out = re.sub(r"\\begin{cases}\\\\\\\\\n",
             r"\\begin{cases}\n", out)
out = re.sub(r"\\\\\\\\\n(.*?)\\end{cases}",
             r"\n\1\\end{cases}", out, flags=re.MULTILINE)

print(out)

pyperclip.copy(out)
