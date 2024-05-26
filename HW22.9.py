try:
    array = list(map(float, input("Введите последовательность чисел в любом порядке, через пробел: ").split()))
    element = float(input("Введите любое число из заданного диапазона: "))
except ValueError:
    print('Ошибка! Пожалуйста, вводите только числа!')
else:
    def bubble_sorting(array):
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array


    def binary_search(array, element, left, right):
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] >= element and array[middle - 1] < element:
            return middle - 1
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)


    print('Сортированный список', bubble_sorting(array))
    left = float(array[0])
    right = float(array[-1])
    if element < left or element > right:
        print('Числа нет в диапазоне')
    else:
        print('Индекс элемента, ближайшего минимального от введенного числа ',
              binary_search(array, element, 0, len(array) - 1))