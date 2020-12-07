from os.path import isfile
from sys import argv
from array import array
import bisect

def bisection_search(data, target):
  """If taget exists in data, returns position in data else, returns None"""
  pos = bisect.bisect_left(data, target)
  if pos != len(data) and data[pos] == target:
    return pos

  return

def find_magic_number(input_path, needed_sum):
  """
  Checks to see if two numbers in 'input_path' sum to 'needed_sum'
  Returns the product if numbers exist, else returns None.
  """

  if not isfile(input_path):
    raise FileNotFoundError

  data = array('I')
  with open(input_path, 'r') as f:
    for line in f:
      cur = int(line)
      diff = needed_sum - cur

      pos = bisection_search(data, diff)
      if pos:
        return cur * diff

      bisect.insort(data, cur)

  return

def main():
  """
  Given a list of unsigned integers, check to see if there exists two numbers
  that sum to 2020 (default) or, an optional second input parameter. If such
  a number exists, reuturns the product of the two numbers.
  """
  if len(argv) not in [2, 3]:
    raise ValueError

  input_path = argv[1]

  if len(argv) == 3:
    needed_sum = argv[2]
  else:
    needed_sum = 2020

  result = find_magic_number(input_path, needed_sum=needed_sum)

  if result:
    print(result)
  else:
    print('Did not find two numbers that add to 2020!')

if __name__ == '__main__':
  main()
