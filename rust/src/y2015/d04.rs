use crate::AocErrors;

/// paste problem statement here.
/// --- Day 4: The Ideal Stocking Stuffer ---
///
/// Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the
/// economically forward-thinking little girls and boys.
///
/// To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes.
/// The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a
/// number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no
/// leading zeroes: 1, 2, 3, ...) that produces such a hash.
///
/// For example:
///
///     * If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts
///       with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
///
///     * If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting
///       with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
///
pub fn solve(input: String) -> Result<(), AocErrors> {
    let (_, part_1) = get_hash(input.clone(), 5)?;
    println!("2015 Day 4 Part 1: {part_1}");
    let (_, part_2) = get_hash(input.clone(), 6)?;
    println!("2015 Day 4 Part 2: {part_2}");
    Ok(())
}

/// function to retrieve the hash of a secret key, along with the number that needs to be
/// appended in order for the hash to have the required number of zeroes.
fn get_hash(secret_key: String, zeroes: usize) -> Result<(String, usize), AocErrors> {
    let mut suffix = 1;
    let prefix = "0".repeat(zeroes);
    println!("Searching for a digest that has a prefix of {zeroes} 0s : `{prefix}`");

    loop {
        let digest = md5::compute(format!("{secret_key}{suffix}"));
        let digest_str = format!("{:x}", digest);
        if digest_str.starts_with(&prefix) {
            return Ok((digest_str, suffix));
        } else {
            suffix += 1;
        }
    }

    Err(AocErrors::Internal(
        "The code shouldn't reach this point".to_string(),
    ))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_2015_day_04_five_zeroes_one() {
        let secret_key = "abcdef".to_string();
        let answer = 609043;
        let (_, tries_for_hash) = get_hash(secret_key, 5).unwrap();
        assert_eq!(tries_for_hash, answer);
    }

    #[test]
    fn test_2015_day_04_five_zeroes_two() {
        let secret_key = "pqrstuv".to_string();
        let answer = 1048970;
        let (_, tries_for_hash) = get_hash(secret_key, 5).unwrap();
        assert_eq!(tries_for_hash, answer);
    }
}
