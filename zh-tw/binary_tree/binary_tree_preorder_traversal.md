# Binary Tree Preorder Traversal

## Question

- leetcode: [Binary Tree Preorder Traversal | LeetCode OJ](https://leetcode.com/problems/binary-tree-preorder-traversal/)
- lintcode: [(66) Binary Tree Preorder Traversal](http://www.lintcode.com/en/problem/binary-tree-preorder-traversal/)

```
Given a binary tree, return the preorder traversal of its nodes' values.

Note
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3

return [1,2,3].

Example
Challenge
Can you do it without recursion?
```

## 題解1 - 遞迴

**面試時不推薦遞迴這種做法。**

遞迴版很好理解，首先判斷當前節點(根節點)是否為`null`，是則返回空vector，否則先返回當前節點的值，然後對當前節點的左節點遞迴，最後對當前節點的右節點遞迴。遞迴時對返回結果的處理方式不同可進一步細分為遍歷和分治兩種方法。

譯註：也不是完全不能這麼做，不過以二元樹的遍歷來說，遞迴方法太容易實現，面試官很可能進一步要求迭代的方法，並且有可能會問遞迴的缺點(連續呼叫函數導致stack的overflow問題)，不過如果遍歷並不是題幹而只是解決方法的步驟，用簡單的迭代方式實現有時亦無不可且可以減少錯誤，因此務必要和面試官充分溝通，另即使迭代寫不出來只寫出遞迴版本也要好過完全寫不出東西。

### Python - Divide and Conquer

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        if root == None:
            return []
        return [root.val] + self.preorderTraversal(root.left) \
                          + self.preorderTraversal(root.right)
```

### C++ - Divide and Conquer

```c++
/**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 */

class Solution {
public:
    /**
     * @param root: The root of binary tree.
     * @return: Preorder in vector which contains node values.
     */
    vector<int> preorderTraversal(TreeNode *root) {
        vector<int> result;
        if (root != NULL) {
            // Divide (分)
            vector<int> left = preorderTraversal(root->left);
            vector<int> right = preorderTraversal(root->right);
            // Merge
            result.push_back(root->val);
            result.insert(result.end(), left.begin(), left.end());
            result.insert(result.end(), right.begin(), right.end());
        }

        return result;
    }
};
```

### C++ - Traversal

```c++
/**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 */

class Solution {
public:
    /**
     * @param root: The root of binary tree.
     * @return: Preorder in vector which contains node values.
     */
    vector<int> preorderTraversal(TreeNode *root) {
        vector<int> result;
        traverse(root, result);

        return result;
    }

private:
    void traverse(TreeNode *root, vector<int> &ret) {
        if (root != NULL) {
            ret.push_back(root->val);
            traverse(root->left, ret);
            traverse(root->right, ret);
        }
    }
};
```

### Java - Divide and Conquer

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();
        if (root != null) {
            // Divide
            List<Integer> left = preorderTraversal(root.left);
            List<Integer> right = preorderTraversal(root.right);
            // Merge
            result.add(root.val);
            result.addAll(left);
            result.addAll(right);
        }
        
        return result;
    }
}
```

### 源碼分析

使用遍歷的方法保存遞迴返回結果需要使用輔助遞迴函數`traverse`，將結果作為參數傳入遞迴函數中，傳值時注意應使用`vector`的引用。
分治方法首先分開計算各結果，最後合並到最終結果中。
C++ 中由於是使用vector, 將新的vector插入另一vector不能再使用push_back, 而應該使用insert。
Java 中使用`addAll`方法.

### 複雜度分析

遍歷樹中節點，時間複雜度 $$O(n)$$, 未使用額外空間(不包括呼叫函數的stack開銷)。

## 題解2 - 迭代

迭代時需要利用堆疊來保存遍歷到的節點，紙上畫圖分析後發現應首先進行出堆疊拋出當前節點，保存當前節點的值，隨後將右、左節點分別進入堆疊(注意進入堆疊順序，先右後左)，迭代到其為葉子節點(NULL)為止。

### Python

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        if root is None:
            return []

        result = []
        s = []
        s.append(root)
        while s:
            root = s.pop()
            result.append(root.val)
            if root.right is not None:
                s.append(root.right)
            if root.left is not None:
                s.append(root.left)
                
        return result
        
```

### C++

```c++
/**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 */

class Solution {
public:
    /**
     * @param root: The root of binary tree.
     * @return: Preorder in vector which contains node values.
     */
    vector<int> preorderTraversal(TreeNode *root) {
        vector<int> result;
        if (root == NULL) return result;

        stack<TreeNode *> s;
        s.push(root);
        while (!s.empty()) {
            TreeNode *node = s.top();
            s.pop();
            result.push_back(node->val);
            if (node->right != NULL) {
                s.push(node->right);
            }
            if (node->left != NULL) {
                s.push(node->left);
            }
        }

        return result;
    }
};
```

### Java

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();
        if (root == null) return result;
        
        Stack<TreeNode> s = new Stack<TreeNode>();
        s.push(root);
        while (!s.empty()) {
            TreeNode node = s.pop();
            result.add(node.val);
            if (node.right != null) s.push(node.right);
            if (node.left != null) s.push(node.left);
        }
        
        return result;
    }
}
```

### 源碼分析

1. 對root進行異常處理
2. 將root壓入堆疊
3. 循環終止條件為堆疊s為空，所有元素均已處理完
4. 訪問當前堆疊頂元素(首先取出堆疊頂元素，隨後pop掉堆疊頂元素)並存入最終結果
5. 將右、左節點分別壓入堆疊內，以便取元素時為先左後右。
6. 返回最終結果

其中步驟4,5,6為迭代的核心，對應前序遍歷「根左右」。

所以說到底，**使用迭代，只不過是另外一種形式的遞迴。**使用遞迴的思想去理解遍歷問題會容易理解許多。

### 複雜度分析

使用輔助堆疊，最壞情況下堆疊空間與節點數相等，空間複雜度近似為 $$O(n)$$, 對每個節點遍歷一次，時間複雜度近似為 $$O(n)$$.
