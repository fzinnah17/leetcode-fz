"""Problem Statement: 

Given an array of integers, find the first element that occurs more than once. If no such element exists, return -1.

Example:

Input: [3, 5, 7, 9, 3, 2, 5, 5, 7, 9, 2]
Output: 3
"""


def repeatedElements(input):
  input_dict = {}
  for el in input:
    if el not in input_dict:
      input_dict[el] = 1
    else:
      input_dict[el] += 1
  dictKeys = list(input_dict.keys())
  return dictKeys[0]
    

def main():
  input = [3, 5, 7, 9, 3, 2, 5, 5, 7, 9, 2]

  first_key = repeatedElements(input)

  # Use the first key in your code as needed
  print(first_key)

if __name__ == '__main__':
  main()
