from sys import argv
from os.path import isfile


def count_valid_passwords(input_path):
  """
  Counts the number of entries in the input list of the form:
    pos1-pos2 char: string
  that follow:
    string[pos1-1] == char xor string[pos-1] == char
  """
  if not isfile(input_path):
    raise FileNotFoundError

  n_valid = 0
  with open(input_path, 'r') as f:
    for line in f:
      rules, password = line.split(': ')
      print(password)
      rules = rules.split(' ')
      char = rules[-1]
      pos1 = int(rules[0].split('-')[0]) - 1
      pos2 = int(rules[0].split('-')[1]) - 1

      print(rules, pos1, password[pos1], pos2, password[pos2])
      if (password[pos1] == char) != (password[pos2] == char):
        print('valid')
        n_valid += 1

  return n_valid


def main():
  if len(argv) != 2:
    raise TypeError

  input_path = argv[1]
  try:
    result = count_valid_passwords(input_path)
  except FileNotFoundError:
    print('Input file does not exist!')
    raise e
  except Exception as e:
    print('Failed to count number of valid passwords!')
    raise e

  print(result)

if __name__ == '__main__':
  main()
