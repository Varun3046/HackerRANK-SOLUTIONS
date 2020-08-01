#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):

# Create an array of length len(arr)+2 , initialize the list_array[len(arr) - 1] as arr[len(arr) - 1] and list_array[len(arr) -2] = max(arr[len(arr)-1], arr[len(arr)-2])
# list_arr[len(arr)-1] =  max(list_arr[i+2]+arr[i],list_arr[i+1],arr[i]) shd be the max of list_arr[i+2] + arr[i] ,list_arr[i+1] and arr[i]

# look for max between 
    list_arr = [0]*(n+2)    
    for i in reversed(range(len(arr))):
        if i==(len(arr)-1):
            list_arr[i]=arr[i]
        elif i==(len(arr)-2):
            list_arr[i]= max(arr[i],arr[i+1])
        else:
            list_arr[i] = max(list_arr[i+2]+arr[i],list_arr[i+1],arr[i])
    return list_arr[0]

    max(maxSubsetSum(arr))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
