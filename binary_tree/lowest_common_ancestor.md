# Lowest Common Ancestor

Question: [(88) Lowest Common Ancestor](http://www.lintcode.com/en/problem/lowest-common-ancestor/) <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>

```
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.
Example
        4

    /     \

  3         7

          /     \

        5         6
For 3 and 5, the LCA is 4.

For 5 and 6, the LCA is 7.
For 6 and 7, the LCA is 7.
```

### 题解1 - 自顶向下

初次接触这种题可能会没有什么思路，在没有思路的情况下我们就从简单例子开始分析！首先看看`3`和`5`，这两个节点分居根节点`4`的两侧，如果可以从子节点往父节点递推，那么他们将在根节点`4`处第一次重合；再来看看`5`和`6`，这两个都在根节点`4`的右侧，沿着父节点往上递推，他们将在节点`7`处第一次重合；最后来看看`6`和`7`，此时由于`7`是`6`的父节点，故`7`即为所求。从这三个基本例子我们大概可以将其总结为如下三种情况：
1. 两个节点分居树的左右两侧，当前节点不是两个节点中的任意一个。
2. 两个节点同时在树的左侧/右侧，当前节点不是两个节点中的任意一个。
3. 当前根节点即为两个节点中的一个，此时返回根节点(但不一定是所求)。

将三种情况组合起来(整体思想)即可递归求解，下面我们来看看使用分治思想的递归版代码。

#### C++ Recursion Divide and Conquer

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
     * @param root: The root of the binary search tree.
     * @param A and B: two nodes in a Binary.
     * @return: Return the least common ancestor(LCA) of the two nodes.
     */
    TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *A, TreeNode *B) {
        if (NULL == root || root == A || root == B) {
            return root;
        } // case 3

        TreeNode *left = lowestCommonAncestor(root->left, A, B);
        TreeNode *right = lowestCommonAncestor(root->right, A, B);

        if ((NULL != left) && (NULL != right)) {
            return root;
        } // case 1

        if (NULL != left) {
            return left;
        } // case 2

        if (NULL != right) {
            return right;
        } // case 2

        return NULL;
    }
};
```

#### 源码分析

结合例子和递归的整体思想去理解代码，在`root == A || root == B`后即层层上浮，直至找到最终的最小公共祖先节点。

两个节点和根节点的各种情况均已在代码中标注，共4中情况，前三种为我们主要关注的。

## Reference

- [Lowest Common Ancestor | 九章算法](http://www.jiuzhang.com/solutions/lowest-common-ancestor/) - Divide and Conquer 部分即为题解1的源泉。
- [Lowest Common Ancestor of a Binary Tree Part I | LeetCode](http://articles.leetcode.com/2011/07/lowest-common-ancestor-of-a-binary-tree-part-i.html)
- [Lowest Common Ancestor of a Binary Tree Part II | LeetCode](http://articles.leetcode.com/2011/07/lowest-common-ancestor-of-a-binary-tree-part-ii.html) - 如果
