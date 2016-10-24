def answer(data, n):
  iMap = {};
  for idx, val in enumerate(data):

    if val in iMap:
      iMap[val].append(idx)
    else:
      iMap[val] = [idx]

  ret = []
  for val in data:
    indices = iMap[val]
    if len(indices)<=n:
      ret.append(val)

  return ret



print answer([5, 10, 15, 10, 7], 1);

print answer([1, 2, 3], 0);

print answer([1, 2, 2, 3, 3, 3, 4, 5, 5], 1);

print answer([1, 2, 3], 6);

