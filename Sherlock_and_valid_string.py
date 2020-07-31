#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):

#the idea is to create a dictionary of all the characters in the string with their number of occurences as values .
#once created , we create another dictionary with count as the key and values as the number of characters that have the corresponding count
#create two variables max_count and min_count to store the max and min number of occurences of the NUMBER OF CHARACTERS THAT HAVE THE CORRESPONDING COUNT
#check for the length of the count  dictionary , if 1 then all the characters occured same number of times
# else if length is 2 , check  for difference between max and min count
#now consider two cases , if the count of the max count( number of times the max count has appeared ie number of characters having max count) is 1 then the extra charater can be removed  , so it is true
#else if count of min count( number of times the max count has appeared ie number of characters having min count) is 1 then this character can be removed all along , so it is true
# rest of the cases are false

    for char in s:
        if char in char_dict:
            char_dict[char]+=1
        else:
            char_dict[char]=1
        
    min_count = char_dict[char]
    max_count = char_dict[char]

    count_dict = {}
    for ele ,value in char_dict.items():
        if value in count_dict:
            count_dict[value]+=1
        else:
            count_dict[value]=1
        if value > max_count:
            max_count =value
        if value < min_count:
            min_count = value
            
    if len(count_dict) ==1 :
        return 'YES'
    elif len(count_dict)==2:
        if count_dict[max_count] == 1 and max_count - min_count==1:
            return 'YES'
        elif count_dict[min_count] == 1 and max_count - min_count==1:
            return 'YES'
    
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
