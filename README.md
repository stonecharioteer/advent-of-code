# Advent of Code

My solutions for [Advent of Code.](https://adventofcode.com/).

## About

Advent of Code is a bunch of programming exercises that are quite fun to do.
They mostly involve command line parsing and text processing. They range from
easy to medium in terms of difficulty. I have wanted to get into the habit of
doing these for quite some time.

### Note

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


## CLI

Irrespective of the language, here's what I want to support:

`aoc -y <year> -d <day> <path-to-file>` should output the result for the given day

Additionally, if you want to pipe the file contents in:

`cat <path-to-file> | aoc -y <year> -d <day>`

Additional parameters:

`--log-file` should output the logs (if any) to the file.

`-v / --verbosity` should increase the log level (support upto `-vvvv` to
correspond to `ERROR`, `WARNING`, `INFO`, `DEBUG`)

Similarily, `-q / --quiet` should decrease the log level.

## Testing

I want to add tests for both the CLI, as well as for individual
samples, so that I'm testing for the smaller test-cases that are in the
AOC problem descriptions.

# Wishlist

* Need to write something to automatically get the input files.
* Need to write a flow to automatically submit results.

## Documentation

* [Rust](./rust/README.md)
* [Go](./go/README.md)
* [Python](./python/README.md)
* [Javascript](./nodejs/README.md)
* [Kotlin](./kotlin/README.md)
* [Elixir](./elixir/README.md)
* [Ruby](./ruby/README.md)
* [Lua](./lua/README.md)
* [Haskell](./Haskell/README.md)
* [General Documentation](./docs/README.md)

