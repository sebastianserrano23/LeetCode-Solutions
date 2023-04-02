from tkinter import Toplevel
from turtle import left
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                # move top left into a variable
                topLeft = matrix[top][l + i]
                #move bottom  left into top left
                matrix[top][l + i] = matrix[bottom - i][l]
                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                # move top left into top right
                matrix[top + i][r] = topLeft
            l = l - 1
            r = r + 1
            top = top + 1
            bottom = bottom - 1