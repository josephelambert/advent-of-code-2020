from sys import argv
from os.path import isfile
from typing import List

def create_dict(input_list: List[str],
                bound=':'):
  """
  Splits each item in list by split_char
  The first half is used as key in dict pair
  The second half is used as value in dict pair
  """
  return {itm.split(bound)[0]:itm.split(bound)[1] for itm in input_list}
  

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
    datum = []
    for line in f:
      # blank line makrs end of insatnce
      if line == '\n' and datum:
        # create dictionary of key value pairs and add to list
        data.append(create_dict(datum))
        datum.clear()
      else:
        # collect key value pairs for this line
        datum.extend(line.strip().split(' '))

    # add last entry
    if datum:
      data.append(create_dict(datum))

  return data

def count_valid_ids(data: dict, required_fields: set):
  """For each instance, make sure that all required fields are present"""
  n_required_fields = len(required_fields)
  n_valid = 0
  for datum in data:
    if len(datum) < n_required_fields:
      continue
    if required_fields.issubset(datum.keys()):
      n_valid += 1

  return n_valid

def main():
  """
  Reads in a list of key value pairs 
  Counts the number of ids that include all necessary fields.
  Necessary fields include:
    -byr (Birth Year)
    -iyr (Issue Year)
    -eyr (Expiration Year)
    -hgt (Height)
    -hcl (Hair Color)
    -ecl (Eye Color)
    -pid (Passport ID)
  Optional fileds include:
    -cid (Country ID)
  """
  required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

  if len(argv) != 2:
    raise TypeError

  input_path = argv[1]

  data = get_data(input_path)

  n_valid = count_valid_ids(data, required_fields)

  print('The number of ids with all required fields is %s' % n_valid)

if __name__ == '__main__':
  main()
