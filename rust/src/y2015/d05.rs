use crate::AocErrors;

/// paste problem statement here.
/// --- Day 5: Doesn't He Have Intern-Elves For This? ---
///
/// Santa needs help figuring out which strings in his text file are naughty or nice.
///
/// A nice string is one with all of the following properties:
///
///     It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
///     It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or
///     aabbccdd (aa, bb, cc, or dd).
///     It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the
///     other requirements.
///
/// For example:
///
///     ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double
///     letter (...dd...), and none of the disallowed substrings.
///     aaa is nice because it has at least three vowels and a double letter, even though the
///     letters used by different rules overlap.
///     jchzalrnumimnmhp is naughty because it has no double letter.
///     haegwjzuvuyypxyu is naughty because it contains the string xy.
///     dvszwmarrgswjxmb is naughty because it contains only one vowel.
///
/// How many strings are nice?
///
/// --- Part Two ---
///
/// Realizing the error of his ways, Santa has switched to a better model of determining whether a
/// string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.
///
/// Now, a nice string is one with all of the following properties:
///
///     It contains a pair of any two letters that appears at least twice in the string without
///     overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
///     It contains at least one letter which repeats with exactly one letter between them, like
///     xyx, abcdefeghi (efe), or even aaa.
///
/// For example:
///
///     qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that
///     repeats with exactly one letter between them (zxz).
///     xxyxx is nice because it has a pair that appears twice and a letter that repeats with one
///     between, even though the letters used by each rule overlap.
///     uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter
///     between them.
///     ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but
///     no pair that appears twice.
///
/// How many strings are nice under these new rules?
pub fn solve(input: String) -> Result<(), AocErrors> {
    let nice_strings: Vec<&str> = input
        .lines()
        .filter(|x| x.to_string().is_nice_1())
        .collect();
    println!("2015 Day 4 Part 1: {}", nice_strings.len());
    let nice_strings: Vec<&str> = input
        .lines()
        .filter(|x| x.to_string().is_nice_2())
        .collect();
    println!("2015 Day 4 Part 1: {}", nice_strings.len());
    Ok(())
}

trait IsNice {
    fn is_nice_1(self) -> bool;
    fn is_nice_2(self) -> bool;
}

impl IsNice for String {
    /// A nice string is one with all of the following properties:
    ///
    ///     It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    ///     It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or
    ///     aabbccdd (aa, bb, cc, or dd).
    ///     It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the
    ///     other requirements.
    fn is_nice_1(self) -> bool {
        let mut vowel_count = 0;
        let vowels: Vec<char> = vec!['a', 'e', 'i', 'o', 'u'];
        let contains_at_least_3_vowels = self
            .chars()
            .filter(|x| vowels.contains(x))
            .collect::<Vec<char>>()
            .len()
            >= 3;
        let contains_repeated_chars = {
            let mut last_char = None;
            let mut contains_repeated_chars = false;
            for char in self.chars() {
                if let Some(last) = last_char {
                    if last == char {
                        contains_repeated_chars = true;
                        break;
                    } else {
                        last_char = Some(char);
                    }
                } else {
                    last_char = Some(char);
                }
            }
            contains_repeated_chars
        };

        let doesnt_contain_unwanted_strings = !(self.contains("ab")
            || self.contains("cd")
            || self.contains("pq")
            || self.contains("xy"));
        contains_at_least_3_vowels && contains_repeated_chars && doesnt_contain_unwanted_strings
    }

    /// A nice string is one with all of the following properties:
    ///
    ///     It contains a pair of any two letters that appears at least twice in the string without
    ///     overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    ///     It contains at least one letter which repeats with exactly one letter between them, like
    ///     xyx, abcdefeghi (efe), or even aaa.
    fn is_nice_2(self) -> bool {
        todo!()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_nice_1() {
        let samples: Vec<(&str, bool)> = vec![
            ("ugknbfddgicrmopn", true),
            ("aaa", true),
            ("jchzalrnumimnmhp", false),
            ("haegwjzuvuyypxyu", false),
            ("dvszwmarrgswjxmb", false),
        ];
        assert_eq!(String::from("ugknbfddgicrmopn").is_nice_1(), true);

        for (sample, is_nice) in samples {
            assert_eq!(String::from(sample).is_nice_1(), is_nice);
        }
    }
    #[test]
    fn test_nice_2() {
        let samples: Vec<(&str, bool)> = vec![
            ("qjhvhtzxzqqjkmpb", true),
            ("xxyxx", true),
            ("uurcxstgmygtbstg", false),
            ("ieodomkazucvgmuy", false),
        ];

        for (sample, is_nice) in samples {
            assert_eq!(String::from(sample).is_nice_2(), is_nice);
        }
    }
}
