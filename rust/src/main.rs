#![allow(unused)]
use clap::Parser;
use std::path::PathBuf;

#[derive(Debug, Parser)]
#[command(author, version, about, long_about = None)]
struct Cli {
    /// Year (2015-2022)
    #[arg(short, long)]
    year: aoc::Year,

    /// Day (1-25)
    #[arg(short, long)]
    day: u8,

    /// Optional path to Input file, if not supplied,
    /// will read from stdin
    input: Option<PathBuf>,
}

fn main() -> Result<(), anyhow::Error> {
    let cli = Cli::parse();
    // TODO: READ the input, either file or the piped input
    let input = String::from("Input problem text");

    aoc::solve(cli.year, cli.day, input)?;
    Ok(())
}
