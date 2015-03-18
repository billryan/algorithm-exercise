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
        Array.sort(num);
        backTrack(result, list, num, 0);
        
        return result;
    }
    
    private static void backTrack(ArrayList<ArrayList<Integer>> result,
        ArrayList<Integer> list, int[] num, int pos) {
        
        result.add(new ArrayList<Integer>(list));
        
        for (int i = pos; i < num.length; i++) {
            list.add(num[i]);
            backTrack(result, list, num, i + 1);
            list.remove(list.size() - 1);
        }
    }

    public static void main(String[] args) {
	    int[] input = {1, 2};
        ArrayList<ArrayList<Integer>> result = subsets(input);
    }
}
```
以测试数组[1,2]为例分析回溯法的调用栈。

1. 首先由主函数 `subsets` 进入，初始化 `result` 为[]，接着进行异常处理，随后初始化 `list` 为[]，递归调用`backTrack()`, `num = [1, 2]`。
2. `result = [], list = [], pos = 0`. 调用`result.add()`加入[], `result = [[]]`。进入`for`循环，`num.length  = 2`。
    1. `i = 0`, 
        1. `list.add(num[0]) -> list = [1]`, 递归调用`backTrack()`前, `result = [[]], list = [1], pos = 1`
        2. 递归调用`backTrack([[]], [1], 2，1)`
            1. `reslut.add[[1]] -> result = [[], [1]]`
            2. `i = 1`, for(i = 1 < 2)
                - `list.add(num[1]) -> list = [1, 2]`
                - 递归调用`backTrack([[], [1]], [1, 2], 2，2)`
                    + `reslut.add[[1, 2]] -> result = [[], [1], [1, 2]]`
                - `list.remove(2 - 1) -> list = [1]`
                - `i++ -> i = 2`
            3. `i = 2`, 退出for循环，退出此次调用
        3. `list.remove() -> list = []`
        4. `i++ -> i = 1`，进入下一次循环
    2. `i = 1`, for(i = 1 < 2)
        - `list.add(num[1]) -> list = [2]`
        - 递归调用`backTrack([[], [1], [1, 2]], [2], 2，2)`
            + `reslut.add[[2]] -> result = [[], [1], [1, 2], [2]]`
            + `i = 2` 退出循环
        - `list.remove(1 - 1) -> list = []`
        - `i++ -> i = 2`
    3. `i = 2`, 退出for循环。
3. 的