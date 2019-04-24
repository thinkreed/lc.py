class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        result = [0] * len(temperatures)

        for i, temperature in enumerate(temperatures):
            while len(stack) > 0 and temperature > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index

            stack.append(i)

        return result

    def daily_temperatures(self, temperatures):
        stack = [0] * len(temperatures)
        result = [0] * len(temperatures)
        top = -1

        for i in range(len(temperatures)):
            while top > -1 and temperatures[i] > temperatures[stack[top]]:
                index = stack[top]
                top -= 1
                result[index] = i - index

            top += 1
            stack[top] = i

        return result
