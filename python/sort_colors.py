def merge_sort(sample_list: list):
    if len(sample_list) < 2:
        return
    else:
        mid = len(sample_list) // 2
        left = [sample_list[i] for i in range(mid)]
        right = [sample_list[i] for i in range(mid, len(sample_list))]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sample_list[k] = left[i]
                i += 1
            else:
                sample_list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            sample_list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            sample_list[k] = right[j]
            j += 1
            k += 1


def sortColors(nums: list[int]):
    merge_sort(nums)
