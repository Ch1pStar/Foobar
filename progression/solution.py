import math

def answer(total_lambs):
  return communism(total_lambs) - capitalism(total_lambs)

def communism(n):
  cnt = 1;
  fibN =  fib(cnt);
  sm = fibN;

  while((fib(cnt)+sm)<n):
    cnt+=1;
    fibN =  fib(cnt);
    sm += fibN;

  return cnt;


def capitalism(n):
  a1 = 1
  cnt = 2
  handout = a1*math.pow(2,cnt-1);
  sc = a1 + handout

  while ((sc+a1*math.pow(2,cnt)) <= n):
    handout = a1*math.pow(2,cnt);
    sc += handout;
    cnt+=1;

  return cnt

def fib(n):
  if n < 2:
    return n

  phi = (1 + math.sqrt(5)) / 2.
  return int((math.pow(phi,n) - math.pow(1-phi,n))/math.sqrt(5));


print answer(10) #1
print answer(143) #3
print answer(10**9) #3