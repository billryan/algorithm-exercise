# Heap Sort - 堆排序

堆排序通常基于[**二叉堆** ](http://algorithm.yuanbin.me/zh-hans/basics_data_structure/heap.html)实现，以大根堆为例，堆排序的实现过程分为两个子过程。第一步为取出大根堆的根节点(当前堆的最大值), 由于取走了一个节点，故需要对余下的元素重新建堆。重新建堆后继续取根节点，循环直至取完所有节点，此时数组已经有序。基本思想就是这样，不过实现上还是有些小技巧的。

## 堆的操作

以大根堆为例，堆的常用操作如下。

1. 最大堆调整（Max_Heapify）：将堆的末端子节点作调整，使得子节点永远小于父节点
2. 创建最大堆（Build_Max_Heap）：将堆所有数据重新排序
3. 堆排序（HeapSort）：移除位在第一个数据的根节点，并做最大堆调整的递归运算

其中步骤1是给步骤2和3用的。

![Heapsort-example](../../shared-files/images/Heapsort-example.gif)

建堆时可以自顶向下，也可以采取自底向上，以下先采用自底向上的思路分析。我们可以将数组的后半部分节点想象为堆的最下面的那些节点，由于是单个节点，故显然满足二叉堆的定义，于是乎我们就可以从中间节点向上逐步构建二叉堆，每前进一步都保证其后的节点都是二叉堆，这样一来前进到第一个节点时整个数组就是一个二叉堆了。下面用 C++/Java 实现一个堆的类。C++/Java 中推荐使用 PriorityQueue 来使用堆。

堆排在空间比较小(嵌入式设备和手机)时特别有用，但是因为现代系统往往有较多的缓存，堆排序无法有效利用缓存，数组元素很少和相邻的其他元素比较，故缓存未命中的概率远大于其他在相邻元素间比较的算法。但是在海量数据的排序下又重新发挥了重要作用，因为它在插入操作和删除最大元素的混合动态场景中能保证对数级别的运行时间。TopM

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

### 复杂度分析

从代码中可以发现堆排最费时间的地方在于构建二叉堆的过程。

上述构建大根堆和小根堆都是自底向上的方法，建堆过程时间复杂度为 $$O(2N)$$, 堆化过程(可结合图形分析，最多需要调整的层数为最大深度)时间复杂度为 $$\log i$$, 故堆排过程中总的时间复杂度为 $$O(N \log N)$$.

先看看建堆的过程，画图分析(比如以8个节点为例)可知在最坏情况下，每次都需要调整之前已经成为堆的节点，那么就意味着有二分之一的节点向下比较了一次，四分之一的节点向下比较了两次，八分之一的节点比较了三次... 等差等比数列求和，具体过程可参考下面的链接。

## Reference

- [堆排序 - 维基百科，自由的百科全书](http://zh.wikipedia.org/wiki/%E5%A0%86%E6%8E%92%E5%BA%8F)
- [Priority Queues](http://algs4.cs.princeton.edu/24pq/) - Robert Sedgewick 的大作，详解了关于堆的操作。
- [经典排序算法总结与实现 | Jark's Blog](http://wuchong.me/blog/2014/02/09/algorithm-sort-summary/) - 堆排序讲的很好。
- *Algorithm* - Robert Sedgewick
- [堆排序中建堆过程时间复杂度O(n)怎么来的？](http://www.zhihu.com/question/20729324)
- [《大话数据结构》第9章 排序 9.7 堆排序（上） - 伍迷 - 博客园](http://www.cnblogs.com/cj723/archive/2011/04/21/2024261.html)
- [《大话数据结构》第9章 排序 9.7 堆排序（下） - 伍迷 - 博客园](http://www.cnblogs.com/cj723/archive/2011/04/22/2024269.html)
