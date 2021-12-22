class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        len_a, len_b = len(a), len(b)
        lo, hi = 0, len_b//len_a+3  # upper bound of repeated time is len_b//len_a+2, therefore, the upper bound of bi-search is len_b//len_a+3
        flag = 0
        while lo < hi:
            mid = (lo+hi)//2
            if b in mid * a:
                hi = mid
                flag = 1
            else:
                lo = mid + 1
        if not flag:
            return -1
        return hi

'''
RESULT:
执行用时：
160 ms
, 在所有 Python3 提交中击败了
56.82%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
52.73%
的用户
通过测试用例：
57 / 57
'''

'''
其实中间的字符串匹配部分可以换成KMP算法，但是我现在还不太会写 ^ ^
'''
