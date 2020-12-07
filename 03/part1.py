from sys import argv, exit
from os.path import isfile

def get_map(input_path):
  """Open input parh and load into 2D array"""
  if not isfile(input_path):
    raise FileNotFoundError

  tree_map = []
  with open(input_path, 'r') as f:
    for line in f:
      tree_map.append(line.strip())

  return tree_map
      
def get_n_trees(tree_map, right, down):
  """Given input and slope (right and down), count how many '#'s there are"""

  # the map is cyclic, the map repeats every n_lines
  n_lines = len(tree_map[0])

  # we need to travel from 0 to n_rows
  n_rows = len(tree_map)

  # number of trees in the way 
  n_trees = 0

  # starting point
  loc = 0
  for i in range(down, n_rows, down):
    loc = (loc + right) % n_lines
    if tree_map[i][loc] == '#':
      n_trees += 1

  return n_trees

def main():
  """Given input and slope (right and down), count how many '#'s there are"""
  if len(argv) not in [2, 4]:
    print('Usage: python %s input.txt' % argv[0])
    exit()

  input_path = argv[1]

  if len(argv) == 4:
    right, down = int(argv[2]), int(argv[3])
  else:
    right, down = (3, 1)

  # load data into 2D array (map)
  tree_map = get_map(input_path)

  # count the number of '#'s (trees) that you encounter along you trip
  result = get_n_trees(tree_map, right, down)

  print('During your travel South, you encounter %s trees.' % result)

if __name__ == '__main__':
  main()
