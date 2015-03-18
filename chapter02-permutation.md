# 排列组合

排列组合模板->搜索问题(是否要排序，哪些情况要跳过)

## backtrack(回溯法)

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
