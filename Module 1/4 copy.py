def swap(a, b):
  n_a = b[:2] + a[2:]
  n_b = a[:2] + b[2:]

  return n_a + ' ' + n_b
print(swap('abc', 'xyz'))
