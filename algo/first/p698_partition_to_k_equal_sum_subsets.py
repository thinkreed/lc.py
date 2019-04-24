class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if nums is None or len(nums) == 0 or k == 0:
            return False

        nums = sorted(nums)

        sumary = sum(nums)

        if sumary % k != 0 or sumary < k:
            return False

        target = sumary // k

        def dfs(visited, index):
            if index == -1:
                for s in visited:
                    if s != target:
                        return False
                return True

            num = nums[index]

            for i in range(len(visited)):
                if visited[i] + num <= target:
                    visited[i] += num
                    if dfs(visited, index - 1):
                        return True
                    visited[i] -= num

            return False

        return dfs([0] * k, len(nums) - 1)

    def can_partition_k_subsets(self, nums, k):
        target, remain = divmod(sum(nums), k)
        if remain or max(nums) > target:
            return False
        n = len(nums)
        visited = [0] * n
        nums.sort(reverse=True)

        def dfs(k, index, current_sum):
            if k == 1:
                return True

            if current_sum == target:
                return dfs(k - 1, 0, 0)
            for i in range(index, n):
                if not visited[i] and current_sum + nums[i] <= target:
                    visited[i] = 1
                    if dfs(k, i + 1, current_sum + nums[i]):
                        return True
                    visited[i] = 0
            return False

        return dfs(k, 0, 0)
