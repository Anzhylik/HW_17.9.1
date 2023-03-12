def sort_list(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums
def bin_search(sort_arr, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if sort_arr[middle] == element:
        return middle
    elif element < sort_arr[middle]:
        return bin_search(sort_arr, element, left, middle - 1)
    else:
        return bin_search(sort_arr, element, middle + 1, right)

try:
    nums = list(map(int, input('Введите числа через пробел:').split()))
    if len(set(nums)) != len(nums):
        nums = list(set(nums))
        print('У Вас есть повторяющиеся числа, но мы их исключили!')
    element = int(input('Введите любое число: '))
    if element not in nums:
        nums.append(element)
    sort_arr = sorted(nums)
    print('Сортировка списка по возрастанию элементов:', sort_arr)
    if element is sort_arr[0]:
        print('Элемент, меньший, чем введенное число, отсутствует')
        print('Номер позиции элемента, большего, чем введенное число:',
              bin_search(sort_arr, element, 0, len(sort_arr) - 1) + 1)
    elif element is sort_arr[-1]:
        print('Номер позиции элемента, меньшего, чем введенное число:',
              bin_search(sort_arr, element, 0, len(sort_arr) - 1) - 1)
        print('Элемент, больший, чем введенное число, отсутствует')
    else:
        print('Номер позиции элемента, меньшего, чем введенное число:',
              bin_search(sort_arr, element, 0, len(sort_arr) - 1) - 1)
        print('Номер позиции элемента, большего, чем введенное число:',
              bin_search(sort_arr, element, 0, len(sort_arr) - 1) + 1)
except ValueError:
    print('Вы ввели букву или символ!')