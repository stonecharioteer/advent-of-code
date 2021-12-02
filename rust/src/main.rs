use std::path::PathBuf;
use structopt::StructOpt;

use aoc{self, y2019};

#[derive(Debug, StructOpt)]
#[structopt(name = "aoc", about = "A CLI to run advent of code")]
struct Opt {
    /// Year
    year: usize,

    /// Day
    day: usize,

    /// Optional path to Input file,, if not supplied, will read from stdin
    input: Option<PathBuf>,
}

fn main() {
    let opt = Opt::from_args();
    aoc::foo();
    aoc::y2019::lol()

}
