n = 3

s = ['r',]
for i in range(n**2 - 1):
  s.append('e')
print(s)

r = 5
g = 5
m_made = 0
i = 1
prev_i = 1
while m_made <= n**2:
  if i = 0:
    r1 = r
    while r1 != 0:
      if s[prev_i] == 'e':
        r1 -= 1
      if prev_i = n**2 -1:
        prev_i = 0
      else:
        prev_i += 1
    s[prev_i] = 'r'
  else:
    g1 = g
    while g1 != 0:
      if s[prev_i] == 'e':
        g1 -= 1
      if prev_i = n**2 -1:
        prev_i = 0
      else:
        prev_i += 1
    s[prev_i] = 'g'
print(s)








