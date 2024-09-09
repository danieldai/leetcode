def insertion_sort(arr):
    # 从第二个元素开始，逐个插入
    for i in range(1, len(arr)):
        key = arr[i]
        # 将当前元素与前面已排序的部分进行比较，找到合适的位置插入
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # 将大于key的元素向后移动
            j -= 1
        arr[j + 1] = key  # 将当前元素插入到合适的位置
