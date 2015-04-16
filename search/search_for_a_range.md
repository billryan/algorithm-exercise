# Search for a Range

Question: [(61) Search for a Range](http://www.lintcode.com/en/problem/search-for-a-range/)

题解：

由上题二分查找可找到满足条件的左边界，因此只需要再将右边界找出即可。注意到在`(target == nums[mid]`时赋值语句为`end = mid`，将其改为`start = mid`即可找到右边界，解毕。

```
/**
 * 本代码fork自九章算法。没有版权欢迎转发。
 * http://www.jiuzhang.com/solutions/search-for-a-range/
 */
public class Solution {
    /**
     *@param A : an integer sorted array
     *@param target :  an integer to be inserted
     *return : a list of length 2, [index1, index2]
     */
    public ArrayList<Integer> searchRange(ArrayList<Integer> A, int target) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        int start, end, mid;
        result.add(-1);
        result.add(-1);

        if (A == null || A.size() == 0) {
            return result;
        }

        // search for left bound
        start = 0;
        end = A.size() - 1;
        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (A.get(mid) == target) {
                end = mid; // set end = mid to find the minimum mid
            } else if (A.get(mid) > target) {
                end = mid;
            } else {
                start = mid;
            }
        }
        if (A.get(start) == target) {
            result.set(0, start);
        } else if (A.get(end) == target) {
            result.set(0, end);
        } else {
            return result;
        }

        // search for right bound
        start = 0;
        end = A.size() - 1;
        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (A.get(mid) == target) {
                start = mid; // set start = mid to find the maximum mid
            } else if (A.get(mid) > target) {
                end = mid;
            } else {
                start = mid;
            }
        }
        if (A.get(end) == target) {
            result.set(1, end);
        } else if (A.get(start) == target) {
            result.set(1, start);
        } else {
            return result;
        }

        return result;
        // write your code here
    }
}
```

源码分析：

1. 首先对输入做异常处理，数组为空或者长度为0
2. 初始化 `start, end, mid`三个变量，注意mid的求值方法，可以防止两个整型值相加时溢出
3. **使用迭代而不是递归**进行二分查找
4. while终止条件应为`start + 1 < end`而不是`start <= end`，`start == end`时可能出现死循环
5. 先求左边界，迭代终止时先判断`A.get(start) == target`，再判断`A.get(end) == target`，因为迭代终止时target必取start或end中的一个，而end又大于start，取左边界即为start.
6. 再求右边界，迭代终止时先判断`A.get(end) == target`，再判断`A.get(start) == target`
