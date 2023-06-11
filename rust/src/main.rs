#![allow(unused)]
use aoc::AocErrors;
use clap::Parser;
use std::{fs, io, path::PathBuf};

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
    //       This needs to be a *readable* buffer.
    let input = match cli.input {
        Some(input_file) => {
            if input_file.exists() && input_file.is_file() {
                fs::read_to_string(input_file)?.trim().to_string()
            } else {
                return Err(AocErrors::InputFileError(input_file).into());
            }
        }
        None => {
            let mut piped_input = String::new();
            io::stdin().read_line(&mut piped_input)?;
            piped_input = piped_input.trim().to_string();
            if piped_input.is_empty() {
                return Err(AocErrors::EmptyInputPipe.into());
            } else {
                piped_input
            }
        }
    };
    aoc::solve(cli.year, cli.day, input)?;
    Ok(())
}
