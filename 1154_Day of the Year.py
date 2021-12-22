class Solution:
    def dayOfYear(self, date: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])
        # identify leap year
        if year%4 == 0 and year%100 != 0:
            months[1] += 1
        elif year%400 == 0:
            months[1] += 1
        cnt = 0
        for i in range(month-1):
            cnt += months[i]
        return cnt + day
'''
简单的打表题，昨天家里停电没做，今天补上来

'''
