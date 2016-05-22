# Valid Sudoku

## Question

- leetcode: [Valid Sudoku | LeetCode OJ](https://leetcode.com/problems/valid-sudoku/)
- lintcode: [(389) Valid Sudoku](http://www.lintcode.com/en/problem/valid-sudoku/)

```
Determine whether a Sudoku is valid.

The Sudoku board could be partially filled,
where empty cells are filled with the character ..

Example
The following partially filed sudoku is valid.
```

![valid-sudoku.png](../../shared-files/images/valid-sudoku.png)

```
Valid Sudoku

Note
A valid Sudoku board (partially filled) is not necessarily solvable.
Only the filled cells need to be validated.
Clarification
What is Sudoku?

http://sudoku.com.au/TheRules.aspx
https://zh.wikipedia.org/wiki/%E6%95%B8%E7%8D%A8
https://en.wikipedia.org/wiki/Sudoku
http://baike.baidu.com/subview/961/10842669.htm
```

## 題解

看懂數獨的含義就好了，分為三點考慮，一是每行無重複數字；二是每列無重複數字；三是小的九宮格中無重複數字。

### Java

```java
class Solution {
    /**
      * @param board: the board
        @return: wether the Sudoku is valid
      */
    public boolean isValidSudoku(char[][] board) {
        if (board == null || board.length == 0) return false;

        // check row
        for (int i = 0; i < 9; i++) {
            boolean[] numUsed = new boolean[9];
            for (int j = 0; j < 9; j++) {
                if (isDuplicate(board[i][j], numUsed)) {
                    return false;
                }
            }
        }

        // check column
        for (int i = 0; i < 9; i++) {
            boolean[] numUsed = new boolean[9];
            for (int j = 0; j < 9; j++) {
                if (isDuplicate(board[j][i], numUsed)) {
                    return false;
                }
            }
        }

        // check sub box
        for (int i = 0; i < 9; i = i + 3) {
            for (int j = 0; j < 9; j = j + 3) {
                if (!isValidBox(board, i, j)) {
                    return false;
                }
            }
        }

        return true;
    }

    private boolean isValidBox(char[][] box, int x, int y) {
        boolean[] numUsed = new boolean[9];
        for (int i = x; i < x + 3; i++) {
            for (int j = y; j < y + 3; j++) {
                if (isDuplicate(box[i][j], numUsed)) {
                    return false;
                }
            }
        }
        return true;
    }

    private boolean isDuplicate(char c, boolean[] numUsed) {
        if (c == '.') {
            return false;
        } else if (numUsed[c - '1']) {
            return true;
        } else {
            numUsed[c - '1'] = true;
            return false;
        }
    }
}
```

### C++

```c++
class Solution {
public:
    bool isValidBlock(vector<int>& v){
        bool ans = true;
        for(int i = 0; i < v.size(); i++){
            if(v[i] > 1)
                ans = false;
            v[i] = 0;
        }
        return ans;
    }
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<int> num(9, 0);

        //row
        for(int i=0; i<9; i++){
            for(int j=0; j<9; j++){
                char n = board[i][j];
                if('1' <= n and n <= '9')
                    num[n - '1'] ++;
            }
            
            if(!isValidBlock(num))
                return false;
        }
        
        //col
        
        for(int j=0; j<9; j++){
            for(int i=0; i<9; i++){
                char n = board[i][j];
                if('1' <= n and n <= '9')
                    num[n - '1']++;
            }
            if(!isValidBlock(num))
                return false;
        }
        
        //block
        
        for(int row = 0; row < 3; row++){
            for(int col = 0; col < 3; col++){
                for(int i = 0; i < 3; i++){
                    for(int j = 0; j < 3; j++){
                        char n = board[3*row +i][3*col+j];
                        if('1' <= n and  n <= '9')
                            num[n - '1']++;
                    }
                }
                if(!isValidBlock(num))
                    return false;
            }
        }
        return true;
    }
};
```

### 源碼分析

首先實現兩個小的子功能模塊判斷是否有重複和小的九宮格是否重複。

### 複雜度分析

略

## Reference

- Soulmachine 的 leetcode 題解
