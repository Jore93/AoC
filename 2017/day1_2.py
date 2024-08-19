# -*- coding:UTF-8 -*-

import sys

def read_file(file_name):
    file = open(file_name)
    text = file.read()
    file.close()
    return text


def count_values(text):
    result = 0
    step = (len(text)-1)/2

    for i in range(len(text)-1):
        value1 = int(text[i])

        if(i<step):
            if text[i] == text[i+step]:
                result += value1
            else:
                pass
        else:
            if text[i] == text[i-step]:
                result += value1
            else:
                pass
            
    return result
    

if __name__ == "__main__":        
    t = read_file(sys.argv[1])
    v = count_values(t)
    print(v)