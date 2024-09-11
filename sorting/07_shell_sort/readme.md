原理：基于插入排序的思想，将元素按一定间隔分组，然后对每组进行插入排序，逐步缩小间隔，最后进行全体排序。 时间复杂度：O(n log n)（具体取决于间隔序列）

希尔排序的特点：
时间复杂度：希尔排序的时间复杂度取决于选择的增量序列。最坏情况下的时间复杂度为 O(n²)，但在实际应用中通常比 O(n²) 的排序算法（如冒泡排序、插入排序）要快。使用合适的增量序列（如 Hibbard 增量、Sedgewick 增量），可以将时间复杂度降低到 O(n^(3/2)) 或 O(n log² n)。
空间复杂度：希尔排序的空间复杂度为 O(1)，因为它是原地排序算法，不需要额外的存储空间。
不稳定性：希尔排序是不稳定的排序算法，因为相同元素的相对位置可能会改变。

https://www.bilibili.com/video/BV1eg411w7gn?p=36&vd_source=dead283aa3efb297fb9f9c1d2b8e9fe8

一种基于插入排序的快速的排序算法。简单插入排序对于大规模乱序数组很慢,因为元素只
能一点一点地从数组的一端移动到另一端。
希尔排序为了加快速度简单地改进了插入排序,也称为缩小增量排非序,同时该算法是冲破
O(n^2)的第一批算法之一。
希尔排序是把记录按下表的一定增量分组,对每组使用直接插入排非序算法排序;然后缩小增
量继续分组排序,随着增量逐渐减少,每组包含的关键词越来越多多,当增量减至1时,整个文
件恰被分成一组,再次排序,完成整个数组的排序。这个不断缩小的增量,就构成了一个增
量序列。