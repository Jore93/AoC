# -*- coding:UTF-8 -*-

import sys 
from cmath import sqrt
from math import ceil
from math import floor

def calc_grid_size(value):
    # Calculate length of one side of the grid
    val = sqrt(float(value))
    side = ceil(val.real)
    if side % 2 == 0:
        side += 1
    else:
        pass
        
    return side
    
def calc_path(side, value):
    value = int(value)
    # Calculate how many steps it takes to go directly to the most outer ring of the grid
    r = int(floor(side/2))
    # Right lower corner value
    r_low = int(side**2)
    # Left lower corner value
    l_low = int(r_low - side + 1)
    # Left top corner value
    l_top = int(l_low - side + 1)
    # Right top corner value
    r_top = int(l_top - side + 1)


    if value == 1:
        x = 0
        y = 0
    
    # Highest value on the grid level
    elif value == r_low or value == l_low or value == l_top or value == r_top:
        x = r
        y = r
            
    # Bottom side
    elif value < r_low and value > l_low:
        y = r
        if r_low-value == r:
            x = 0
        elif r_low-value < r:
            x = abs(r_low-value-r)
        else:
            x = abs(value-l_low-r)
    
    # Left side
    elif value < l_low and value > l_top:
        x = r
        if l_low-value == r:
            y = 0
        elif l_low-value < r:
            y = abs(l_low-value-r)
        else:
            y = abs(value-l_top-r)
            
    # Top side
    elif value < l_top and value > r_top:
        y = r
        if l_top-value == r:
            x = 0
        elif l_top -value < r:
            x = abs(l_top-value-r)
        else:
            x = abs(value-r_top-r)
    
    # Right side
    elif value < r_top:
        x = r
        if r_top-value == r:
            y = 0
        elif r_top-value < r:
            y = abs(r_top-value-r)
        else:
            val = sqrt(float(r_low))
            n = (int(val.real)-2)**2+1
            if value>=n and r<r_top-value:
                y = abs(r_top-value-r)
            else:
                pass

    else:
        pass
    
    return (x+y)
    
    
    
if __name__ == "__main__":
    s = calc_grid_size(sys.argv[1])
    ret = calc_path(s, sys.argv[1])
    print(ret)
    
    
    