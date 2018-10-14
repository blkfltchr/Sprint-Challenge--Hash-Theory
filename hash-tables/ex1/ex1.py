def get_indices_of_item_weights(weights, limit):

  # hash_table = { i : weights[i] for i in range(0, len(weights) ) } 
  # hash_table2 = {y:x for x,y in hash_table.items()}

  # for weight in hash_table2:
  #   try:
  #     twoWeights = hash_table2[limit-weight]
  #     return (hash_table2[limit-weight], hash_table2[weight])
  #   except KeyError: 
  #     print('Try again...')

  hash_table = { weights[i] : i for i in range(len(weights)) }
  
  for i in range(len(weights)):
    try:
      return (hash_table[limit-weights[i]], i)
    except KeyError:
      pass

  return ()

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  print(get_indices_of_item_weights([4,6,10,15,16], 21))
  print(get_indices_of_item_weights([4, 4], 8), (1, 0))
  print(get_indices_of_item_weights([4, 6, 10, 15, 16], 21), (3, 1))
  print(get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 7), (6, 2))
  # print(get_indices_of_item_weights([9], 9), ())