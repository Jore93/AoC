# -*- coding:UTF-8 -*-

import sys

def read_file(file_name):
    file = open(file_name)
    text = file.readlines()
    file.close()
    return text

def calc_checksum(text):
    checks = []
    val = []
    for i in range(len(text)-1):
        values = text[i]
        number = values.split("\t")

        for j in number:
            if(j.isdigit()):
                val.append(int(j))
            else:
                n = j.split("\n")
                val.append(int(n[0]))
                
        max_val = max(val)
        min_val = min(val)
        checksum = int(max_val)-int(min_val)
        checks.append(checksum)
        number = []
        val = []
    return sum(checks)

if __name__ == "__main__":        
    t = read_file(sys.argv[1])
    s = calc_checksum(t)
    print(s)