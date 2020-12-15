# We need to sort the keywords according to their frequency and their lexicical order.
# A Hashmap can store the frequency and retrieve it in O(1). We can use it to count the frequency for all keywords.
# A Priority Queue can use keys to maintain an order while adding or deleting new items. We can use it to sort all keys.
# 1. Go through the list Build a hashmap to count the frequency
# 2. Go through all the keys in the Hashmap and add them into a Heap.
# 3. Return the first k keywords.
from heapq import heappush
from collections import defaultdict

def solve(keywords, reviews, k):
  # Build Hashmap
  freq = defaultdict(int)
  keywords = set(keywords)
  for review in reviews:
    for w in review.split(" "):
      if w.lower() in keywords:
        freq[w.lower()] += 1

  # Build heap
  items = list(freq.items())

  items.sort(key=lambda x: (-x[1], x[0]))
  return [item[0] for item in items[:k]]

k = 2
keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]
print(solve(keywords, reviews, k))
