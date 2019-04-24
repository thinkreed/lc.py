class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = [0] * 26
        maximum = 0
        max_count = 0
        ord_A = ord('A')

        for task in tasks:
            ord_task = ord(task)
            counter[ord_task - ord_A] += 1
            if maximum == counter[ord_task - ord_A]:
                max_count += 1
            elif maximum < counter[ord_task - ord_A]:
                maximum = counter[ord_task - ord_A]
                max_count = 1

        part_count = maximum - 1
        part_length = n - (max_count - 1)
        empty_slots = part_count * part_length
        available_tasks = len(tasks) - maximum * max_count
        idles = max(0, empty_slots - available_tasks)
        return len(tasks) + idles

        return len(tasks) + idles
