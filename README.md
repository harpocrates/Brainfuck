# Brainfuck Interpreter and Encoder

Brainfuck is an [esoteric language](http://en.wikipedia.org/wiki/Brainfuck) that has 8 instructions. 
This project has two parts:
  1. interpreter - interprets the brainfuck code
  2. encoder - generates (reasonably) condensed brainfuck code to output strings ([online version][1])

#### Interpreter (`Brainfuck.py`)

Standard implementations of brainfuck require that memory be unlimited (or at least in theory) and
that each memory cell take on an 8-bit value. The current interpreter has a REPL (read evaluate
print loop) that executes the sequence of provided instructions, pausing for input if necessary,
and at the end outputting any printed information as well as a snapshot of the memory at that time.
The memory cell pointed to at that time will be green.

There are a couple bonus instructions:

  * `!` clears memory and resets the pointer to address 0
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
the previous letter, or to start from 0 again.

The Python program `pickle`s this table, so as not to recalculate it every time. The Javascript version
stores it in a `.js` file.

[1]: http://rawgit.com/harpocrates/Brainfuck/master/JavaScript/Encode_Brainfuck_Text.html
[2]: https://raw.githubusercontent.com/harpocrates/Brainfuck/master/Images/screencapture-1.png
[3]: http://codegolf.stackexchange.com/questions/3450/how-to-encode-shortest-brainf-ck-strings

##### Possible improvements

  * Make the algorithm less locally greedy: explore options of going forward and back
  * Construct multiple letters at a time.

