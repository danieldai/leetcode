def selection_sort(arr):
    n = len(arr)
    # 遍历数组
    for i in range(n):
        # 假设当前元素是最小的
        min_idx = i
        # 找到剩余部分中最小的元素
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # 交换找到的最小元素与当前位置的元素
        arr[i], arr[min_idx] = arr[min_idx], arr[i]