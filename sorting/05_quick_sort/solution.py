

def quick_sort(arr):
    # 如果数组长度小于等于1，则无需排序
    if len(arr) <= 1:
        return arr
    else:
        # 选择一个基准元素，通常选择第一个元素
        pivot = arr[0]
        
        # 将数组分成三部分：小于基准、等于基准和大于基准
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        
        # 递归排序子数组，并将结果拼接起来
        return quick_sort(less) + [pivot] + quick_sort(greater)