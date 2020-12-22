#!/usr/bin/python3

#import decimal

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

if __name__ == "__main__":

  d = loop_count_add(1, 100, 1, 1)
  print(d)

  e = loop_count_add(1, 100, 0.01, 0.01)
  print(e)

