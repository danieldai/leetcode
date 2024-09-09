def counting_sort(arr):
    if not arr:
        return []

    # 找到数组中的最大值
    max_val = max(arr)
    # 创建计数数组，长度为max_val + 1
    count = [0] * (max_val + 1)

    # 计算每个元素的出现次数
    for num in arr:
        count[num] += 1

    # 填充排序后的数组
    sorted_arr = []
    for i, freq in enumerate(count):
        # 根据计数数组构造排序后的数组
        sorted_arr.extend([i] * freq)

    return sorted_arr

# 示例用法
if __name__ == "__main__":
    # 示例数组
    arr = [4, 2, 2, 8, 3, 3, 1]
    
    print("排序前的数组:")
    print(arr)
    
    sorted_arr = counting_sort(arr)
    
    print("排序后的数组:")
    print(sorted_arr)
