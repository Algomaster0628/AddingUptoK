def addToK(n,k): # Returns numbers which adds upto K using greedy algorithm.
  x = 0
  y = len(n) - 1
  while y != 0:
    if n[x] + n[y] == k:
      return str(n[x]) + " and " + str(n[y]) + " adds up to K."
    elif n[x] + n[y] > k:
      y -= 1
    elif n[x] + n[y] < k:
      x += 1
  y -= 1
z = addToK([2,3,4,5],9)
print(z)
