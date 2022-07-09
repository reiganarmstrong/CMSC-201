"""
File:         longest_substring.py
Author:       Reagan Armstrong
Date:         12/15/2020
Section:      24
E-mail:       reagana1@umbc.edu
Description:  This file has a longest_substring function that 
              finds the longest substring of the inputted 
              find_string in the inputted total_string.
"""


def longest_substring(total_string, find_string):
    longest_sequence = 0
    for x in range(len(total_string)):
        # iterates through the total_string
        for y in range(len(find_string)):
            # iterates through the find_string
            if total_string[x:x+1] == find_string[y:y+1]:
                z = 1
                found_match = True
                while(x+z < len(total_string)
                      and y+z < len(find_string)
                      and found_match):
                    # continues to iterate from x in total_string and
                    # y in find_string and sees if the pattern
                    # continues
                    if(total_string[x+z:x+z+1] == find_string[y+z:y+z+1]):
                        z += 1
                    else:
                        found_match = False
                if z > longest_sequence:
                    # checks if this sequence is the longest found
                    longest_sequence = z
    return longest_sequence


if __name__ == "__main__":
    print(longest_substring('the name of the game is asdf so play it well',
                            'asasdasdf'))
