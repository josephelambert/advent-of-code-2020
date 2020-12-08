from sys import argv
from os.path import isfile

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
    chars = set()
    for line in f:
      # blank line makrs end of insatnce
      if line == '\n' and chars:
        # concatenate uniaue characters into a string
        data.append(''.join(chars))
        chars.clear()
      else:
        # collect key value pairs for this line
        for char in line.strip():
          chars.add(char)

    # add last entry
    if chars:
      data.append(''.join(chars))

  return data

def main():
  """
  """
  if len(argv) != 2:
    raise TypeError

  input_path = argv[1]

  data = get_data(input_path)

  sum_answer_length = sum([len(d) for d in data])

  print('The total unique number of questioned answered by all groups is {}'\
        .format(sum_answer_length))

if __name__ == '__main__':
  main()
