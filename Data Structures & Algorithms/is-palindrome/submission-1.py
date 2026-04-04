from typing import List
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        left_idx = 0
        right_idx = len(alpha) - 1

        while left_idx < right_idx:
            if alpha[left_idx] != alpha[right_idx]:
                return False

            left_idx += 1
            right_idx -= 1

        return True