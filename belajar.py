from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(numRows):
            # Baris pertama selalu [1]
            row = [1] * (i + 1)
            # Hitung nilai tengah baris (selain ujung kiri dan kanan)
            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
            result.append(row)

        return result
