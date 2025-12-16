def find_even_numbers(lst):
  even_list = []
  for item in lst:
    if item%2==0:
      even_list.append(item)
  return even_list
