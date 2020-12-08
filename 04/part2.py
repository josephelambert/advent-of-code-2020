from sys import argv
from os.path import isfile
from typing import List
from re import search

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

# TODO: replace datum with list of named tuples
def pass_require(data):
  """
  Check hardcoded requirments on id fields:
    -byr (Birth Year) - four digits; at least 1920 and at most 2002.
    -iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    -eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    -hgt (Height) - a number followed by either cm or in:
         If cm, the number must be at least 150 and at most 193.
         If in, the number must be at least 59 and at most 76.
    -hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    -ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    -pid (Passport ID) - a nine-digit number, including leading zeroes.
    -cid (Country ID) - ignored, missing or not.
  """
  valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
  hair_color_pattern = '^#(?:[0-9a-f]{3}){1,2}$'
  byr_min, byr_max = 1920, 2002
  iyr_min, iyr_max = 2010, 2020
  eyr_min, eyr_max = 2020, 2030
  hgt_in_min, hgt_in_max = 59, 76
  hgt_cm_min, hgt_cm_max = 150, 193

  # check birth year (byr): if not int, will raise ValueError
  n_digits = len(data['byr'])
  byr = int(data['byr'])
  if n_digits != 4 or byr < byr_min or byr > byr_max:
    return False

  # check issue year (iyr): if not int, will raise ValueError
  n_digits = len(data['iyr'])
  iyr = int(data['iyr'])
  if n_digits != 4 or iyr < iyr_min or iyr > iyr_max:
    return False

  # check expiration year (eyr): if not int, will raise ValueError
  n_digits = len(data['eyr'])
  eyr = int(data['eyr'])
  if n_digits != 4 or eyr < eyr_min or eyr > eyr_max:
    return False

  # check height (hgt)
  hgt_unit = data['hgt'][-2:]
  hgt = int(data['hgt'][:-2])
  if hgt_unit == 'in':
    if hgt < hgt_in_min or hgt > hgt_in_max:
      return False
  elif hgt_unit == 'cm':
    if hgt < hgt_cm_min or hgt > hgt_cm_max:
      return False
  else:
    return False

  # check hair color (hcl)
  if not search(hair_color_pattern, data['hcl']):
    return False

  # check eye color (ecl)
  if data['ecl'] not in valid_eye_colors:
    return False

  # check passport ID (pid): if not int, will raise ValueError
  if len(data['pid']) != 9 or int(data['pid']) < 0:
    return False

  return True  

def count_valid_ids(data: dict, required_fields: set):
  """For each instance, make sure that all required fields are present"""
  n_required_fields = len(required_fields)
  n_valid = 0
  for datum in data:
    # meets required number of fields
    if len(datum) < n_required_fields:
      continue
    # validates that required fields are present
    if not required_fields.issubset(datum.keys()):
      continue

    # check to make sure instances are valid
    try:
      pass_req = pass_require(datum)
    except Exception as e:
      continue

    if pass_req:
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

  Requirments on each field:
    -byr (Birth Year) - four digits; at least 1920 and at most 2002.
    -iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    -eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    -hgt (Height) - a number followed by either cm or in:
         If cm, the number must be at least 150 and at most 193.
         If in, the number must be at least 59 and at most 76.
    -hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    -ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    -pid (Passport ID) - a nine-digit number, including leading zeroes.
    -cid (Country ID) - ignored, missing or not.
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
