from collections import defaultdict

def solve(maxTravelDist, forwardRouteList, returnRouteList):
  fList = sorted(forwardRouteList, key=lambda x: x[1])
  rList = sorted(returnRouteList, key=lambda x: x[1])

  lp, sp = 0, len(rList) - 1
  ans = defaultdict(list)
  maxOptimized = 0

  while lp < len(fList) and sp >= 0:
    dis = forwardRouteList[lp][1] + returnRouteList[sp][1]
    if dis <= maxTravelDist:
        ans[dis].append([forwardRouteList[lp][0], returnRouteList[sp][0]])
        maxOptimized = max(maxOptimized, dis)
        lp += 1
    else:
      sp -= 1

  return ans[maxOptimized]

print(solve(7000, [[1,2000], [2,4000], [3,6000]], [[1,2000]]))
print(solve(10000, [[1,3000], [2,5000], [3,7000], [4,10000]], [[1,2000], [2,3000], [3,4000], [4,5000]]))
