# 排列组合

排列组合模板->搜索问题(是否要排序，哪些情况要跳过)

## subsets - 子集

1. [(17) 子集](http://lintcode.com/zh-cn/problem/subsets/)
2. 

### subsets模板(回溯法)

```
void subsets(int[] num) {
    ArrayList<Integer> path = new ArrayList<Integer>();
    Arrays.sort(num);
    subsetsHelper(path, num, 0);
}

void subsetsHelper(ArrayList<Integer> path, int[] num, int pos) {
    outputToResult(path);
    
    for (int i = pos; i < num.length; i++) {
        path.add(num[i]);
        subsetsHelper(path, num, i + 1);
        path.remove(path.size() - 1);
    }
}
```

回溯法可用图示和函数运行的堆栈图来理解。

### subsets调试代码

```
import java.util.*;

class Solution {
    /**
     * @param S: A set of numbers.
     * @return: A list of lists. All valid subsets.
     */
    public static ArrayList<ArrayList<Integer>> subsets(int[] num) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        if (num == null || num.length == 0) {
            return result;
        }
        // write your code here
        
        ArrayList<Integer> list = new ArrayList<Integer>();
        backTrack(result, list, num, 0);
        
        return result;
    }
    
    private static void backTrack(ArrayList<ArrayList<Integer>> result,
        ArrayList<Integer> list, int[] num, int pos) {
	System.out.println("backTrack entrance pos = " + pos);
            
	if (pos == num.length) {
	    return;
	}

	System.out.println("result : " + result);
    result.add(new ArrayList<Integer>(list));
	System.out.println("result.add : " + result);
        for (int i = pos; i < num.length; i++) {
	    System.out.println("backTrack i = " + i);
	    System.out.println("list : " + list);
        list.add(num[i]);
	    System.out.println("list.add : " + list);
        backTrack(result, list, num, pos + 1);
        list.remove(list.size() - 1);
	    System.out.println("list.remove : " + list);
        }
    }

    public static void main(String[] args) {
	//ArrayList<Integer> input = new ArrayList<Integer>();
	//input.add(1);
	//input.add(2);
	//input.add(3);
	int[] input = {1, 2};
	//ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>(subsets(input));
	ArrayList<ArrayList<Integer>> result = subsets(input);
	System.out.println(result);
    }
}
```

以测试数组[1,2]为例分析回溯法的调用栈。

1. 首先由主函数 `subsets` 进入，初始化 `result` 为[]，接着进行异常处理，随后初始化 `list` 为[]，递归调用`backTrack()`。
2. `result`, `list`均为[], `num`为[1, 2], `pos`为0. 调用`result.add()`加入[]。进入`for`循环，`num.length  = 2`。
    1. `i = 0`, 
        1. 的
    2. 的
3. 的