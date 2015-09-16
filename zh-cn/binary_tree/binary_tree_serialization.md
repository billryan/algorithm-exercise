# Binary Tree Serialization

## Source

- lintcode: [(7) Binary Tree Serialization](http://www.lintcode.com/en/problem/binary-tree-serialization/)

```
Design an algorithm and write code to serialize and deserialize a binary tree.
Writing the tree to a file is called 'serialization'
and reading back from the file to reconstruct
the exact same binary tree is 'deserialization'.
There is no limit of how you deserialize or serialize a binary tree,
you only need to make sure you can serialize a binary tree to a string
and deserialize this string to the original structure.
Have you met this question in a real interview? Yes
Example
An example of testdata: Binary tree {3,9,20,#,#,15,7},
denote the following structure:
  3
 / \
9  20
  /  \
 15   7
Our data serialization use bfs traversal.
This is just for when you got wrong answer and want to debug the input.

You can use other method to do serializaiton and deserialization.
```

## 题解

根据之前由前序，中序，后序遍历恢复二叉树的经验，确定根节点的位置十分重要（但是这里可能有重复元素，故和之前的题目不太一样）。能直接确定根节点的有前序遍历和广度优先搜索，其中较为简洁的为前序遍历。序列化较为简单，但是反序列化的实现不太容易。需要借助字符串解析工具。

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
class Solution {
    /**
     * This method will be invoked first, you should design your own algorithm
     * to serialize a binary tree which denote by a root node to a string which
     * can be easily deserialized by your own "deserialize" method later.
     */
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        if (root == null) return sb.toString();

        seriaHelper(root, sb);

        return sb.substring(0, sb.length() - 1);
    }

    private void seriaHelper(TreeNode root, StringBuilder sb) {
        if (root == null) {
            sb.append("#,");
        } else {
            sb.append(root.val).append(",");
            seriaHelper(root.left, sb);
            seriaHelper(root.right, sb);
        }
    }

    /**
     * This method will be invoked second, the argument data is what exactly
     * you serialized at method "serialize", that means the data is not given by
     * system, it's given by your own serialize method. So the format of data is
     * designed by yourself, and deserialize it here as you serialize it in
     * "serialize" method.
     */
    public TreeNode deserialize(String data) {
        if (data == null || data.length() == 0) return null;

        StringTokenizer st = new StringTokenizer(data, ",");
        return deseriaHelper(st);
    }

    private TreeNode deseriaHelper(StringTokenizer st) {
        if (!st.hasMoreTokens()) return null;

        String val = st.nextToken();
        if (val.equals("#")) {
            return null;
        }

        TreeNode root = new TreeNode(Integer.parseInt(val));
        root.left = deseriaHelper(st);
        root.right = deseriaHelper(st);

        return root;
    }
}
```

### 源码分析

由二叉树序列化的过程不难，难就难在根据字符串进行反序列化，这里引入了 Java 中的 StringTokenizer 字符串分割工具，非常方便，使得递归得以顺利实现。其中`deseriaHelper`的实现较为巧妙。

### 复杂度分析

略

## Reference

- [Serialize and Deserialize a Binary Tree (pre order).](https://gist.github.com/bittib/5620951)
- [Serialization/Deserialization of a Binary Tree | LeetCode](http://articles.leetcode.com/2010/09/serializationdeserialization-of-binary.html)
