from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # Total area
        total_area = sum(l * l for _, _, l in squares)
        target = total_area / 2.0

        def area_below(y: float) -> float:
            area = 0.0
            for _, yi, li in squares:
                if y <= yi:
                    continue
                elif y >= yi + li:
                    area += li * li
                else:
                    area += (y - yi) * li
            return area

        low = min(yi for _, yi, _ in squares)
        high = max(yi + li for _, yi, li in squares)

        for _ in range(60):  
            mid = (low + high) / 2
            if area_below(mid) < target:
                low = mid
            else:
                high = mid

        return low
