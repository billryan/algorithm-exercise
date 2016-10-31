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


## 題解 - 使用隊列

此題爲廣度優先搜索(BFS)的基礎題，使用一個隊列保存每層的節點即可。出隊列和將子節點入隊列的實現使用 for 循環，將每一輪的節點輸出。

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

### 源碼分析

1. 異常，還是異常
2. 使用STL的`queue`數據結構，將`root`添加進隊列
3. **遍歷當前層所有節點，注意需要先保存隊列大小，因爲在入隊出隊時隊列大小會變化**
4. `list`保存每層節點的值，每次使用均要初始化

### 複雜度分析

使用輔助隊列，空間複雜度 $$O(n)$$, 時間複雜度 $$O(n)$$.
