# Maintain a prefixSum, prefixSum[i] stores the total sum of asterisks before i, i inclusive
# A nearestLeftPipe[], nearestLeftPipe[i] stores the nearest left pipe of index i, i inclusive
# A nearestRightPipe[], nearestRightPipe[i] stores the nearest right pipe of index i, i inclusive
# prefixSum = [0, 1, 2, 2, 3, 3, 4]
# nearestLeftPipe = [0, 0, 0, 3, 3, 5, 5]
# nearestRightPipe = [0, 3, 3, 3, 5, 5, None]
# startIndices = [1, 1]
# endIndices = [5, 6]
# first = [1, 5], rightPipe = nearestRightPipe[start-1] = 0, leftPipe  = nearestLeftPipe[end-1] = 3
# result = prefixSum[3] - prefixSum[0] = 2 - 0 = 2
# second = [1, 6], rightPipe = nearestRightPipe[start-1] = 0, leftPipe  = nearestLeftPipe[end-1] = 5
# result = prefixSum[5] - prefixSum[0] = 3 - 0 = 3

def solve(s, startIndices, endIndices):
  prefixSum = getPrefixSum(s)
  nearestLeftPipe = getNearestLeftPipe(s)
  nearestRightPipe = getNearestRightPipe(s)
  ans = []
  for start, end in zip(startIndices, endIndices):
    if start < 1 or end > len(s):
      continue

    rightPipe = nearestRightPipe[start-1]
    leftPipe = nearestLeftPipe[end-1]

    if rightPipe < 0 or leftPipe < 0:
      continue
    ans.append(prefixSum[leftPipe] - prefixSum[rightPipe])
  return ans

def getPrefixSum(s):
  ans = []
  count = 0
  for i in range(len(s)):
    if s[i] == "*":
      count += 1
    ans.append(count)

  return ans

def getNearestLeftPipe(s):
  ans = []
  leftIndex = -1
  for i in range(len(s)):
    if s[i] == "|":
      leftIndex = i
    ans.append(leftIndex)
  return ans

def getNearestRightPipe(s):
  ans = []
  rightIndex = -1

  for i in range(len(s)-1, -1, -1):
    if s[i] == "|":
      rightIndex = i
    ans.insert(0, rightIndex)
  return ans

print(solve("|**|*|*", [1, 1], [5, 6]))
print(solve("*|*|", [1, 2], [3, 4]))
