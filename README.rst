==================
advent-of-code
==================

My solutions for `advent of code. <https://adventofcode.com/>`_

-------
About
-------

Advent of Code is a bunch of programming exercises that are quite fun to do.
They mostly involve command line parsing and text processing.
They range from easy to medium in terms of difficulty.
I have wanted to get into the habit of doing these for quite some time.

.. note:: 

    I am trying out Advent of Code in several languages. I will organize them
    by branches.

    Here are the languages I hope to try these with:

    * Rust
    * Go
    * Python
    * Javascript
    * Kotlin
    * Elixir
    * Ruby
    * Lua
    * Haskell
    * Zig or Nim (undecided)


----------------
CLI
----------------

Irrespective of the language, here's what I want to support:

``aoc -y <year> -d <day> <path-to-file>`` should output the result for the given day

Additionally, if you want to pipe the file contents in:

``cat <path-to-file> | aoc -y <year> -d <day>``

Additional parameters:

``--log-file`` should output the logs (if any) to the file.

``-v / --verbosity`` should increase the log level (support upto ``-vvvv`` to
correspond to ``ERROR``, ``WARNING``, ``INFO``, ``DEBUG``)

Similarily, ``-q / --quiet`` should decrease the log level.

--------------------
Testing
--------------------

The tests should target the individual language implementations of this CLI, not the problem code itself.

-----------------
Wishlist
-----------------

* Need to write something to automatically get the input files.
* Need to write a flow to automatically submit results.

-------------------
Documentation
-------------------

Each language-specific documentation of these solutions will be in `docs/ <docs/>`_
