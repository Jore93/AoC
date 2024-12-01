use std::fs::read_to_string;

fn read_file(filename: &str) -> Vec<String> {
    read_to_string(filename)
        .unwrap() // panic on possible file-reading errors
        .lines() // split the string into an iterator of string slices
        .map(String::from) // make each slice into a string
        .collect() // gather them together into a vector
}

fn get_sets(line: &str) -> (i32, i32) {
    let sets = line.split_whitespace().collect::<Vec<&str>>();
    return (sets[0].parse::<i32>().unwrap(), sets[1].parse::<i32>().unwrap());
}

fn calc_distance(a: &i32, b: &i32) -> i32 {
    return (a - b).abs();
}

fn main() {
    let lines = read_file("../input.txt");

    let mut historians1 = Vec::<i32>::new();
    let mut historians2 = Vec::<i32>::new();

    for line in lines {
        let (a, b) = get_sets(&line);
        historians1.push(a);
        historians2.push(b);
    }

    historians1.sort();
    historians2.sort();

    let mut distance = 0;
    for i in 0..historians1.len() {
        distance += calc_distance(&historians1[i], &historians2[i]);
    }
    println!("{}", distance);
}
