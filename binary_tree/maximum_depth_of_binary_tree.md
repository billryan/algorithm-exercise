# Maximum Depth of Binary Tree

Question: [(97) Maximum Depth of Binary Tree](http://www.lintcode.com/en/problem/maximum-depth-of-binary-tree/)

```
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example
Given a binary tree as follow:

        1

     /     \

   2       3

          /    \

        4      5

The maximum depth is 3
```

### 题解 - 递归

树遍历的题最方便的写法自然是递归，不过递归调用的层数过多可能会导致栈空间溢出，因此需要适当考虑递归调用的层数。我们首先来看看使用递归如何解这道题，要求二叉树的最大深度，直观上来讲使用深度优先搜索判断左右子树的深度孰大孰小即可，从根节点往下一层树的深度即自增1，遇到`NULL`时即返回0。

由于对每个节点都会使用一次`maxDepth`，故时间复杂度为 $$O(n)$$, 树的深度最大为 $$n$$, 最小为 $$\log_2 n$$, 故空间复杂度介于 $$O(\log n)$$ 和 $$ O(n)$$ 之间。

#### C++ Recursion

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
     * @return: An integer
     */
    int maxDepth(TreeNode *root) {
        if (NULL == root) {
            return 0;
        }

        int left_depth = maxDepth(root->left);
        int right_depth = maxDepth(root->right);

        return max(left_depth, right_depth) + 1;
    }
};
```

### 题解 - 迭代

使用递归可能会导致栈空间溢出，这里使用显式栈空间(使用堆内存)来代替之前的隐式栈空间。
