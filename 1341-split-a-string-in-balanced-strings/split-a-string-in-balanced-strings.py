class Solution:
  def balancedStringSplit(self, s: str) -> int:
    ans = 0
    curr = 0

    for l in s:
      curr += 1 if l == 'R' else -1
      ans += curr == 0

    return ans