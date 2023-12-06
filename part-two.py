#!/usr/bin/env python3

import os
import math

def answer(input_file):
    with open(input_file, "r") as input:
        data = input.read().split('\n')
    time = int(data[0][10:].replace(' ',''))
    distance = int(data[1][10:].replace(' ',''))
    sqrtbsqminusfourac = math.sqrt((time * time) - (4 * distance))
    lower_limit = math.ceil((- time + sqrtbsqminusfourac) / -2)
    upper_limit = math.floor((- time - sqrtbsqminusfourac) / -2)
    if (lower_limit * time) - (lower_limit * lower_limit)  == distance:
        lower_limit += 1
    if (upper_limit * time) - (upper_limit * upper_limit)  == distance:
        upper_limit -= 1

    answer = (upper_limit - lower_limit + 1)

    print(f'The answer is: {answer}')

input_file = os.path.join(os.path.dirname(__file__), "input")
answer(input_file)
