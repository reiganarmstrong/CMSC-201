"""
File:         jumble.py
Author:       Reagan Armstrong
Date:         12/15/2020
Section:      24
E-mail:       reagana1@umbc.edu
Description:  This file has a jumble function that jumbles
              an inputted string based on the two integers also
              inputted.
"""
def jumble(a_string,a,b):
    used_indicies=[]
    jumbled_string=''
    for x in range(len(a_string)):
        possible_index=(a*x+b)%len(a_string)
        if possible_index not in used_indicies:
            # exectutes if the possible index has not already been used.
            jumbled_string+=a_string[possible_index:possible_index+1]
            used_indicies.append(possible_index)
    return jumbled_string
if __name__ == "__main__":
    print(jumble("201isover",3,5))