from sys import argv
from os.path import isfile


def count_valid_passwords(input_path):
  """
  Counts the number of entries in the input list of the form:
    min-max char: string
  that follow:
    string.count(char) >= min and string.count(char) <= max
  """
  if not isfile(input_path):
    raise FileNotFoundError

  n_valid = 0
  with open(input_path, 'r') as f:
    for line in f:
      rules, password = line.split(': ')
      rules = rules.split(' ')
      char = rules[-1]
      char_min = int(rules[0].split('-')[0])
      char_max = int(rules[0].split('-')[1])

      char_count = password.count(char)
      if char_count >= char_min and char_count <= char_max:
        n_valid += 1

  return n_valid


def main():
  if len(argv) != 2:
    raise TypeError

  input_path = argv[1]
  try:
    result = count_valid_passwords(input_path)
  except Exception as e:
    print('Failed to count number of valid passwords!')
    raise e

  print(result)

if __name__ == '__main__':
  main()
