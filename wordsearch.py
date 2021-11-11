'''Given an m x n grid of characters board and a string word, return true if word
exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where
adjacent cells are horizontally or vertically neighboring.The same letter cell may
not be used more than once.

Example  1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
'''
from typing import List


class Solution:
    #backtracking approach
    #DFS search grid and if curr path doesn't work would need to backtrack
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows,cols = len(board), len(board[0])
        #print(cols,rows)

        #set to keep track of visited letters on grid
        visited = set()

        #recursive function to perform DFS & backtracking on grid
        def backtrackDFS(row, col,index, visited):
            #check out of bounds
            if row < 0 or row > len(board) - 1 or col < 0 or col > len(board[0]) - 1:
                return False
            # if already visited current cell
            if (row,col) in visited:
                return False
            #check if found 1st letter of word
            if board[row][col] == word[index]:
                #add to visited
                visited.add((row,col))
                #print(visited)
                #once reach end of word and found entire thing
                if index == len(word) -1: return True
                # boolean to equal recursive calls for all 4 directions up, down, left, right
                checkExist = (
                    backtrackDFS(row-1,col,index+1,visited) or backtrackDFS(row,col-1,index+1,visited) or
                    backtrackDFS(row+1,col,index+1,visited) or backtrackDFS(row,col+1,index+1,visited)
                )
                #remove from visited since may need to backtrack and explore another path
                visited.remove((row,col))
                #print (checkExist)
                return checkExist
        #return true of recursive call returns true for any letter in any row or col
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrackDFS(i,j,0,visited):
                    return True
        return False
    #Time Complexity of above: O(N * 3^L)
    #N = number of cells
    #3 = directions we take (Not 4 since backtracking)
    #L = length of word to be matched

    #Space Complexity = O(L) L is length of word
    #To make the above approach faster we can add all the letters on the board to a set and compare that
    #with the word and return false immediately instead of going deeper into the search and discovering that
    #not all the letters in the given word are even on the board


    def main(self):
        sol = self.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED")
        print(sol)

obj = Solution()
obj.main()