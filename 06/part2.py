from sys import argv
from os.path import isfile
from typing import List

def get_common(data: List[str]):
  """
  Given a list of strings, return string containing characters
  that are unique to all strings in the list  
  """
  if not len(data):
    return ''

  common = set(data[0])
  for i in range(1, len(data)):
    common = common.intersection(data[i])
  return ''.join(common)

def get_data(input_path):
  """
  Load key value pairs from file
  Each instance is seperated by a blank line
  Each key value is seperated by either a line break or space
  Return a list of dictionaries
  """
  if not isfile(input_path):
    raise FileNotFoundError

  data = []
  with open(input_path, 'r') as f:
    lines = []
    for line in f:
      line = line.strip()
      # blank line marks end of insatnce
      if not line:
        data.append(get_common(lines))
        lines.clear()
      else:
        lines.append(line) 

    # add last entry
    if lines:
      data.append(get_common(lines))

  return data

def main():
  """
  """
  if len(argv) != 2:
    raise TypeError

  input_path = argv[1]

  # return a list of strings representing answers common to all mebers of group
  data = get_data(input_path)

  len_ans = [len(d) for d in data]
  sum_len_ans = sum(len_ans)

  print('The sum of the common answers per group is {}'.format(sum_len_ans))

if __name__ == '__main__':
  main()
