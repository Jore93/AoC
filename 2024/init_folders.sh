#!/bin/bash

for i in {1..25}
do
  cd $i
  cargo new task1
  cargo new task2
  cd ..
done
