N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

def calc(B):
  i, j, countX, countY, res = 0, 0, 0, 0, 0
  while i != len(B):
      #XとYが見つかっていなければloop
      #片方が０ならloopする
    while j != len(B) and (countX == 0 or countY == 0):
        #もしXがみつかったら
      if B[j] == X:
        countX += 1
        #もしYがみつかったら
      if B[j] == Y:
        countY += 1

      j += 1
    #どちらも見つかったらその区間は条件を満たしている
    if countX > 0 and countY > 0:#どっちも見つかっていれば
        
      res += len(B) + 1 - j#手前側までの数字を足す

      
    if B[i] == X:
      countX -= 1
    if B[i] == Y:
      countY -= 1
    i += 1
  return res


i, ans = 0, 0
while i != N:
  B = []
  while i != N and Y <= A[i] <= X:
    B.append(A[i])
    i += 1
  if len(B) != 0:
    ans += calc(B)
  else:
    i += 1
print(ans)
