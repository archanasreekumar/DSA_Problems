class SelectionSort:

    def arr_sort(self, array):
        n = len(array)
        for i in range(n - 1): #range(n) itself will itr till n-1 only.
            min_index = i
            for j in range(i, n):
                if array[j] < array[min_index]:
                    min_index = j
            array[i], array[min_index] = array[min_index], array[i]
        return array


ss = SelectionSort()
print(ss.arr_sort([1, 3, 6, 10, 4]))
