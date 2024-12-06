use std::fs::read_to_string;

fn read_file(filename: &str) -> Vec<String> {
    read_to_string(filename)
        .unwrap() // panic on possible file-reading errors
        .lines() // split the string into an iterator of string slices
        .map(String::from) // make each slice into a string
        .collect() // gather them together into a vector
}

fn difference_is_ok(a :&i32, b:&i32) -> bool {
    let diff = (a-b).abs();
    diff >= 1 && diff <= 3
}

fn get_report(line: &str) -> Vec<&str> {
    let report = line.split_whitespace().collect::<Vec<&str>>();
    report
}

fn level_is_linear(a: &i32, b: &i32, ascending: bool) -> bool {
    ascending == (a < b)
}

fn values_ascending(a: &str, b: &str) -> bool {
    let a = a.parse::<i32>().unwrap();
    let b = b.parse::<i32>().unwrap();
    a < b
}

fn main() {
    let lines = read_file("../input.txt");
    let mut safe_reports = 0;
    for line in lines {
        let mut line_ok = false;
        let report = get_report(&line);
        let ascending = values_ascending(&report[0], &report[1]);
        for i in 0..report.len()-1 {
            let diff_ok = difference_is_ok(&report[i].parse::<i32>().unwrap(), &report[i+1].parse::<i32>().unwrap());
            let level_ok = level_is_linear(&report[i].parse::<i32>().unwrap(), &report[i+1].parse::<i32>().unwrap(), ascending);
            line_ok = diff_ok && level_ok;
            if !line_ok {
                break;
            }
        }
        if line_ok {
            safe_reports += 1;
        }
    }
    println!("{}", safe_reports);
}
