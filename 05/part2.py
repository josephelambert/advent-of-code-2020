from sys import argv
from os.path import isfile

def get_data(input_path):
  """Loads data from text file into list"""
  if not isfile(input_path):
    raise FileNotFoundError

  with open(input_path, 'r') as f:
    return [line.strip() for line in f]

def binary_part(data: str, c: str):
  """
  Binary partition

  Assumes that each character in the string represents a binary digit of a
  binary number

  Assumes that the string is made up of a 'forward' character and a 'backwards'
  character.

  Converts string into an integer based on binary partition
  """
  row_min, row_max = 0, 2**len(data) - 1
  for char in data:
    diff = row_max - row_min
    quotient, remainder = divmod(diff, 2)
    if char == c:
      row_max -= quotient + remainder
    else:
      row_min += quotient + remainder

  assert row_min == row_max
  return row_min

def decode(data):
  """
  first 7 chars are row
  last 3 are column
  """
  row = binary_part(data[:7], 'F')
  col = binary_part(data[7:], 'L')

  return row, col

def seat_id(row, col):
  """Calculates the row ID given the seat column and the seat row"""
  return row * 8 + col

def find_missing(data):
  """
  Find missing value using a binary search
  """
  data = sorted(data)
  data_min, data_max = data[0], data[-1]
  idx_min, idx_max = 0, len(data) - 1

  while True:
    # get index at central point
    idx_diff = idx_max - idx_min
    idx_test = idx_min + idx_diff // 2 + idx_diff % 2

    # get expected data value at central point
    data_diff = data_max - data_min
    data_test = data_min + data_diff // 2 + data_diff % 2

    if data[idx_test] == data_test:
      # missing value is to the left
      idx_max = idx_test
      data_max = data_test
    elif data[idx_test] < data_test:
      # missing value is to the right
      idx_min = idx_test
      data_min = data_test

    if idx_min + 1 == idx_max:
      if data[idx_min] == data[idx_max]:
        # no missing values
        return -1
      else:
        # missing value located
        return data[idx_min] + 1

def main():
  """
  Reads in data from a text file
  Converts each entry to a seat columna and a seat row
  Converts each seat column/row to a seat ID
  """
  if len(argv) != 2:
    raise TypeError

  input_path = argv[1]

  # read data into list
  data = get_data(input_path)

  # convert each value into a tuple (row, col)
  decoded = [decode(d) for d in data]

  # convert (row, col) to row ID (row * 8 + col)
  seat_ids = [seat_id(*x) for x in decoded]

  # find missing seat ID
  seat_id_missing = find_missing(seat_ids)

  print('Your seat ID is %s' % seat_id_missing)

if __name__ == '__main__':
  main()
