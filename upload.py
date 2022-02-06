import time


a = 11
b = 22
print(a + b)

with open('out.txt', 'w') as fout:
  fout.write('{}\n'.format(time.time()))
  fout.write('{}'.format(a + b))
