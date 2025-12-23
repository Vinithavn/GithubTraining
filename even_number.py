def find_even_numbers(lst):
  new_list = []
  for i in lst:
    if i % 2 == 0:
      new_list.append(i)
  print("Removing a messy commit 2")
  a="commit 1"
  return new_list

if __name__ == "__main__":
  sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  print("Even numbers in the list:", find_even_numbers(sample_list))
