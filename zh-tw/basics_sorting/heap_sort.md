# Heap Sort - 堆排序

堆排序通常基於[**二元堆** ](http://algorithm.yuanbin.me/zh-hans/basics_data_structure/heap.html)實現，以大根堆(根結點為最大值)爲例，堆排序的實現過程分爲兩個子過程。第一步爲取出大根堆的根節點(當前堆的最大值), 由於取走了一個節點，故需要對餘下的元素重新建堆。重新建堆後繼續取根節點，循環直至取完所有節點，此時數組已經有序。基本思想就是這樣，不過實現上還是有些小技巧的。

## 堆的操作

以大根堆爲例，堆的常用操作如下。

1. 最大堆調整（Max_Heapify）：將堆的末端子節點作調整，使得子節點永遠小於父節點
2. 創建最大堆（Build_Max_Heap）：將堆所有數據重新排序
3. 堆排序（HeapSort）：移除位在第一個數據的根節點，並做最大堆調整的遞歸運算

其中步驟1是給步驟2和3用的。

![Heapsort-example](../../shared-files/images/Heapsort-example.gif)

建堆時可以自頂向下，也可以採取自底向上，以下先採用自底向上的思路分析。我們可以將數組的後半部分節點想象爲堆的最下面的那些節點，由於是單個節點，故顯然滿足二叉堆的定義，於是乎我們就可以從中間節點向上逐步構建二叉堆，每前進一步都保證其後的節點都是二叉堆，這樣一來前進到第一個節點時整個數組就是一個二叉堆了。下面用 C++/Java 實現一個堆的類。C++/Java 中推薦使用 PriorityQueue 來使用堆。

堆排在空間比較小(嵌入式設備和手機)時特別有用，但是因爲現代系統往往有較多的快取，堆排序無法有效利用快取，數組元素很少和相鄰的其他元素比較，故快取未命中的機率遠大於其他在相鄰元素間比較的算法。但是在大數據的排序下又重新發揮了重要作用，因爲它在插入操作和刪除最大元素的混合動態場景中能保證對數級別的運行時間。

### C++

```c++
#include <iostream>
#include <vector>

using namespace std;

class HeapSort {
	// get the parent node index
	int parent(int i) {
		return (i - 1) / 2;
	}

	// get the left child node index
	int left(int i) {
		return 2 * i + 1;
	}

	// get the right child node index
	int right(int i) {
		return 2 * i + 2;
	}

	// build max heap
	void build_max_heapify(vector<int> &nums, int heap_size) {
		for (int i = heap_size / 2; i >= 0; --i) {
			max_heapify(nums, i, heap_size);
		}
		print_heap(nums, heap_size);
	}

	// build min heap
	void build_min_heapify(vector<int> &nums, int heap_size) {
		for (int i = heap_size / 2; i >= 0; --i) {
			min_heapify(nums, i, heap_size);
		}
		print_heap(nums, heap_size);
	}

	// adjust the heap to max-heap
	void max_heapify(vector<int> &nums, int k, int len) {
		// int len = nums.size();
		while (k < len) {
			int max_index = k;
			// left leaf node search
			int l = left(k);
			if (l < len && nums[l] > nums[max_index]) {
				max_index = l;
			}
			// right leaf node search
			int r = right(k);
			if (r < len && nums[r] > nums[max_index]) {
				max_index = r;
			}
			// node after k are max-heap already
			if (k == max_index) {
				break;
			}
			// keep the root node the largest
			int temp = nums[k];
			nums[k] = nums[max_index];
			nums[max_index] = temp;
			// adjust not only just current index
			k = max_index;
		}
	}

	// adjust the heap to min-heap
	void min_heapify(vector<int> &nums, int k, int len) {
		// int len = nums.size();
		while (k < len) {
			int min_index = k;
			// left leaf node search
			int l = left(k);
			if (l < len && nums[l] < nums[min_index]) {
				min_index = l;
			}
			// right leaf node search
			int r = right(k);
			if (r < len && nums[r] < nums[min_index]) {
				min_index = r;
			}
			// node after k are min-heap already
			if (k == min_index) {
				break;
			}
			// keep the root node the largest
			int temp = nums[k];
			nums[k] = nums[min_index];
			nums[min_index] = temp;
			// adjust not only just current index
			k = min_index;
		}
	}

public:
	// heap sort
	void heap_sort(vector<int> &nums) {
		int len = nums.size();
		// init heap structure
		build_max_heapify(nums, len);
		// heap sort
		for (int i = len - 1; i >= 0; --i) {
			// put the largest number int the last
			int temp = nums[0];
			nums[0] = nums[i];
			nums[i] = temp;
			// reconstruct heap
			build_max_heapify(nums, i);
		}
		print_heap(nums, len);
	}

	// print heap between [0, heap_size - 1]
	void print_heap(vector<int> &nums, int heap_size) {
		for (int i = 0; i < heap_size; ++i) {
			cout << nums[i] << ", ";
		}
		cout << endl;
	}
};

int main(int argc, char *argv[])
{
	int A[] = {19, 1, 10, 14, 16, 4, 7, 9, 3, 2, 8, 5, 11};
	vector<int> nums;
	for (int i = 0; i < sizeof(A) / sizeof(A[0]); ++i) {
		nums.push_back(A[i]);
	}

	HeapSort sort;
	sort.print_heap(nums, nums.size());
	sort.heap_sort(nums);

	return 0;
}
```

### Java

```java
import java.util.*;

public class HeapSort {
    // sign = 1 ==> min-heap, sign = -1 ==> max-heap
    private void siftDown(int[] nums, int k, int size, int sign) {
        int half = (size >>> 1);
        while (k < half) {
            int index = k;
            // left leaf node search
            int l = (k << 1) + 1;
            if (l < size && (sign * nums[l]) < (sign * nums[index])) {
                index = l;
            }
            // right leaf node search
            int r = l + 1;
            if (r < size && (sign * nums[r]) < (sign * nums[index])) {
                index = r;
            }
            // already heapify
            if (k == index) break;
            // keep the root node the smallest/largest
            int temp = nums[k];
            nums[k] = nums[index];
            nums[index] = temp;
            // adjust next index
            k = index;
        }
    }

    private void heapify(int[] nums, int size, int sign) {
        for (int i = size / 2; i >= 0; i--) {
            siftDown(nums, i, size, sign);
        }
    }

    private void minHeap(int[] nums, int size) {
        heapify(nums, size, 1);
    }

    private void maxHeap(int[] nums, int size) {
        heapify(nums, size, -1);
    }

    public void sort(int[] nums, boolean ascending) {
        if (ascending) {
            // build max heap
            maxHeap(nums, nums.length);
            // heap sort
            for (int i = nums.length - 1; i >= 0; i--) {
                int temp = nums[0];
                nums[0] = nums[i];
                nums[i] = temp;
                // reconstruct max heap
                maxHeap(nums, i);
            }
        } else {
            // build min heap
            minHeap(nums, nums.length);
            // heap sort
            for (int i = nums.length - 1; i >= 0; i--) {
                int temp = nums[0];
                nums[0] = nums[i];
                nums[i] = temp;
                // reconstruct min heap
                minHeap(nums, i);
            }
        }
    }

    public static void main(String[] args) {
        int[] A = new int[]{19, 1, 10, 14, 16, 4, 4, 7, 9, 3, 2, 8, 5, 11};
        HeapSort heapsort = new HeapSort();
        heapsort.sort(A, true);
        for (int i : A) {
            System.out.println(i);
        }
    }
}
```

### 複雜度分析

從程式碼中可以發現堆排最費時間的地方在於構建二叉堆的過程。

上述構建大根堆和小根堆都是自底向上的方法，建堆過程時間複雜度爲 $$O(2N)$$, 堆化過程(可結合圖形分析，最多需要調整的層數爲最大深度)時間複雜度爲 $$\log i$$, 故堆排過程中總的時間複雜度爲 $$O(N \log N)$$.

先看看建堆的過程，畫圖分析(比如以8個節點爲例)可知在最壞情況下，每次都需要調整之前已經成爲堆的節點，那麼就意味着有二分之一的節點向下比較了一次，四分之一的節點向下比較了兩次，八分之一的節點比較了三次... 等差等比數列求和，具體過程可參考下面的連結。

## Reference

- [堆排序 - 維基百科，自由的百科全書](http://zh.wikipedia.org/wiki/%E5%A0%86%E6%8E%92%E5%BA%8F)
- [Priority Queues](http://algs4.cs.princeton.edu/24pq/) - Robert Sedgewick 的大作，詳解了關於堆的操作。
- [經典排序算法總結與實現 | Jark's Blog](http://wuchong.me/blog/2014/02/09/algorithm-sort-summary/) - 堆排序講的很好。
- *Algorithm* - Robert Sedgewick
- [堆排序中建堆過程時間複雜度O(n)怎麼來的？](http://www.zhihu.com/question/20729324)
- [《大話數據結構》第9章 排序 9.7 堆排序（上） - 伍迷 - 博客園](http://www.cnblogs.com/cj723/archive/2011/04/21/2024261.html)
- [《大話數據結構》第9章 排序 9.7 堆排序（下） - 伍迷 - 博客園](http://www.cnblogs.com/cj723/archive/2011/04/22/2024269.html)
