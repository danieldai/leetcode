def counting_sort_for_radix(arr, exp):
    """使用计数排序对基数排序中的某一位进行排序"""
    n = len(arr)
    output = [0] * n  # 输出数组
    count = [0] * 10  # 计数数组，范围为0到9

    # 计算每个桶中的数量
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # 计算每个桶的起始位置
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 构造输出数组
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # 将排序后的结果复制到原数组
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    """基数排序函数"""
    # 找到最大值以确定最大位数
    max_val = max(arr)
    
    # 从最小位开始进行排序
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

# 示例用法
if __name__ == "__main__":
    # 示例数组
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    
    print("排序前的数组:")
    print(arr)
    
    radix_sort(arr)
    
    print("排序后的数组:")
    print(arr)
