# Lowest Common Ancestor

## Question

- lintcode: [(88) Lowest Common Ancestor](http://www.lintcode.com/en/problem/lowest-common-ancestor/)


### Problem Statement

Given the root and two nodes in a Binary Tree. Find the lowest common
ancestor(LCA) of the two nodes.

The lowest common ancestor is the node with largest depth which is the
ancestor of both nodes.

#### Example

For the following binary tree:

    
    
      4
     / \
    3   7
       / \
      5   6
    

LCA(3, 5) = `4`

LCA(5, 6) = `7`

LCA(6, 7) = `7`


## 题解1 - 自底向上

初次接触这种题可能会没有什么思路，在没有思路的情况下我们就从简单例子开始分析！首先看看`3`和`5`，这两个节点分居根节点`4`的两侧，如果可以从子节点往父节点递推，那么他们将在根节点`4`处第一次重合；再来看看`5`和`6`，这两个都在根节点`4`的右侧，沿着父节点往上递推，他们将在节点`7`处第一次重合；最后来看看`6`和`7`，此时由于`7`是`6`的父节点，故`7`即为所求。从这三个基本例子我们可以总结出两种思路——自顶向下(从前往后递推)和自底向上(从后往前递推)。

顺着上述实例的分析，我们首先看看自底向上的思路，自底向上的实现用一句话来总结就是——如果遍历到的当前节点是 A/B 中的任意一个，那么我们就向父节点汇报此节点，否则递归到节点为空时返回空值。具体来说会有如下几种情况：

1. 当前节点不是两个节点中的任意一个，此时应判断左右子树的返回结果。
    - 若左右子树均返回非空节点，那么当前节点一定是所求的根节点，将当前节点逐层向前汇报。// 两个节点分居树的两侧
    - 若左右子树仅有一个子树返回非空节点，则将此非空节点向父节点汇报。// 节点仅存在于树的一侧
    - 若左右子树均返回`NULL`, 则向父节点返回`NULL`. // 节点不在这棵树中
2. 当前节点即为两个节点中的一个，此时向父节点返回当前节点。

根据此递归模型容易看出应该使用先序/后序遍历来实现。

### C++ Recursion From Bottom to Top

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
        // return either A or B or NULL
        if (NULL == root || root == A || root == B) return root;

        TreeNode *left = lowestCommonAncestor(root->left, A, B);
        TreeNode *right = lowestCommonAncestor(root->right, A, B);

        // A and B are on both sides
        if ((NULL != left) && (NULL != right)) return root;

        // either left or right or NULL
        return (NULL != left) ? left : right;
    }
};
```

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
     * @param root: The root of the binary search tree.
     * @param A and B: two nodes in a Binary.
     * @return: Return the least common ancestor(LCA) of the two nodes.
     */
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode A, TreeNode B) {
        if (root == null) return null;
        
        TreeNode lNode = lowestCommonAncestor(root.left, A, B);
        TreeNode rNode = lowestCommonAncestor(root.right, A, B);
        // root is the LCA of A and B
        if (lNode != null && rNode != null) return root;
        // root node is A/B(including the case below)
        if (root == A || root == B) return root;
        // return lNode/rNode if root is not LCA
        return (lNode != null) ? lNode : rNode;
    }
}
```

### 源码分析

结合例子和递归的整体思想去理解代码，在`root == A || root == B`后即层层上浮(自底向上)，直至找到最终的最小公共祖先节点。

最后一行`return (NULL != left) ? left : right;`将非空的左右子树节点和空值都包含在内了，十分精炼！[^leetcode]

> **fixme** 细心的你也许会发现，其实题解的分析漏掉了一种情况，即树中可能只含有 A/B 中的一个节点！这种情况应该返回空值，但上述实现均返回非空节点。

关于重复节点：由于这里比较的是元素地址，因此可以认为树中不存在重复元素，否则不符合树的数据结构。

## 题解 - 自底向上(计数器)

