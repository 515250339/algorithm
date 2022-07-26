import random

"""
1. 从第一个元素开始，该元素可以认为已经被排序；
2. 取出下一个元素，在已经排序的元素序列中从后向前扫描；
3. 如果该元素（已排序）大于新元素，将该元素移到下一位置；
4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
5. 将新元素插入到该位置后；
6. 重复步骤2~5。
"""


def insert_sort(li):
    """
    插入排序 时间复杂度 O(n²)  空间复杂度O(1)
    :param li:
    :return:
    """
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j = j - 1
        li[j + 1] = tmp


li = [random.randint(0, 100) for i in range(10)]
print(li)
insert_sort(li)
print(li)
