# Bubble Sort - 氣泡排序

核心：**氣泡**，持續比較相鄰元素，大的挪到後面，因此大的會逐步往後挪，故稱之為氣泡。

![Bubble Sort](../../shared-files/images/bubble_sort.gif)

## Implementation

### Python

```python
#!/usr/bin/env python


def bubbleSort(alist):
    for i in xrange(len(alist)):
        print(alist)
        for j in xrange(1, len(alist) - i):
            if alist[j - 1] > alist[j]:
                alist[j - 1], alist[j] = alist[j], alist[j - 1]

    return alist

unsorted_list = [6, 5, 3, 1, 8, 7, 2, 4]
print(bubbleSort(unsorted_list))
```

### Java

```java
public class Sort {
	public static void main(String[] args) {
		int unsortedArray[] = new int[]{6, 5, 3, 1, 8, 7, 2, 4};
		bubbleSort(unsortedArray);
		System.out.println("After sort: ");
		for (int item : unsortedArray) {
			System.out.print(item + " ");
		}
	}

	public static void bubbleSort(int[] array) {
		int len = array.length;
		for (int i = 0; i < len; i++) {
			for (int item : array) {
				System.out.print(item + " ");
			}
			System.out.println();
			for (int j = 1; j < len - i; j++) {
				if (array[j - 1] > array[j]) {
					int temp = array[j - 1];
					array[j - 1] = array[j];
					array[j] = temp;
				}
			}
		}
	}
}
```

###C++
```C++
void bubbleSort(vector<int> & arr){
    for(int i = 0; i < arr.size(); i++){
        for(int j = 1; j < arr.size() - i; j++){
            if(arr[j - 1] > arr[j])){
                std::swap(arr[j-1], arr[j]);
            }
        }
    }
    return arr;
}
```

### 複雜度分析

平均情況與最壞情況均為 $$O(n^2)$$, 使用了 temp 作為臨時交換變量，空間複雜度為 $$O(1)$$.
可以做適當程度的優化，當某一次外迴圈中發現陣列已經有序，就跳出迴圈不再執行，但這僅對於部分的輸入有效，平均及最壞時間複雜度仍為$$O(n^2)$$

```C++
void bubbleSort(vector<int> & arr){
    bool unsorted = true;
    for(int i = 0; i < arr.size() && unsorted; i++){
        unsorted = false;
        for(int j = 1; j < arr.size() - i; j++){
            if(arr[j - 1] > arr[j])){
                std::swap(arr[j-1], arr[j]);
                unsorted = true;
            }
        }
    }
    return arr;
}
```

## Reference

- [氣泡排序 - 維基百科，自由的百科全書](http://zh.wikipedia.org/wiki/%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F)
