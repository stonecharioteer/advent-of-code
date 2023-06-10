#![allow(unused)]
use std::str::FromStr;

pub mod y2015;
pub mod y2016;
pub mod y2017;
pub mod y2018;
pub mod y2019;
pub mod y2020;
pub mod y2021;
pub mod y2022;

/// Internal errors for this crate
#[derive(thiserror::Error, Debug, Clone)]
pub enum AocErrors {
    #[error("Internal error.")]
    Internal(String),
    #[error("Not Found.")]
    NotFound,
    #[error("Parsing Error: {0}")]
    ParseError(String),
    #[error("Invalid AoC Event Year: {0}")]
    InvalidEventYear(u16),
}

/// a function that takes a year and a day, and runs the
/// appropriate solution for the provided input,
/// which could either be piped in, or a file input.
pub fn solve(year: Year, day: u8, input: AocInput) -> Result<(), AocErrors> {
    match year {
        Year::Y2015 => y2015::solve(day, input),
        Year::Y2016 => y2016::solve(day, input),
        Year::Y2017 => y2017::solve(day, input),
        Year::Y2018 => y2018::solve(day, input),
        Year::Y2019 => y2019::solve(day, input),
        Year::Y2020 => y2020::solve(day, input),
        Year::Y2021 => y2021::solve(day, input),
        Year::Y2022 => y2022::solve(day, input),
    }
}

/// All the years listed in https://adventofcode.com/2022/events
/// corresponding to AOC events.
#[derive(Debug, PartialEq, Clone)]
pub enum Year {
    Y2015,
    Y2016,
    Y2017,
    Y2018,
    Y2019,
    Y2020,
    Y2021,
    Y2022,
}

impl FromStr for Year {
    type Err = AocErrors;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let s = String::from(s);
        if let Ok(year) = s.parse::<u16>() {
            match year {
                2015 => Ok(Year::Y2015),
                2016 => Ok(Year::Y2016),
                2017 => Ok(Year::Y2017),
                2018 => Ok(Year::Y2018),
                2019 => Ok(Year::Y2019),
                2020 => Ok(Year::Y2020),
                2021 => Ok(Year::Y2021),
                2022 => Ok(Year::Y2022),
                v => Err(AocErrors::InvalidEventYear(v)),
            }
        } else {
            Err(AocErrors::ParseError(s.to_string()))
        }
    }
}

type AocInput = String;
