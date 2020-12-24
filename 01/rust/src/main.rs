#[macro_use]
extern crate timeit;

use std::fs;
use std::collections::HashSet;
//use std::time::Instant;

fn part_one(vec: &Vec<i64>) -> i64 {
    for x_int in vec {
        for y_int in vec { 
            if x_int+y_int==2020 {
                return x_int*y_int;
            }
        }
    }
    return -1;
}

fn part_two(vec: &Vec<i64>) -> i64 {
    for x_int in vec {
        for y_int in vec {
            for z_int in vec {
                if x_int+y_int+z_int==2020 {
                    return x_int*y_int*z_int;
                }
            }
        }
    }
    return -1;
}

fn part_one_fast(vec: &Vec<i64>) -> i64 {
    let mut needed_nums = HashSet::<i64>::new();
    for x_int in vec {
        if needed_nums.contains(x_int) {
            return (2020-x_int)*x_int;
        }
        let remainder = 2020 - x_int;
        needed_nums.insert(remainder);
    }
    return -1;
}

fn part_two_fast(vec: &Vec<i64>) -> i64 {
    let mut needed_nums = HashSet::<i64>::new();
    for x_int in vec {
        let remainder = 2020 - x_int;
        needed_nums.insert(remainder);
    }
    for x_int in vec {
        for y_int in vec {
            let sum = x_int + y_int;
            if needed_nums.contains(&sum) {
                let mult = x_int * y_int;
                return (2020-sum)*(mult);
            }
        }
    }
    return -1;
}

fn main() {
    let filename = "/Users/baumfalk/Programming/adventofcode/2020/01/input.txt";
    println!("In file {}", filename);

    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");
    //let split = contents.split("\n");

    //let vec = split.collect::<Vec<&str>>();
    //let vec_ints: Vec<i64> = contents.split("\n").map(|x| x.parse::<i64>().unwrap()).collect();
    let vec_ints: Vec<i64> = contents.split("\n").filter_map(|x| x.parse::<i64>().ok()).collect();
    println!("Part 1: {}", part_one(&vec_ints));
    println!("Part 2: {}", part_two(&vec_ints));
    println!("Part 1 fast: {}", part_one_fast(&vec_ints));
    println!("Part 2 fast: {}", part_two_fast(&vec_ints));

    timeit!({ part_one(&vec_ints);});
    timeit!({ part_two(&vec_ints);});
    timeit!({ part_one_fast(&vec_ints);});
    timeit!({ part_two_fast(&vec_ints);});
}
    
