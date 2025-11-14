import sys
input = sys.stdin.readline

T = int(input())
for test_case in range(1, T+1):
  n = float(input())
  isAns = False
  ans = ""
  for i in range(1, 13):
    minus = 2 ** ((-1) * i)
    if n > minus:
      n -= minus
      ans += "1"
    elif n < minus:
      ans += "0"
    elif n == minus:
      print('#' + str(test_case) + ' ' + ans + "1")
      isAns = True
  if isAns == False:
    print('#' + str(test_case) + ' ' + 'overflow')
  
