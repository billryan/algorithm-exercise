# Find Minimum in Rotated Sorted Array

如前节所述，对于旋转数组的分析可使用画图的方法，如下图所示，升序数组经旋转后可能为如下两种形式。

![Rotated Array](../figure/rotated_array.png)

最小值可能在上图中的两种位置出现，如果仍然使用数组首部元素作为target去比较，则需要考虑图中右侧情况。**使用逆向思维分析，如果使用数组尾部元素分析，则无需图中右侧的特殊情况。**
