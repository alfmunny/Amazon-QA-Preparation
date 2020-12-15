from heapq import heappush, heappop
def fiveStarReviews(productRatings, threshold):
  heap = []
  current_perc = 0

  for ratings in productRatings:
    improvement = get_improvement(ratings[0], ratings[1])
    heappush(heap, [-improvement, ratings[0], ratings[1]])
    current_perc += ratings[0] / ratings[1]
  current_perc /= len(productRatings)

  ans = 0

  while current_perc <= threshold:
    first, second = heappop(heap)[1:]
    improvement = get_improvement(first, second)
    current_perc += improvement / len(productRatings)
    improvement = get_improvement(first+1, second+1)
    heappush(heap, [-improvement, first+1, second+1])
    ans += 1
  return ans

def get_improvement(r1, r2):
  return (r1+1) / (r2+1) - r1/r2

print(fiveStarReviews([[4,4], [1,2], [3, 6]], 0.77))