为了解决上述方法可能导致误判的情况，我们可以对返回结果添加计数器来解决。**由于此计数器的值只能由子树向上递推，故应该用后序遍历。**在类中添加私有变量较为方便, C++中的写法较为复杂，后续再优化。

定义`pair<TreeNode *, int> result(node, counter)`表示遍历到某节点时的返回结果，返回的`node`表示LCA 路径中的可能的最小节点，相应的计数器`counter`则表示目前和`A`或者`B`匹配的节点数，若计数器为2，则表示已匹配过两次，该节点即为所求，若只匹配过一次，还需进一步向上递推。表述地可能比较模糊，还是看看代码吧。

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
     * @param root: The root of the binary search tree.
     * @param A and B: two nodes in a Binary.
     * @return: Return the least common ancestor(LCA) of the two nodes.
     */
    TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *A, TreeNode *B) {
        if ((NULL == A) || (NULL == B)) return NULL;

        pair<TreeNode *, int> result = helper(root, A, B);

        if (A != B) {
            return (2 == result.second) ? result.first : NULL;
        } else {
            return (1 == result.second) ? result.first : NULL;
        }
    }

private:
    pair<TreeNode *, int> helper(TreeNode *root, TreeNode *A, TreeNode *B) {
        TreeNode * node = NULL;
        if (NULL == root) return make_pair(node, 0);

        pair<TreeNode *, int> left = helper(root->left, A, B);
        pair<TreeNode *, int> right = helper(root->right, A, B);

        // return either A or B
        int count = max(left.second, right.second);
        if (A == root || B == root)  return make_pair(root, ++count);

        // A and B are on both sides
        if (NULL != left.first && NULL != right.first) return make_pair(root, 2);

        // return either left or right or NULL
        return (NULL != left.first) ? left : right;
    }
};
```

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
    private int count = 0;
    /**
     * @param root: The root of the binary search tree.
     * @param A and B: two nodes in a Binary.
     * @return: Return the least common ancestor(LCA) of the two nodes.
     */
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode A, TreeNode B) {
        TreeNode result = helper(root, A, B);
        if (A == B) {
            return result;
        } else {
            return (count == 2) ? result : null;
        }
    }
    
    private TreeNode helper(TreeNode root, TreeNode A, TreeNode B) {
        if (root == null) return null;
        
        TreeNode lNode = helper(root.left, A, B);
        TreeNode rNode = helper(root.right, A, B);
        // root is the LCA of A and B
        if (lNode != null && rNode != null) return root;
        // root node is A/B(including the case below)
        if (root == A || root == B) {
            count++;
            return root;
        }
        // return lNode/rNode if root is not LCA
        return (lNode != null) ? lNode : rNode;
    }
}
```

### 源码分析

在`A == B`时，计数器返回1的节点即为我们需要的节点，否则只取返回2的节点，如此便保证了该方法的正确性。对这种实现还有问题的在下面评论吧。

## Reference

- [^leetcode]: [Lowest Common Ancestor of a Binary Tree Part I | LeetCode](http://articles.leetcode.com/2011/07/lowest-common-ancestor-of-a-binary-tree-part-i.html) - 清晰易懂的题解和实现。
- [Lowest Common Ancestor of a Binary Tree Part II | LeetCode](http://articles.leetcode.com/2011/07/lowest-common-ancestor-of-a-binary-tree-part-ii.html) - 如果存在指向父节点的指针，我们能否有更好的解决方案？
- [Lowest Common Ancestor of a Binary Search Tree (BST) | LeetCode](http://articles.leetcode.com/2011/07/lowest-common-ancestor-of-a-binary-search-tree.html) - 二叉搜索树中求最小公共祖先。
- [Lowest Common Ancestor | 九章算法](http://www.jiuzhang.com/solutions/lowest-common-ancestor/) - 第一种和第二种方法可以在知道父节点时使用，但第二种 Divide and Conquer 才是本题需要的思想（第二种解法可以轻易改成不需要 parent 的指针的）。
