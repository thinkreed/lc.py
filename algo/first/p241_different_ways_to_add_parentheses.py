class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]

        result = []

        for i in range(len(input)):
            if input[i] in '+-*':
                result_left = self.diffWaysToCompute(input[:i])
                result_right = self.diffWaysToCompute(input[i + 1:])
                for a in result_left:
                    for b in result_right:
                        if input[i] == '+':
                            result.append(a + b)
                        elif input[i] == '-':
                            result.append(a - b)
                        else:
                            result.append(a * b)

        return result
