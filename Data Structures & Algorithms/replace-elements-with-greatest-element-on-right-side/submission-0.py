class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1
        for i in range(len(arr) - 1, -1, -1):
        # Keep old value before overwriting
            old_val = arr[i]
            arr[i] = max_val
            max_val = max(max_val, old_val)
        return arr