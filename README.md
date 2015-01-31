# Brainfuck Interpreter and Encoder

Brainfuck is an [esoteric language](http://en.wikipedia.org/wiki/Brainfuck) that has 8 instructions. 
This project has two parts:
  1. interpreter - interprets the brainfuck code
  2. encoder - generates (reasonably) condensed brainfuck code to output strings ([online version][1])

[1]:

#### Interpreter (`Brainfuck.py`)

Standard implementations of brainfuck require that memory be unlimited (or at least in theory) and
that each memory cell take on an 8-bit value. The current interpreter has a REPL (read evaluate
print loop) that executes the sequence of provided instructions, pausing for input if necessary,
and at the end outputting any printed information as well as a snapshot of the memory at that time.
The memory cell pointed to at that time will be green.

There are a couple bonus instructions:

  * `!` clears memory
  * `#` prints out memory at that moment
  * `;` exits the loop
  
Here is a screenshot of what the program looks like:

![screen-capture-1][2]

#### Encoder (`Encode_Brainfuck_Text.py` or `Encode_Brainfuck_Text.html`)

This was motivated by a [Code Golf][3] question. The challenge is to make a program that generates
the shortest possible brainfuck code that when run produces the given string input. This solution
performs slightly better than the best answer there (Lenna.png is 11.4 times its size when encoded
as opposed to 12.3 times).

The general approach (borrowed) is to construct a table that calculates the costs to go from a
given letter to another. Then, for every letter, we either choose to reuse the value left behind by
the previous letter, or to start from 0 again. To go from any one letter to another, we have three options

  <!--1. Concatenate a bunch of "+" or "-" together. So "a", which is 97, would be 97 plus signs concatenated.-->
  <!--2. We have sequences of the form `[A>B<]>` where `A` and `B` are themselves sequences of plus or minus-->
  <!--   signs. If we start this combination at a value of `C`, then we expect the loop to run $n$ times, where -->
  <!--   $$-->
  <!--    C+An = 0 \pmod{256}-->
  <!--   $$-->
  <!--   And the value pointed to when the snippet ends will be $x = Bn \pmod{256}$. Then, we get that $Ax = -->
  <!--   -BC \pmod{256}$.-->
  <!--3. Use a combination of 1 and 2. If the cost to go from a given letter to some intermediary letter plus-->
  <!--   the cost of going from that intermediary letter to the destination letter is less than the cost of-->
  <!--   going straight to the destination letter, take that path instead.-->

[2]: 
[3]: http://codegolf.stackexchange.com/questions/3450/how-to-encode-shortest-brainf-ck-strings

### Possible improvements

Make the algorithm less locally greedy: explore options 

