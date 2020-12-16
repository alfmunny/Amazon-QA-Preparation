# heapify the array.
# pop the two smallest ones, connect them, and insert it back into the heap
# reapt that until there is only one rope.
from heapq import heappop, heappush, heapify

def solve(ropes):
  ans = 0
  heapify(ropes)

  while len(ropes) > 1:
    # pop the two smallest ones
    first = heappop(ropes)
    second = heappop(ropes)
    # connect and push back
    new = first + second
    heappush(ropes, new)
    ans += new

  return ans

print(solve([8, 4, 6, 12]))
print(solve([20, 4, 8, 2]))
print(solve([1, 2, 5, 10, 35, 89]))
print(solve([2, 2, 3, 3]))
