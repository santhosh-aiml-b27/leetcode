class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            rev = -int(str(-x)[::-1])
        else:
            rev = int(str(x)[::-1])

        if abs(rev) > 2147483647:
            return 0

        return rev