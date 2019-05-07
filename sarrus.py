#!/usr/bin/env python
import sys

first_vector  = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]
second_vector = [int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])]
third_vector  = [int(sys.argv[7]), int(sys.argv[8]), int(sys.argv[9])]

sarrus = ((first_vector[0] * second_vector[1] * third_vector[2]) + (first_vector[1] * second_vector[2] * third_vector[0]) + (first_vector[2] * second_vector[0] * third_vector[1])) - ((first_vector[2] * second_vector[1] * third_vector[0]) + (first_vector[1] * second_vector[0] * third_vector[2]) + (first_vector[0] * second_vector[2] * third_vector[1]))

print(sarrus)
