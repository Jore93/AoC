# -*- coding:UTF-8 -*-

import sys

def read_file(file_name):
    file = open(file_name)
    text = file.read()
    file.close()
    return text


def count_values(text):
    result = 0

    for i in range(len(text)-1):
        value1 = int(text[i])

        if text[i] == text[i+1]:
            result += value1
        else:
            pass
        
    if text[0] == text[-2]:
        result += int(text[0])
    else:
        pass
    
    return result
    

if __name__ == "__main__":        
    t = read_file(sys.argv[1])
    v = count_values(t)
    print(v)