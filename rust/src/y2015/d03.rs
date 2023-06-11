use crate::{AocErrors, AocInput};

#[derive(Debug, Clone, PartialEq, Eq)]
struct Location {
    x: isize,
    y: isize,
}

impl Location {
    pub fn new(x: isize, y: isize) -> Self {
        Self { x, y }
    }

    pub fn go_north(&mut self) {
        self.y = self.y.wrapping_sub(1);
    }

    pub fn go_south(&mut self) {
        self.y = self.y.wrapping_add(1);
    }

    pub fn go_east(&mut self) {
        self.x = self.x.wrapping_sub(1);
    }

    pub fn go_west(&mut self) {
        self.x = self.x.wrapping_add(1);
    }
}
/// --- Day 3: Perfectly Spherical Houses in a Vacuum ---
/// Santa is delivering presents to an infinite two-dimensional grid of houses.
///
/// He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.
///
/// However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once.
/// How many houses receive at least one present?
///
/// For example:
///
///     > delivers presents to 2 houses: one at the starting location, and one to the east.
///     ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
///     ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
///
/// --- Part Two ---
///
/// The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.
///
/// Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.
///
/// This year, how many houses receive at least one present?
///
/// For example:
///
///     ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
///     ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
///     ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
///
pub fn solve(input: AocInput) -> Result<(), AocErrors> {
    // first, start tracking where I've been before. How do I store locations?
    let mut current_location = Location::new(0, 0);
    let mut char_count: usize = 0;
    let mut visited_locations: Vec<Location> = vec![current_location.clone()];
    for direction in input.chars() {
        char_count += 1;
        match direction {
            '<' => current_location.go_west(),
            '>' => current_location.go_east(),
            '^' => current_location.go_north(),
            'v' => current_location.go_south(),
            c => {
                return Err(AocErrors::InvalidInputFile(format!(
                    "`{c}` is not a valid input for 2015 day 03."
                )))
            }
        }
        if !visited_locations.contains(&current_location) {
            visited_locations.push(current_location.clone());
        };
    }
    println!("Part 1: At least 1 Visit: {}", visited_locations.len());
    // Note: Need to now account for the robot making the visits as well, so after the first house,
    // alternatively give each a direction to go, thus splitting it, but also making it so that
    // they can share the load. The first house gets 2 gifts though.
    let mut current_location_santa = Location::new(0, 0);
    let mut current_location_robot = Location::new(0, 0);
    let mut visited_locations: Vec<Location> = vec![current_location_santa.clone()];

    for (ix, direction) in input.chars().enumerate() {
        // santa gets the odd positions, robot gets the evens.
        match direction {
            '<' => {
                if ix % 2 == 0 {
                    current_location_robot.go_west();
                } else {
                    current_location_santa.go_west();
                }
            }
            '>' => {
                if ix % 2 == 0 {
                    current_location_robot.go_east();
                } else {
                    current_location_santa.go_east();
                }
            }
            '^' => {
                if ix % 2 == 0 {
                    current_location_robot.go_north();
                } else {
                    current_location_santa.go_north();
                }
            }
            'v' => {
                if ix % 2 == 0 {
                    current_location_robot.go_south();
                } else {
                    current_location_santa.go_south();
                }
            }
            c => {
                return Err(AocErrors::InvalidInputFile(format!(
                    "`{c}` is not a valid input for 2015 day 03."
                )))
            }
        }
        if !visited_locations.contains(&current_location_santa) {
            visited_locations.push(current_location_santa.clone());
        };
        if !visited_locations.contains(&current_location_robot) {
            visited_locations.push(current_location_robot.clone());
        };
    }
    println!(
        "Part 2: At least 1 Visit (with robot): {}",
        visited_locations.len()
    );
    Ok(())
}
