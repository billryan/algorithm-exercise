# Binary Tree Maximum Path Sum

## Question

- leetcode: [Binary Tree Maximum Path Sum | LeetCode OJ](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
- lintcode: [(94) Binary Tree Maximum Path Sum](http://www.lintcode.com/en/problem/binary-tree-maximum-path-sum/)

### Problem Statement

Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

#### Example

Given the below binary tree:

    
    
      1
     / \
    2   3
    

return `6`.

## 题解1 - 递归中仅返回子树路径长度

如题目右侧的四颗半五角星所示，本题属于中等偏难的那一类题。题目很短，要求返回最大路径和。咋看一下感觉使用递归应该很快就能搞定，实则不然，**因为从题目来看路径和中不一定包含根节点！也就是说可以起止于树中任一连通节点。**

弄懂题意后我们就来剖析剖析，本着由简入难的原则，我们先来分析若路径和包含根节点，如何才能使其路径和达到最大呢？选定根节点后，路径和中必然包含有根节点的值，剩下的部分则为左子树和右子树，要使路径和最大，则必然要使左子树和右子树中的路径长度都取最大。

> **Warning** 注意区分包含根节点的路径和(题目要的答案)和左子树/右子树部分的路径长度(答案的一个组成部分)。路径和=根节点+左子树路径长度+右子树路径长度

```
       -10
       /  \
      2    -3
     / \   / \
    3   4 5   7
```
如上所示，包含根节点`-10`的路径和组成的节点应为`4 -> 2 -> -10 <- -3 <- 7`, 对于左子树而言，其可能的路径组成节点为`3 -> 2`或`4 -> 2`, 而不是像根节点的路径和那样为`3 -> 2 <- 4`. 这种差异也就造成了我们不能很愉快地使用递归来求得最大路径和。

我们使用分治的思想来分析路径和/左子树/右子树，设 $$f(root)$$ 为`root`的子树到`root`节点(含)路径长度的最大值，那么我们有
$$f(root) = root->val + \max (f(root->left), ~f(root->right))$$

递归模型已初步建立起来，接下来就是分析如何将左右子树的路径长度和最终题目要求的「路径和」挂钩。设 $$g(root)$$ 为当「路径和」中根节点为`root`时的值，那么我们有
$$g(root) = root->val + f(root->left) + f(root->right)$$

顺着这个思路，我们可以遍历树中的每一个节点求得 $$g(node)$$ 的值，输出最大值即可。如果不采取任何记忆化存储的措施，其时间复杂度必然是指数级别的。嗯，先来看看这个思路的具体实现，后续再对其进行优化。遍历节点我们使用递归版的前序遍历，求单边路径长度采用递归。

### C++ Recursion + Iteration(Not Recommended) <i class="fa fa-hand-o-down"></i>

**Time Limit Exceeded**

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
    int maxPathSum(TreeNode *root) {
        if (NULL == root) {
            return 0;
        }

        int result = INT_MIN;
        stack<TreeNode *> s;
        s.push(root);
        while (!s.empty()) {
            TreeNode *node = s.top();
            s.pop();

            int temp_path_sum = node->val + singlePathSum(node->left) \
                                          + singlePathSum(node->right);

            if (temp_path_sum > result) {
                result = temp_path_sum;
            }

            if (NULL != node->right) s.push(node->right);
            if (NULL != node->left) s.push(node->left);
        }

        return result;
    }

private:
    int singlePathSum(TreeNode *root) {
        if (NULL == root) {
            return 0;
        }

        int path_sum = max(singlePathSum(root->left), singlePathSum(root->right));
        return max(0, (root->val + path_sum));
    }
};
```

### 源码分析

注意`singlePathSum`中最后的返回值，如果其路径长度`path_sum`比0还小，那么取这一段路径反而会减少最终的路径和，故不应取这一段，我们使用0表示这一隐含意义。

## 题解2 - 递归中同时返回子树路径长度和路径和

### C++ using std::pair

上题求路径和和左右子树路径长度是分开求得的，因此导致了时间复杂度剧增的恶劣情况，从题解的递推关系我们可以看出其实是可以在一次递归调用过程中同时求得路径和和左右子树的路径长度的，只不过此时递归程序需要返回的不再是一个值，而是路径长度和路径和这一组值！C++中我们可以使用`pair`或者自定义新的数据类型来相对优雅的解决。

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
private:
    pair<int, int> helper(TreeNode *root) {
        if (NULL == root) {
            return make_pair(0, INT_MIN);
        }

        pair<int, int> leftTree = helper(root->left);
        pair<int, int> rightTree = helper(root->right);

        int single_path_sum = max(leftTree.first, rightTree.first) + root->val;
        single_path_sum = max(0, single_path_sum);

        int max_sub_sum = max(leftTree.second, rightTree.second);
        int max_path_sum = root->val + leftTree.first + rightTree.first;
        max_path_sum = max(max_sub_sum, max_path_sum);

        return make_pair(single_path_sum, max_path_sum);
    }

public:
    /**
     * @param root: The root of binary tree.
     * @return: An integer
     */
    int maxPathSum(TreeNode *root) {
        if (NULL == root) {
            return 0;
        }

        return helper(root).second;
    }
};
```

### 源码分析

除了使用`pair`对其进行封装，也可使用嵌套类新建一包含单路径长度和全局路径和两个变量的类，不过我用 C++写的没编译过... 老是提示`...private`，遂用`pair`改写之。建议使用`class`而不是`pair`封装`single_path_sum`和`max_path_sum`[^pair_is_harmful].

这种方法难以理解的地方在于这种实现方式的正确性，较为关键的语句为`max_path_sum = max(max_sub_sum, max_path_sum)`, 这行代码是如何体现题目中以下的这句话的呢？
> The path may start and end at any node in the tree.

简单来讲，题解2从两个方面予以保证：
1. 采用「冒泡」法返回不经过根节点的路径和的较大值。
2. 递推子树路径长度(不变值)而不是到该节点的路径和(有可能变化)，从而保证了这种解法的正确性。

如果还不理解的建议就以上面那个根节点为-10的例子画一画。

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
    class ResultType {
    public:
        int singlePath, maxPath;
        ResultType(int s, int m):singlePath(s), maxPath(m) {}
    };

private:
    ResultType helper(TreeNode *root) {
        if (root == NULL) {
            ResultType *nullResult = new ResultType(0, INT_MIN);
            return *nullResult;
        }
        // Divide
        ResultType left = helper(root->left);
        ResultType right = helper(root->right);

        // Conquer
        int singlePath = max(left.singlePath, right.singlePath) + root->val;
        singlePath = max(singlePath, 0);

        int maxPath = max(left.maxPath, right.maxPath);
        maxPath = max(maxPath, left.singlePath + right.singlePath + root->val);
        
        ResultType *result = new ResultType(singlePath, maxPath);
        return *result;
    }

public:
    int maxPathSum(TreeNode *root) {
        ResultType result = helper(root);
        return result.maxPath;
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
class Result {
    int singlePath, maxPath;
    Result(int singlePath, int maxPath) {
        this.singlePath = singlePath;
        this.maxPath = maxPath;
    }
}

public class Solution {
    public int maxPathSum(TreeNode root) {
        return helper(root).maxPath;
    }
    
    private Result helper(TreeNode root) {
        if (root == null) {
            // maxPath should be MIN_VALUE to avoid negtive
            return new Result(0, Integer.MIN_VALUE);
        }
        
        Result left = helper(root.left);
        Result right = helper(root.right);
        
        int singlePath = Math.max(left.singlePath, right.singlePath) + root.val;
        singlePath = Math.max(0, singlePath); // drop negtive
        
        int maxPath = Math.max(left.maxPath, right.maxPath);
        maxPath = Math.max(maxPath, root.val + left.singlePath + right.singlePath);
        
        return new Result(singlePath, maxPath);
    }
}
```

### 源码分析
1. 如果不用 `ResultType *XXX = new ResultType ...` 再 `return *XXX` 的方式，则需要在自定义 class 中重载 `new` operator。
2. 如果遇到 `...private` 的编译错误，则是因为自定义 class 中需要把成员声明为 public，否则需要把访问这个成员的函数也做 class 内部处理。

## Reference

- [^pair_is_harmful]: [std::pair considered harmful! « Modern Maintainable Code](http://maintainablecode.logdown.com/posts/158531-stdpair-considered-harmful) - 作者指出了`pair`不能滥用的原因，如不可维护，信息量小。
- [Binary Tree Maximum Path Sum | 九章算法](http://www.jiuzhang.com/solutions/binary-tree-maximum-path-sum/)
