"""
File:         nth_day.py
Author:       Reagan Armstrong
Date:         12/15/2020
Section:      24
E-mail:       reagana1@umbc.edu
Description:  This file has a function nth_day_of_christmas
              that returns the total number of presents
              someone recieves on the inputted day.
"""


def nth_day_of_christmas(day):
    if day == 0:
        # base case of day=0
        return 0
    else:
        # recursive case day>0
        num_presents = (day*(day+1))/2
        return num_presents+nth_day_of_christmas(day-1)


if __name__ == "__main__":
    print(nth_day_of_christmas(12))
