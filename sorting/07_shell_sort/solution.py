def shell_sort(arr):
    n = len(arr)
    # 初始的增量（gap）为数组长度的一半
    gap = n // 2

    # 不断缩小增量，直到增量为0
    while gap > 0:
        # 从gap开始遍历数组元素
        for i in range(gap, n):
            # 将arr[i]插入到前面gap距离的有序序列中
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        # 缩小增量
        gap //= 2

# 示例用法
if __name__ == "__main__":
    # 示例数组
    arr = [12, 34, 54, 2, 3]
    
    print("排序前的数组:")
    print(arr)
    
    shell_sort(arr)
    
    print("排序后的数组:")
    print(arr)
