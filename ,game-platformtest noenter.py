# general config:
player = "#"
background = "."
ground = "@"
# this decides if you want a pre generated level or just a space to mess around in (capitalise true or false):
levelgen = True

# config 1, this is for a pre generated level, do not touch config 2:
obstacles = "■"

# ///////////////////////////////////////////////////////////////

# config 2, this is just to mess around, do not touch config 1:
# how long you want the level to be (default is "0"):
genkeep = 10

# end of config

import time
import getch

print("Use wasd to move, any other key will exit the game (including double presses!)\n")
pos = 1
pos2 = 4
global game
game = True
dot = background
if levelgen is True:
   bg = f"{background} "*10 + f"{obstacles} "*3 + f"{background} "*57
   ground = f"{ground} "*70
   hash = f"{player}"
else:
   bg = f"{background} "*genkeep
   ground = f"{ground} "*genkeep
   hash = f"{player}"
   genstatekeep = genkeep + 1


def a():
   print("\n"); print("\n"); print("\n"); print("\n"); print("\n")
   global pos
   global pos2
   if pos2 == 1:
      xy()
      p(); p(); p(); k()
   elif pos2 == 2:
      p()
      xy()
      p(); p(); k()
   elif pos2 == 3:
      p(); p()
      xy()
      p(); k()
   elif pos2 == 4:
      p(); p(); p()
      xy()
      k()
   elif pos2 == 5:
      pos2 = 4
      p(); p(); p()
      xy()
      k()

def xy():
   global gen
   global genstate
   global genkeep
   global genstatekeep
   global pos
   global genvar
   if levelgen is True:
      gen = 70
      genstate = 71
   else:
      gen = genkeep
      genstate = genstatekeep
   gen -= pos
   genstate -= gen
   while gen >= 2:
      if genstate >= 2:
         print(".", end=" ")
         genstate -= 1
      elif genstate == 1:
          t()
          genstate = 0
      else:
         print(".", end=" ") 
         gen -= 1
   print(" ")


def p():
   print(bg)

def t():
   print(hash, end=" ")

def h():
   print(dot, end=" ")

def k():
   print(ground)

def jump():
   global pos2
   global pos
   pos2 = 3
   a()
   m = getch.getch()
   if m == "d":
      pos += 1
   elif m == "a":
      pos -= 1
   elif m == " ":
      pos -= 1
   pos2 = 2
   a()
   m = getch.getch()
   if m == "d":
      pos += 1
   elif m == "a":
      pos -= 1
   pos2 = 3
   a()
   m = getch.getch()
   if m == "d":
      pos += 1
   elif m == "a":
      pos -= 1
   pos2 = 4
   a()
   m = getch.getch()
   if m == "d":
      pos += 1
   elif m == "a":
      pos -= 1
 
a()

def move():
   global pos; global pos2
   if m == "d":
      pos += 1
   elif m == "a":
      pos -= 1
   elif m == "w":
      jump()
 
while game is True:
   global m
   m = getch.getch()
   if m in ["w", "a", "s", "d"]:
      move(); a()
   else:
      print("Game ended")
      game = False
   

