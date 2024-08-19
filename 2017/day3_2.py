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

def check_place(side, value):
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
    elif value == r_low:
        x = r
        y = -r
        
    elif value == l_low:
        x = -r
        y = -r
        
    elif value == l_top:
        x = -r
        y = r
        
    elif value == r_top:
        x = r
        y = r
        
    # Bottom side
    elif value < r_low and value > l_low:
        y = -r
        if r_low-value == r:
            x = 0
        elif r_low-value < r:
            x = abs(r_low-value-r)
        else:
            x = -abs(value-l_low-r)
    
    # Left side
    elif value < l_low and value > l_top:
        x = -r
        if l_low-value == r:
            y = 0
        elif l_low-value < r:
            y = -abs(l_low-value-r)
        else:
            y = abs(value-l_top-r)
            
    # Top side
    elif value < l_top and value > r_top:
        y = r
        if l_top-value == r:
            x = 0
        elif l_top-value < r:
            x = -abs(l_top-value-r)
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
                y = -abs(r_top-value-r)
            else:
                pass

    else:
        pass
    
    place = (x, y)
    return place


def calc_new_value(size, value, all_val):
    val = 0
    x, y = check_place(size, value)
    for i in all_val:
        s = calc_grid_size(i[3])
        xc, yc = check_place(s, i[3])
        if x >= 0 and y >= 0:
            # Top right quarter
            if x == xc and y == yc-1 and y = yc and y == yc+1:
                
            elif x == xc -1 and x == xc and x == xc+1 and y == yc:
                
            elif x == xc and y == yc and y == yc-1
                
        elif x < 0 and y >= 0:
            # Top left quarter
            
        elif x < 0 and y < 0:
            # Bottom left quarter
            
        elif x >= 0 and y < 0:
            # Bottom right quarter
            
        else:
            pass
    return val


if __name__ == "__main__":
    ret = 0
    i = 1
    all_values = [1, 0, 0, 1]
    while(ret<sys.argv[1]):
        s = calc_grid_size(i)
        x_coord, y_coord = check_place(s, i)
        new_val = calc_new_value(s, i, all_values)
        all_values.append([i, x_coord, y_coord, new_val])
        i += 1
    
    