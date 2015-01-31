#!/usr/bin/env python3

# class extending int but with values strictly between -128 and 127
class Byte(int):
  def __new__(cls, value, **kwargs):
    inst = super(Byte, cls).__new__(cls, (value + 128) % 256 - 128)
    return inst
  def __iadd__(self, other):
    return Byte((self + other + 128) % 256 - 128)
  def __isub__(self, other):
    return Byte((self - other + 128) % 256 - 128)
  def __abs__(self):
    return Byte(self if self > 0 else (-self + 128) % 256 - 128)

# resizable list representing memory
class Memory(list):
  def __init__(self, empty=0):
    self.empty = empty
  def __setitem__(self, key, value):
    while key >= len(self):
      self += [self.empty] * (len(self) + 1)
    super().__setitem__(key, value)
  def __getitem__(self, key):
    while key >= len(self):
      self += [self.empty] * (len(self) + 1)
    return super().__getitem__(key)
  def to_string(self, i):
    if len(self) == 0: return "[]"
    memory_string = "["
    for j in range(len(self)):
      memory_string += str(self[j]) if j != i else '\033[1m\033[92m'+str(self[j])+'\033[0m\033[0m'
      memory_string += ", " if j != len(self)-1 else "]"
    return memory_string

i, memory = 0, Memory(empty=Byte(0))

def repl(prompt='> '):
  global i
  "A prompt-read-eval-print loop."
  import sys

  print('Welcome to the "Brainfuck" language simulator.')

  for f in sys.argv[1:]:
    print('The file '+f+' is loading.')
    f = open(f, 'w')
    for line in f:
      read(line)

  while True:
    read(input(prompt))
    print(memory.to_string(i))

def read(s):
  global i, memory
  j=0
  to_print = ""
  while j!=len(s):
    memory[0]
    c=s[j]
    if c=='>':
      i += 1
      memory[i]
    elif c=='<': i -= 1
    elif c=='+': memory[i] += 1
    elif c=='-': memory[i] -= 1
    elif c=='.': to_print += chr(int(memory[i])%256)
    elif c==',':
      if to_print != "":
        print(to_print)
        to_print = ""
      memory[i] = Byte(ord(input("")))
    elif c=='[':
      if memory[i]==0:
        bracket_balance = 1
        while bracket_balance != 0:
          j += 1
          bracket_balance += 1 if s[j] == '[' else -1 if s[j] == ']' else 0
    elif c==']':
      if memory[i]!=0:
        bracket_balance = -1
        while bracket_balance != 0:
          j -= 1
          bracket_balance += 1 if s[j] == '[' else -1 if s[j] == ']' else 0
    elif c==';': return
    elif c=='!': i, memory = 0, Memory(Byte(0))
    elif c=='#': print(memory.to_string(i))
    j += 1
  if to_print != "":
    print("=> "+to_print)
    to_print = ""

if __name__=='__main__':
  repl()