use crate::{AocErrors, AocInput};

/// --- Day 1: No Time for a Taxicab ---
///
/// Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's
/// oscillator is regulated by stars. Unfortunately, the stars have been stolen... by the Easter
/// Bunny. To save Christmas, Santa needs you to retrieve all fifty stars by December 25th.
///
/// Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent
/// calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one
/// star. Good luck!
///
/// You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is
/// as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves
/// intercepted start here, and nobody had time to work them out further.
///
/// The Document indicates that you should start at the given coordinates (where you just landed)
/// and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90
/// degrees, then walk forward the given number of blocks, ending at a new intersection.
///
/// There's no time to follow such ridiculous instructions on foot, though, so you take a moment
/// and work out the destination. Given that you can only walk on the street grid of the city, how
/// far is the shortest path to the destination?
///
/// Note: https://en.wikipedia.org/wiki/Taxicab_geometry
/// For example:
///
///     Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
///     R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
///     R5, L5, R5, R3 leaves you 12 blocks away.
///
/// How many blocks away is Easter Bunny HQ?
///
/// --- Part Two ---
///
/// Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ
/// is actually at the first location you visit twice.
///
/// For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4
/// blocks away, due East.
///
/// How many blocks away is the first location you visit twice?
pub fn solve(input: AocInput) -> Result<(), AocErrors> {
    let (part_1, part_2) = solution(input);
    println!("2016 Day 1 Part 1: {part_1}");
    match part_2 {
        Some(part_2) => {
            println!("2016 Day 1 Part 2: {part_2}");
            Ok(())

        },
            None => {
            Err(AocErrors::Internal("This input file didn't seem to have any repeated points. The algorithm must have missed some edgecases for 2016 day 1".to_owned()))
        }
    }
}

/// Different directions on the compass
#[derive(Debug, PartialEq, Clone)]
enum Direction {
    North,
    East,
    West,
    South,
}

impl Direction {
    pub fn turn_right(self) -> Self {
        match self {
            Direction::North => Direction::East,
            Direction::East => Direction::South,
            Direction::South => Direction::West,
            Direction::West => Direction::North,
        }
    }
    pub fn turn_left(self) -> Self {
        match self {
            Direction::North => Direction::West,
            Direction::West => Direction::South,
            Direction::South => Direction::East,
            Direction::East => Direction::North,
        }
    }
}

/// Enum to define the instructions
#[derive(Debug, PartialEq, Clone)]
enum Instruction {
    Left(usize),
    Right(usize),
}

impl Instruction {
    /// constructor for an Instruction from a string that looks like `R<usize>` or `L<usize>`
    pub fn new(dir: &str) -> Result<Self, AocErrors> {
        if dir.len() < 2 {
            return Err(AocErrors::InvalidInputFile(format!(
                "`{dir}` is in invalid input for 2016 Day 01"
            )));
        } else {
            let mut dir_chars = dir.chars();
            let direction = dir_chars.next().unwrap();
            let magnitude_str: String = dir_chars.collect();
            let magnitude: usize = match magnitude_str.parse() {
                Ok(v) => v,
                Err(_) => {
                    return Err(AocErrors::InvalidInputFile(format!(
                        "Error parsing `{dir}`. `{magnitude_str}"
                    )))
                }
            };
            match direction {
                'R' => Ok(Instruction::Right(magnitude)),
                'L' => Ok(Instruction::Left(magnitude)),
                e => Err(AocErrors::InvalidInputFile(format!(
                    "`{e}` is an invalid direction for 2016 day 1. Input: {dir}"
                ))),
            }
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
struct Position {
    x: isize,
    y: isize,
}

impl Position {
    pub fn go_north(&mut self, distance: usize) {
        self.y += distance as isize;
    }

    pub fn go_south(&mut self, distance: usize) {
        self.y -= distance as isize;
    }

    pub fn go_east(&mut self, distance: usize) {
        self.x += distance as isize;
    }

    pub fn go_west(&mut self, distance: usize) {
        self.x -= distance as isize;
    }

    pub fn taxicab_distance(self, other: &Self) -> usize {
        ((self.x - other.x).abs() + (self.y - other.y).abs()) as usize
    }
}

fn solution(input: AocInput) -> (usize, Option<usize>) {
    let instructions: Vec<&str> = input.split(", ").collect();
    let instructions: Vec<Instruction> = instructions
        .iter()
        .map(|x| Instruction::new(x).unwrap())
        .collect();

    let starting_position = Position { x: 0, y: 0 };
    let mut current_position = starting_position.clone();
    let mut current_facing_direction = Direction::North;
    let mut visited_locations: Vec<Position> = vec![current_position.clone()];
    let mut hq_position: Option<Position> = None;
    let mut hq_not_found = true;
    for instruction in &instructions {
        let distance: usize = match instruction {
            Instruction::Left(v) => {
                current_facing_direction = current_facing_direction.turn_left();
                v
            }
            Instruction::Right(v) => {
                current_facing_direction = current_facing_direction.turn_right();
                v
            }
        }
        .to_owned();
        for _ in 0..distance {
            match current_facing_direction {
                Direction::North => current_position.go_north(1),
                Direction::South => current_position.go_south(1),
                Direction::East => current_position.go_east(1),
                Direction::West => current_position.go_west(1),
            };
            if visited_locations.contains(&current_position.clone()) && hq_not_found {
                hq_not_found = false;
                hq_position = Some(current_position.clone());
            } else {
                visited_locations.push(current_position.clone());
            };
        }
    }

    (
        current_position.taxicab_distance(&starting_position),
        match hq_position {
            None => None,
            Some(hq_pos) => Some(hq_pos.taxicab_distance(&starting_position)),
        },
    )
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        let inputs = vec![("R2, L3", 5), ("R2, R2, R2", 2), ("R5, L5, R5, R3", 12)];

        for (input, answer) in inputs {
            let (part_1, _) = solution(input.to_string());
            assert_eq!(part_1, answer);
        }
    }

    #[test]
    fn test_part_2() {
        let (part_1, part_2) = solution(String::from("R8, R4, R4, R8"));
        dbg!(part_1);
        assert_eq!(part_2, Some(4));
    }
}
