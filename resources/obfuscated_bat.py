#!/usr/bin/python3

import random
import string

# This script was transcribed by @therealwlambert from the following video by John Hammond:
# https://www.youtube.com/watch?v=0RADvfJysuA
#
# In this video, John discusses how to create a script to produce an obfuscated batch file intended to execute an arbitrary executable
#
# This ties in with the results/evidence found in the investigation of Trickbot, and it's implementation of batch file obfuscation discussed here:
# https://blog.huntresslabs.com/tried-and-true-hacker-technique-dos-obfuscation-400b57cd7dd
#

goal = "start C:/WINDOWS/System32/calc.exe"
randoms = []

def get_random_mess(min_len=5, max_len=10):
  global randoms
  while True:
    rand = "".join([ random.choice(string.ascii_lowercase) for _ in range(random.randrange(min_len, max_len))])
    if rand not in randoms:
      randoms.append(rand)
      return rand

#character_set = string.printable
#bad_chars = ";<>"
#for bad in bad_chars:
#  character_set = character_set.replace(bad, "")

set_operator = get_random_mess()
space_character = get_random_mess()
equals_character = get_random_mess()

prologue = [
  f"@echo off",
  f"set {set_operator}=set",
  f"%{set_operator}% {space_character}= ",
  f"%{set_operator}%%{space_character}%{equals_character}==",
]

def create_variable(varname, value):
  return f"%{set_operator}%%{space_character}%{varname}%{equals_character}%{value}"

alphabet = {}

var_settings = []

for char in goal:
  varname = get_random_mess()
  value = char
  var_settings.append(create_variable(varname, value))
  alphabet[value] = varname

#print("\n".join(var_settings))

execute = ["".join([f"%{alphabet[char]}%" for char in goal])]

code = [] + prologue + var_settings + execute
final_code = "\n".join(code)
with open("payload.bat", "w") as handle:
  handle.write(final_code)
