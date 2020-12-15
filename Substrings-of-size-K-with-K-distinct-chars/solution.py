# Sliding Window
# Keep a window of size k, and a counter for the window.
from collections import Counter
def solve(s, k):
  left, right = 0, 0
  window = Counter()
  dic = set()
  ans = []

  while right < len(s) and right - left+1 <= k:
    while right < len(s) and right - left + 1 <= k:
      window[s[right]] += 1
      if right - left + 1 == k and len(window) == k:
        w = s[left:right+1]
        if w not in dic:
          dic.add(w)
          ans.append(s[left:right+1])
      right += 1

    window[s[left]] -= 1
    if window[s[left]] == 0:
      window.pop(s[left])
    left += 1

  return ans

print(solve("awaglknagawunagwkwagl", 4))

"""
Input: s = "abcabc", k = 3
Output: ["abc", "bca", "cab"]
Example 2:

Input: s = "abacab", k = 3
Output: ["bac", "cab"]
Example 3:

Input: s = "awaglknagawunagwkwagl", k = 4
Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
Explanation:
Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag", "wagl" 
"wagl" is repeated twice, but is included in the output once.
"""
