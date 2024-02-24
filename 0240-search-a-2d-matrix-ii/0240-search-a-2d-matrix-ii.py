from typing import List


def binary_search(mat, target):
    start = 0
    end = len(mat)-1
    while start<=end:
        mid = (start+end)//2
        if mat[mid] == target:
            return True
        elif mat[mid] > target:
            end = mid-1
        else :
            start = mid+1

    return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        is_exist = False
        for mat in matrix:
            if mat[0] > target or mat[-1] < target:
                continue
            is_exist = binary_search(mat, target)
            if is_exist:
                break

        return is_exist

