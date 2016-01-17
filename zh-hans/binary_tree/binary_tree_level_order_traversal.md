# Binary Tree Level Order Traversal

## Question

- leetcode: [Binary Tree Level Order Traversal | LeetCode OJ](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- lintcode: [(69) Binary Tree Level Order Traversal](http://www.lintcode.com/en/problem/binary-tree-level-order-traversal/)

### Problem Statement

Given a binary tree, return the _level order_ traversal of its nodes' values.
(ie, from left to right, level by level).

#### Example

Given binary tree `{3,9,20,#,#,15,7}`,



        3
       / \
      9  20
        /  \
       15   7


return its level order traversal as:



    [
      [3],
      [9,20],
      [15,7]
    ]

#### Challenge

Challenge 1: Using only 1 queue to implement it.

Challenge 2: Use DFS algorithm to do it.


## 题解 - 使用队列

此题为广搜的基础题，使用一个队列保存每层的节点即可。出队和将子节点入队的实现使用 for 循环，将每一轮的节点输出。

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
     * @return: Level order a list of lists of integer
     */
public:
    vector<vector<int> > levelOrder(TreeNode *root) {
        vector<vector<int> > result;

        if (NULL == root) {
            return result;
        }

        queue<TreeNode *> q;
        q.push(root);
        while (!q.empty()) {
            vector<int> list;
            int size = q.size(); // keep the queue size first
            for (int i = 0; i != size; ++i) {
                TreeNode * node = q.front();
                q.pop();
                list.push_back(node->val);
                if (node->left) {
                    q.push(node->left);
                }
                if (node->right) {
                    q.push(node->right);
                }
            }
            result.push_back(list);
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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (root == null) return result;

        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);
        while (!q.isEmpty()) {
            List<Integer> list = new ArrayList<Integer>();
            int qSize = q.size();
            for (int i = 0; i < qSize; i++) {
                TreeNode node = q.poll();
                list.add(node.val);
                // push child node into queue
                if (node.left != null) q.offer(node.left);
                if (node.right != null) q.offer(node.right);
            }
            result.add(new ArrayList<Integer>(list));
        }

        return result;
    }
}
```

### 源码分析

1. 异常，还是异常
2. 使用STL的`queue`数据结构，将`root`添加进队列
3. **遍历当前层所有节点，注意需要先保存队列大小，因为在入队出队时队列大小会变化**
4. `list`保存每层节点的值，每次使用均要初始化

### 复杂度分析

使用辅助队列，空间复杂度 $$O(n)$$, 时间复杂度 $$O(n)$$.
