from os.path import isfile
from sys import argv
from array import array
import bisect

def get_data(input_path):
  """load data into array('I') from input_path"""
  with open(input_path, 'r') as f:
    return array('I', [int(i) for i in f])

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

  # load and sort input data
  data = sorted(get_data(input_path))
  data_min = min(data)

  for i in range(0, len(data)-1):
    for j in range(i, len(data)):
      diff = needed_sum - data[i] - data[j]

      # if diff is less than min, no point checking
      if diff < data_min:
        continue

      # check to see if needed number exists
      pos = bisection_search(data, diff)

      if pos:
        return diff * data[i] * data[j]

  return

def main():
  """
  Given a list of unsigned integers, check to see if there exists three numbers
  that sum to 2020 (default) or, an optional second input parameter. If such
  a numbera exists, reuturns the product of the three numbers.
  """
  if len(argv) not in [2, 3]:
    print('Usage: python %s input path [sum to look for]' % argv[0])
    raise TypeError

  input_path = argv[1]

  if len(argv) == 3:
    needed_sum = int(argv[2])
  else:
    needed_sum = 2020

  result = find_magic_number(input_path, needed_sum=needed_sum)

  if result:
    print(result)
  else:
    print('Did not find three numbers that add to 2020!')

if __name__ == '__main__':
  main()
