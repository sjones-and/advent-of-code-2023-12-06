#!/usr/bin/env python3

import os
import math
from time import perf_counter_ns

def answer(input_file):
    start = perf_counter_ns()
    with open(input_file, "r") as input:
        data = input.read().split('\n')
    times = [int(time) for time in data[0][10:].split(' ') if len(time) > 0]
    distances = [int(distance) for distance in data[1][10:].split(' ') if len(distance) > 0]
    answer = 1
    for ix in range(len(times)):
        sqrtbsqminusfourac = math.sqrt((times[ix] * times[ix]) - (4 * distances[ix]))
        lower_limit = math.ceil((- times[ix] + sqrtbsqminusfourac) / -2)
        upper_limit = math.floor((- times[ix] - sqrtbsqminusfourac) / -2)
        if (lower_limit * times[ix]) - (lower_limit * lower_limit)  == distances[ix]:
            lower_limit += 1
        if (upper_limit * times[ix]) - (upper_limit * upper_limit)  == distances[ix]:
            upper_limit -= 1

        answer = answer * (upper_limit - lower_limit + 1)
    
    end = perf_counter_ns()
    print(f'The answer is: {answer}')
    print(f'{((end-start)/1000000):.2f} milliseconds')

input_file = os.path.join(os.path.dirname(__file__), "input")
answer(input_file)
