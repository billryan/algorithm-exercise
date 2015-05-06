# Merge Sort - 归并排序

核心：将两个有序对数组归并成一个更大的有序数组。通常做法为递归排序，并将两个不同的有序数组归并到第三个数组中。

先来看看动图，归并排序是一种典型的分治应用。

![Merge Sort](../images/merge_sort.gif)

```python
#!/usr/bin/env python


class Sort:
    def mergeSort(self, alist):
        if len(alist) <= 1:
            return alist

        mid = len(alist) / 2
        left = self.mergeSort(alist[:mid])
        print("left = " + str(left))
        right = self.mergeSort(alist[mid:])
        print("right = " + str(right))
        return self.mergeSortedArray(left, right)

    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        sortedArray = []
        l = 0
        r = 0
        while l < len(A) and r < len(B):
            if A[l] < B[r]:
                sortedArray.append(A[l])
                l += 1
            else:
                sortedArray.append(B[r])
                r += 1
        sortedArray += A[l:]
        sortedArray += B[r:]

        return sortedArray

unsortedArray = [6, 5, 3, 1, 8, 7, 2, 4]
merge_sort = Sort()
print(merge_sort.mergeSort(unsortedArray))
```

## 原地归并

辅助函数：用于将已排序好的两个数组归并。

```
merge(Comaprable[] a, int lo, int mid, int hi)
{   //将a[lo..mid] 和 a[mid+1..hi] 归并
    int i = lo, j = mid + 1;

    // 拷贝a[lo..hi]原数组至aux中
    for (int k = lo; k <= hi; k++) {
        aux[k] = a[k];
    }

    for (int k = lo; k <= hi; k++) {
        if (i > mid) { //左半边用尽，取右半边元素
            a[k] = aux[j++];
        } else if (j > hi) { //右半边用尽，取左半边元素
            a[k] = aux[i++];
        } else if (less(aux[j], aux[i])) { //右半边的当前元素小于左半边的当前元素，取右半边的元素
            a[k] = aux[j++];
        } else { //右半边的当前元素大于等于左半边的当前元素，取左半边的元素
            a[k] = aux[i++];
        }
    }
}
```

时间复杂度为NlogN，但是空间复杂度为N。

## Reference

- [Mergesort](http://algs4.cs.princeton.edu/22mergesort/) - Robert Sedgewick 的大作，非常清晰。
