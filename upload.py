a = 1
b = 2
print(a + b)

with open('out.txt', 'w') as fout:
  fout.write('{}'.format(a + b))
