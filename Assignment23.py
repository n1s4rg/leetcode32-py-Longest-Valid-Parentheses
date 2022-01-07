class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        l = len(s)
        ls = 0

        for i in range(0, l):
            if s[i] == "(":
                stack.append(i)
                ls += 1
            else:
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                    ls -= 1
                else:
                    stack.append(i)
                    ls += 1
        if not stack:
            return l
        res = stack[0] - 0
        last = stack[0]

        for i in range(1, ls):
            res = max(res, stack[i] - last - 1)
            last = stack[i]

        return max(res, l - last - 1)


print(Solution().longestValidParentheses( ")()())"))
