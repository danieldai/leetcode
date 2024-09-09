def merge_sort(arr):
    # 如果数组长度大于1，则继续分割
    if len(arr) > 1:
        # 找到数组的中间点
        mid = len(arr) // 2
        
        # 分割数组
        L = arr[:mid]
        R = arr[mid:]
        
        # 递归调用归并排序对左右两半分别排序
        merge_sort(L)
        merge_sort(R)
        
        # 初始化三个指针
        i = j = k = 0
        
        # 合并左右两半
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # 将剩余的元素放回原数组
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
