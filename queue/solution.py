def answer(start, length):
  end = length*length;
  i = 0
  line = length
  group_start = start
  res = 0
  while(line>0):
    i=0
    while(i<line):
      res = res^(group_start+i)
      i+=1

    group_start += length
    line-=1

  return res



print answer(17,4)
print answer(0,3)