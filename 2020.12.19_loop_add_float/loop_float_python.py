#!/usr/bin/python3

from decimal import Decimal
import math

def loop_count_add(counter_start, counter_end, a, b):
    """
    """

    list = []

    while counter_start <= counter_end:
        #print(a)
        list.append(a)
        a = a + b

        counter_start+=1

    return list

def loop_count_add_decimal(counter_start, counter_end, a, b):
    """
    """

    list = []

    while counter_start <= counter_end:
        #print(a)
        list.append(float('{:1}'.format(a)))
        a = Decimal(str(a))+Decimal(str(b))

        counter_start+=1
        
    return list

def loop_count_add_math(counter_start, counter_end, a, b):
    """
    """

    list = []
    
    while counter_start <= counter_end:
        #print(a)
        list.append(a)
        a = math.floor(a + b)

        counter_start+=1

    return list


if __name__ == "__main__":

  d = loop_count_add(1, 100, 1, 1)
  print(d)

  e = loop_count_add(1, 100, 0.01, 0.01)
  print(e)

  f = loop_count_add_decimal(1, 100, 0.01, 0.01)
  print(f)

  g = loop_count_add_math(1, 100, 0.01, 0.01)
  print(g)


