#!/usr/bin/env python3

from itertools import *
import pickle

class Byte(int):
  def __new__(cls, value, **kwargs):
    inst = super(Byte, cls).__new__(cls, value % 256)
    return inst
  def __iadd__(self, other): return Byte((self + other) % 256)
  def __isub__(self, other): return Byte((self - other) % 256)

def get_num_naive(to, frm=Byte(0)):
  dif = (to-frm) % 256
  return '-'*(256-dif) if dif > 128 else '+'*dif

# ONE TIME OVERHEAD (pickled table)
T = {}
import os.path
if os.path.isfile("table.p"):
  T = pickle.load(open("table.p", "rb"))
else:
  T = { (frm, to):get_num_naive(Byte(to),Byte(frm)) for to in range(256) for frm in range(256) }

  # Modular multiplication. - a[b>c<]> = x => c*a = b*x (mod 256)
  for frm in imap(Byte,range(0,256)):
    for b in imap(Byte,chain(range(-20,0),range(1,21))):
      for c in imap(Byte,chain(range(-20,0),range(1,21))):
        a, to = frm, Byte(0)
        for _ in range(256):
          if a == Byte(0):
            T[frm,to] = min(["[{}>{}<]>".format(get_num_naive(b),get_num_naive(c)), T[frm,to]], key=len)
            break
          a  += b
          to += c

  changes = True
  while changes:
    changes = None

    # Triangle inequality. (A->B).(B->C) = (A->C)
    for frm in imap(Byte,range(256)):
      for to in imap(Byte,range(256)):
        for z in imap(Byte,range(256)):
          if len(T[frm,z]) + len(T[z,to]) < len(T[frm,to]):
            T[frm,to] = T[frm,z] + T[z,to]
            changes = True

  pickle.dump(T, open("table.p", "wb"))

def generate(string):
  to_parse = [ Byte(ord(c)) for c in string ] if isinstance(string,str) else string
  to_return = ""

  prev = None
  for n in to_parse:
    if prev != None and len(T[prev,n]) < len(T[Byte(0),n])+1: to_return += T[prev,n]
    elif prev != None:                                        to_return += ">"+T[Byte(0),n]
    else:                                                     to_return += T[Byte(0),n]
    to_return += "."
    prev = n

  return to_return

B = lambda x,y: T[Byte(x),Byte(y)]

if __name__ == '__main__':
  print('Welcome to the "Brainfuck" language encoder.')
  while True:
    print(generate(input('> ')))

# Lenna score ratio is 11.4110021538
#
#       with open('Lenna1.txt', 'r') as f:
#         d = filter(lambda x: x!=Byte(0), map(Byte,map(lambda x: int(x, base=16),f.readlines())))
#       print(len(generate(d))/float(len(d)))


