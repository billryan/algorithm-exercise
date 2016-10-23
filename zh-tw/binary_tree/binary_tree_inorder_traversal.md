# Binary Tree Inorder Traversal

## Question

- leetcode: [Binary Tree Inorder Traversal | LeetCode OJ](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- lintcode: [(67) Binary Tree Inorder Traversal](http://www.lintcode.com/en/problem/binary-tree-inorder-traversal/)

### Problem Statement

Given a binary tree, return the _inorder_ traversal of its nodes' values.

#### Example

Given binary tree `{1,#,2,3}`,



       1
        \
         2
        /
       3


return `[1,3,2]`.

#### Challenge

Can you do it without recursion?

## 題解1 - 遞迴版

中序遍歷的訪問順序爲『先左再根後右』，遞迴版最好理解，遞迴調用時注意返回值和遞迴左右子樹的順序即可。

### Python

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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        if root is None:
            return []
        else:
            return [root.val] + self.inorderTraversal(root.left) \
                              + self.inorderTraversal(root.right)
```

### Python - with helper

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
    def inorderTraversal(self, root):
        result = []
        self.helper(root, result)
        return result

    def helper(self, root, ret):
        if root is not None:
            self.helper(root.left, ret)
            ret.append(root.val)
            self.helper(root.right, ret)
```

### C++

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        helper(root, result);
        return result;
    }

private:
    void helper(TreeNode *root, vector<int> &ret) {
        if (root != NULL) {
            helper(root->left, ret);
            ret.push_back(root->val);
            helper(root->right, ret);
        }
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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();
        helper(root, result);
        return result;
    }

    private void helper(TreeNode root, List<Integer> ret) {
        if (root != null) {
            helper(root.left, ret);
            ret.add(root.val);
            helper(root.right, ret);
        }
    }
}
```

### 源碼分析

Python 這種動態語言在寫遞迴時返回結果好處理點，無需聲明類型。通用的方法爲在遞迴函數入口參數中傳入返回結果，
也可使用分治的方法替代輔助函數。

### 複雜度分析

樹中每個節點都需要被訪問常數次，時間複雜度近似爲 $$O(n)$$. 未使用額外輔助空間。

## 題解2  - 迭代版

使用輔助 stack 改寫遞迴程序，中序遍歷沒有前序遍歷好寫，其中之一就在於出入 stack 的順序和限制規則。我們採用「左根右」的訪問順序可知主要由如下四步構成。

1. 首先需要一直對左子樹迭代並將非空節點壓入 stack 
2. 節點指針爲空後不再壓入 stack 
3. 當前節點爲空時進行出 stack 操作，並訪問 stack 頂節點
4. 將當前指針p用其右子節點替代

步驟2,3,4對應「左根右」的遍歷結構，只是此時的步驟2取的左值爲空。

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
    def inorderTraversal(self, root):
        result = []
        s = []
        while root is not None or s:
            if root is not None:
                s.append(root)
                root = root.left
            else:
                root = s.pop()
                result.append(root.val)
                root = root.right

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
    /**
     * @param root: The root of binary tree.
     * @return: Inorder in vector which contains node values.
     */
public:
    vector<int> inorderTraversal(TreeNode *root) {
        vector<int> result;
        stack<TreeNode *> s;

        while (!s.empty() || NULL != root) {
            if (root != NULL) {
                s.push(root);
                root = root->left;
            } else {
                root = s.top();
                s.pop();
                result.push_back(root->val);
                root = root->right;
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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();
        if (root == null) return result;

        Deque<TreeNode> stack = new ArrayDeque<TreeNode>();
        while (root != null || (!stack.isEmpty())) {
            if (root != null) {
                stack.push(root);
                root = root.left;
            } else {
                root = stack.pop();
                result.add(root.val);
                root = root.right;
            }
        }

        return result;
    }
}
```

### 源碼分析

使用 stack 的思想模擬遞迴，注意迭代的演進和邊界條件即可。

### 複雜度分析

最壞情況下 stack 保存所有節點，空間複雜度 $$O(n)$$, 時間複雜度 $$O(n)$$.

## Reference
