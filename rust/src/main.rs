#![allow(unused)]
use aoc::y2019;
use clap::Parser;
use std::path::PathBuf;

#[derive(Debug, Parser)]
#[command(author, version, about, long_about = None)]
struct Cli {
    /// Year
    #[arg(short, long)]
    year: usize,

    /// Day
    #[arg(short, long)]
    day: usize,

    /// Optional path to Input file, if not supplied,
    /// will read from stdin
    input: Option<PathBuf>,
}

fn main() {
    let cli = Cli::parse();
    aoc::foo();
    y2019::lol();
}
