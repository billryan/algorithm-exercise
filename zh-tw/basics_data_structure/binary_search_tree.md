# Binary Search Tree - 二元搜尋樹

定義：

一顆**二元搜尋樹(BST)**是一顆二元樹，其中每個節點都含有一個可進行比較的鍵(key)及相應的值(value)，且每個節點的鍵都**大於等於左子樹中的任意節點的鍵**，而**小於右子樹中的任意節點的鍵**。

使用中序遍歷可得到有序數組，這是二元搜尋樹的又一個重要特徵。

二元搜尋樹使用的每個節點含有**兩個**鏈接，它是將鏈表插入的靈活性和有序數組搜尋的高效性結合起來的高效符號表實現。

二元樹中每個節點只能有一個父節點(根節點無父節點)，只有左右兩個連結，分別為**左子節點**和**右子節點**。

## 基本實現

節點包含
- 一個鍵
- 一個值
- 一條左鏈接
- 一條右鏈接

```c++
template<typename Key, typename Value>
struct BSTNode{
    Key key;
    Value val;
    BSTNode* left;
    BSTNode* right;
    BSTNode(Key k, Value v, BSTNode* l = NULL, BSTNode* r = NULL)
        :key(k), val(v), left(l), right(r){}
};
```
