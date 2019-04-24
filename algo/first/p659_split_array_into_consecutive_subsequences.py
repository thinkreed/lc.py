from collections import Counter


class Solution:
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last = float('-inf')
        one_count = 0
        two_count = 0
        multy_count = 0

        end_one = 0
        end_two = 0
        end_multy = 0

        appears = Counter(nums)

        for num, appear in appears.items():

            if num != last + 1:
                if one_count != 0 or two_count != 0:
                    return False
                end_one = appear
                end_two = 0
                end_multy = 0
            else:
                if appear < (one_count + two_count):
                    return False
                end_one = max(0, appear - (one_count + two_count + multy_count))
                end_two = one_count
                end_multy = two_count + min(multy_count, appear - (one_count + two_count))
            last = num
            one_count = end_one
            two_count = end_two
            multy_count = end_multy

        return one_count == 0 and two_count == 0
