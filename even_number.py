def return_even_numbers(lst):
  return [num for num in lst if num % 2 == 0]

if __name__ == "__main__":
  sample_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 110]
  print("Even numbers in the list:", find_even_numbers(sample_list))
