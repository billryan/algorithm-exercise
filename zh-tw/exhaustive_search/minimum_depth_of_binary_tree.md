# Minimum Depth of Binary Tree

## Question

- leetcode: [Minimum Depth of Binary Tree | LeetCode OJ](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
- lintcode: [(155) Minimum Depth of Binary Tree](http://www.lintcode.com/en/problem/minimum-depth-of-binary-tree/)

```
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path
from the root node down to the nearest leaf node.

Example
Given a binary tree as follow:

        1

     /     \

   2       3

          /    \

        4      5
The minimum depth is 2
```

## 題解

注意審題，題中的最小深度指的是從根節點到**最近的葉子節點（因為題中的最小深度是the number of nodes，故該葉子節點不能是空節點）**，所以需要單獨處理葉子節點為空的情況。此題使用 DFS 遞迴實現比較簡單。

### Java

```java
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: An integer.
     */
    public int minDepth(TreeNode root) {
        if (root == null) return 0;

        int leftDepth = minDepth(root.left);
        int rightDepth = minDepth(root.right);

        // current node is not leaf node
        if (root.left == null) {
            return 1 + rightDepth;
        } else if (root.right == null) {
            return 1 + leftDepth;
        }

        return 1 + Math.min(leftDepth, rightDepth);
    }
}
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
    int depth(TreeNode* n){
        if(!n->left and !n->right) return 1;
        if(!n->left) return 1 + depth(n->right);
        if(!n->right) return 1 + depth(n->left);
        return 1 + min(depth(n->left), depth(n->right));
    }
    int minDepth(TreeNode* root) {
        if(!root) return 0;
        return depth(root);
    }
};
```

### 源碼分析

建立好遞迴模型即可，左右子節點為空時需要單獨處理。

### 複雜度分析

每個節點遍歷一次，時間複雜度 $$O(n)$$. 不計函數呼叫堆疊空間的話空間複雜度 $$O(1)$$.
