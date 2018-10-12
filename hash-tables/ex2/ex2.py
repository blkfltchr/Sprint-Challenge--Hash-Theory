def reconstruct_trip(tickets):

  hash_table = {}
  
  route = []
  
  for ticket in tickets:
    hash_table[ticket[0]] = ticket[1]
  
  current = hash_table[None]
  
  while current is not None:
    route.append(current)
    if current in hash_table:
      current = hash_table[current]
  return route

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  tickets = [
    ('PIT', 'ORD'),
    ('XNA', 'CID'),
    ('SFO', 'BHM'),
    ('FLG', 'XNA'),
    (None, 'LAX'), 
    ('LAX', 'SFO'),
    ('CID', 'SLC'),
    ('ORD', None),
    ('SLC', 'PIT'),
    ('BHM', 'FLG'),
  ]
  print(reconstruct_trip(tickets))
