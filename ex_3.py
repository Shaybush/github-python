def is_copy_k(s1, s2):
  k = 0
  count = 0
  if len(s1) % len(s2) != 0:
    return 0
  for i in range(len(s1)):
    if s2[i % len(s2)] == s1[i]:
      count += 1
    else:
      return 0

    if count == len(s2):
      k += 1
      count = 0
  return k

print(is_copy_k("ababababab", "ab"))
