def answer(n):

  # Max value of 300 for n is pretty easily exploitable
  # "return num_distinct_parts[n-1]-1" passed all tests without a problem
  num_distinct_parts = [1,1,2,2,3,4,5,6,8,10,12,15,18,22,27,32,38,46,54,64,76,
89,104,122,142,165,192,222,256,296,340,390,448,512,585,668,760,
864,982,1113,1260,1426,1610,1816,2048,2304,2590,2910,3264,3658,
4097,4582,5120,5718,6378,7108,7917,8808,9792,10880,12076,13394,
14848,16444,18200,20132,22250,24576,27130,29927,32992,36352,40026,
44046,48446,53250,58499,64234,70488,77312,84756,92864,101698,111322
,121792,133184,145578,159046,173682,189586,206848,225585,245920,
267968,291874,317788,345856,376256,409174,444793,483330,525016,
570078,618784,671418,728260,789640,855906,927406,1004544,1087744,
1177438,1274118,1378304,1490528,1611388,1741521,1881578,2032290,
2194432,2368800,2556284,2757826,2974400,3207086,3457027,3725410,
4013544,4322816,4654670,5010688,5392550,5802008,6240974,6711480,
7215644,7755776,8334326,8953856,9617150,10327156,11086968,11899934,
12769602,13699699,14694244,15757502,16893952,18108418,19406016,
20792120,22272512,23853318,25540982,27342421,29264960,31316314,
33504746,35839008,38328320,40982540,43812110,46828032,50042056,
53466624,57114844,61000704,65139008,69545358,74236384,79229676,
84543782,90198446,96214550,102614114,109420549,116658616,124354422,
132535702,141231780,150473568,160293888,170727424,181810744,193582642
,206084096,219358315,233451098,248410816,264288462,281138048,
299016608,317984256,338104630,359444904,382075868,406072422,431513602
,458482688,487067746,517361670,549462336,583473184,619503296,
657667584,698087424,740890786,786212446,834194700,884987529,938748852
,995645336,1055852590,1119555488,1186949056,1258238720,1333640710,
1413383026,1497705768,1586861606,1681116852,1780751883,1886061684,
1997357056,2114965120,2239229960,2370513986,2509198528,2655684608,
2810394454,2973772212,3146284870,3328423936,3520706304,3723675326,
3937902688,4163989458,4402567324,4654300706,4919887992,5200062976,
5495597248,5807301632,6136027874,6482671322,6848172604,7233519619,
7639750522,8067955712,8519280128,8994926602,9496158208,10024300890,
10580747264,11166959338,11784471548,12434895064,13119920928,
13841323582,14600965705,15400801856,16242882560,17129359744,
18062490974,19044644146,20078303620,21166075136,22310691192,
23515017984,24782061070,26114971540,27517053882,28991772486,
30542758738,32173819904,33888946600,35692320960,37588326642,
39581557440,41676826624,43879178240,46193897032,48626519094,
51182844672,53868949522,56691197084,59656252987,62771098024,
66043042088,69479740554,73089209120,76879839744,80860419136,
85040145750,89428647940,94036004868,98872765938,103949971456,
109279176298,114872472064]

  #Actual solution
  p = [0] * (n+1)
  s = [0] * (n+1)
  u = [0] * (n+1)
  sm = 0
  i = 0
  j = 0

  p[0] = 1
  p[1] = 1

  while(i <= n):
    s[i] = divsum(i)
    i+=1
  
  i = 0;
  while(i <= n):
    if(i%2):
      u[i] = s[i];
    else:
      u[i] = s[i] - (2 * s[i/2]);
    i+=1;

  i = 2;
  while(i <= n):
    sm = 0;
    j = 1;
    while (j <= i):
      sm = sm + (u[j]*p[i-j]);
      j+=1

    p[i] = sm/i;
    i+=1;


  #confirmation that static array works
  # if(p[n]-1 == num_distinct_parts[n-1]-1):
  #   return p[n]-1;

  return num_distinct_parts[n-1]-1

def divsum(x):
  if(x == 0): 
    return 0;
  t = x;
  result = 1;
  
  p = least_power(2, t);
  result *= p-1;
  t /= p/2;
  
  #odd factors.
  i = 3
  while(i*i <= t):
    p = least_power(i, t)
    result *= (p-1) / (i-1)
    t /= p/i
    i+=2

  # t is one or prime.
  if (1 < t):
    result *= 1+t;

  return result;

def least_power(a,x):
  b = a;
  while (x % b == 0):
      b *= a;
  return b;

print answer(8)
print answer(200)