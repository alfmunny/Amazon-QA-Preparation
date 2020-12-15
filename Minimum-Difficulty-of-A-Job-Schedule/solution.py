class Solution:
  def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
    if len(jobDifficulty) < d:
      return -1
    self.h = {}

    return self.dfs(jobDifficulty, 0, d)

  def dfs(self, arr, index, days):

    if days == 1:
      return max(arr[index:])

    if (index, days) in self.h:
      return self.h[(index, days)]

    cur_max, ans = 0, float('inf')

    for i in range(index, len(arr) - 1):
      cur_max = max(cur_max, arr[i])
      ans = min(ans, cur_max+self.dfs(arr, i+1, days-1))

      self.h[(index, days)] = ans
      return ans
