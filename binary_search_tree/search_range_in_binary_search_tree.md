# Search Range in Binary Search Tree


## Source

- lintcode: [(11) Search Range in Binary Search Tree](http://www.lintcode.com/en/problem/search-range-in-binary-search-tree/) <i class="fa fa-star"></i><i class="fa fa-star"></i>


```
Given two values k1 and k2 (where k1 < k2) and a root pointer to a Binary Search Tree.
Find all the keys of tree in range k1 to k2. i.e. print all x such that k1<=x<=k2 and x is a key of given BST.
Return all the keys in ascending order.

Example
For example, if k1 = 10 and k2 = 22, then your function should print 12, 20 and 22.

          20

       /        \

    8           22

  /     \

4       12
```

### 题解 - 中序遍历

中等偏易难度题，本题涉及到二叉查找树的按序输出，应马上联想到二叉树的中序遍历，对于二叉查找树而言，使用中序遍历即可得到有序元素。对每次访问的元素加以判断即可得最后结果，由于 OJ 上给的模板不适合递归处理，新建一个私有方法即可。

#### C++ In-order Recursion

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
     * @param k1 and k2: range k1 to k2.
     * @return: Return all keys that k1<=key<=k2 in ascending order.
     */
    vector<int> searchRange(TreeNode* root, int k1, int k2) {
        vector<int> result;
        inorder_dfs(result, root, k1, k2);

        return result;
    }

private:
    void inorder_dfs(vector<int> &ret, TreeNode *root, int k1, int k2) {
        if (NULL == root) {
            return;
        }

        inorder_dfs(ret, root->left, k1, k2);
        if ((root->val >= k1) && (root->val <= k2)) {
            ret.push_back(root->val);
        }
        inorder_dfs(ret, root->right, k1, k2);
    }
};
```

#### 源码分析

以上为题解思路的简易实现，可以优化的地方为「剪枝过程」的处理——不递归遍历不可能有解的节点。优化后的`inorder_dfs`如下：

```c++
    void inorder_dfs(vector<int> &ret, TreeNode *root, int k1, int k2) {
        if (NULL == root) {
            return;
        }

        if ((NULL != root->left) && (root->val > k1)) {
            inorder_dfs(ret, root->left, k1, k2);
        } // cut-off for left sub tree

        if ((root->val >= k1) && (root->val <= k2)) {
            ret.push_back(root->val);
        } // add valid value

        if ((NULL != root->right) && (root->val < k2)) {
            inorder_dfs(ret, root->right, k1, k2);
        } // cut-off for right sub tree
    }
```

> **Warning** 「剪枝」的判断条件容易出错，应将当前节点的值与`k1`和`k2`进行比较而不是其左子节点或右子节点的值。
