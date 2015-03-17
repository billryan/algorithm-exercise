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