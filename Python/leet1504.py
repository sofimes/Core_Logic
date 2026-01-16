class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        height = [0] * n
        result = 0

        for i in range(m):
            stack = []
            row_sum = 0

            for j in range(n):
                # Update histogram height
                if mat[i][j] == 1:
                    height[j] += 1
                else:
                    height[j] = 0

                count = 1

                # Maintain increasing stack
                while stack and stack[-1][0] >= height[j]:
                    h, c = stack.pop()
                    row_sum -= h * c
                    count += c

                row_sum += height[j] * count
                stack.append((height[j], count))

                result += row_sum

        return result
