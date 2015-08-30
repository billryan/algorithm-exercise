# Remove Element

## Source

- leetcode: [Remove Element | LeetCode OJ](https://leetcode.com/problems/remove-element/)
- lintcode: [(172) Remove Element](http://www.lintcode.com/en/problem/remove-element/)

```
Given an array and a value, remove all occurrences of that value in place and return the new length.

The order of elements can be changed, and the elements after the new length don't matter.

Example
Given an array [0,4,4,0,0,2,4,4], value=4

return 4 and front four elements of the array is [0,0,0,2]
```

## 题解1 - 使用容器

入门题，返回删除指定元素后的数组长度，使用容器操作非常简单。以 lintcode 上给出的参数为例，遍历容器内元素，若元素值与给定删除值相等，删除当前元素并往后继续遍历。

### C++

```c++
class Solution {
public:
    /**
     *@param A: A list of integers
     *@param elem: An integer
     *@return: The new length after remove
     */
    int removeElement(vector<int> &A, int elem) {
        for (vector<int>::iterator iter = A.begin(); iter < A.end(); ++iter) {
            if (*iter == elem) {
                iter = A.erase(iter);
                --iter;
            }
        }

        return A.size();
    }
};

```

### 源码分析

注意在遍历容器内元素和指定欲删除值相等时，需要先自减`--iter`, 因为`for`循环会对`iter`自增，`A.erase()`删除当前元素值并返回指向下一个元素的指针，一增一减正好平衡。如果改用`while`循环，则需注意访问数组时是否越界。

### 复杂度分析

没啥好分析的，遍历一次数组 $$O(n)$$.
<!--- 没啥好分析的，遍历一次阵列 $$O(n)$$. -->
由于vector每次erase的复杂度是$$O(n)$$，我们遍历整个数组，最坏情况下，每个元素都与要删除的目标元素相等，每次都要删除元素的复杂度高达$$O(n^2)$$
观察此方法会如此低效的原因，是因为我们一次只删除一个元素，导致很多没必要的元素交换移动，如果能够将要删除的元素集中处理，则可以大幅增加效率，见题解2。

### 题解2 - 两根指针

由于题中明确暗示元素的顺序可变，且新长度后的元素不用理会。我们可以使用两根指针分别往前往后遍历，头指针用于指示当前遍历的元素位置，尾指针则用于在当前元素与欲删除值相等时替换当前元素，两根指针相遇时返回尾指针索引——即删除元素后「新数组」的长度。

### C++

```c++
class Solution {
public:
    int removeElement(int A[], int n, int elem) {
        for (int i = 0; i < n; ++i) {
            if (A[i] == elem) {
                A[i] = A[n - 1];
                --i;
                --n;
            }
        }

        return n;
    }
};
```

### 源码分析

遍历当前数组，`A[i] == elem`时将数组「尾部(以 n 为长度时的尾部)」元素赋给当前遍历的元素。同时自减`i`和`n`，原因见题解1的分析。需要注意的是`n`在遍历过程中可能会变化。

### 复杂度分析

同题解1，$$O(n)$$.

## Reference

- [Remove Element | 九章算法](http://www.jiuzhang.com/solutions/remove-element/)
