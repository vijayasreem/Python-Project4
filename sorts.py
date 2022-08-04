class Sorting:
    
    def __init__(self, arr, field: str, method: str=""):
        self.arr = arr
        self.field = field
        self.len = len(arr)

        # if len(arr) < 20:
        #     insertion_sort()
        # else:
        #     heap_sort()

    def selection_sort(self) -> None:
        """
        Mutates lst so that it is sorted via selecting the minimum element and
        swapping it with the corresponding index
        Time complexity: O(n^2); Space complexity: O(1)
        Naive and not stable sorting
        """
        for i in range(self.len):
            min_index = i
            for j in range(i + 1, self.len):
                # Update minimum index
                if self.arr[j] < self.arr[min_index]:
                    min_index = j

            # Swap current index with minimum element in rest of list
            self.arr[min_index], self.arr[i] = self.arr[i], self.arr[min_index]

    def bubble_sort(self) -> None:
        """
        Mutates lst so that it is sorted via swapping adjacent elements until
        the entire lst is sorted.
        Time complexity: O(n^2); Space complexity: O(1)
        Naive and stable sorting
        """
        has_swapped = True
        # if no swap occurred, lst is sorted
        while has_swapped:
            has_swapped = False
            for i in range(self.len - 1):
                if self.arr[i] > self.arr[i + 1]:
                    # Swap adjacent elements
                    self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
                    has_swapped = True

    def insertion_sort(self) -> None:
        """
        Mutates elements in a lst by inserting out of place elements into appropriate
        index repeatedly until lst is sorted
        Time complexity: O(n^2); Space complexity: O(1)
        Useful for small size array or nearly sorted array
        """

        for i in range(1, self.len):
            current_index = i

            while current_index > 0 and self.arr[current_index] < self.arr[current_index - 1]:
                # Swap elements that are out of order
                self.arr[current_index], self.arr[current_index - 1] = \
                    self.arr[current_index - 1], self.arr[current_index]
                current_index -= 1

    def heap_sort(self) -> None:


    def counting_sort(self) -> None:
        """
        Sorts a list of integers where minimum value is 0 and maximum value is K
        Time complexity: O(N+K) - N is size of input, K is the maximum number in arr; Space complexity: O(N)
        better when sorting numbers - id, account_number
        """
        K = max(self.arr)
        counts = [0 for _ in range(K + 1)]
        for element in self.arr:
            counts[element] += 1

        # we now overwrite our original counts with the starting index
        # of each element in the final sorted array

        starting_index = 0
        for i, count in enumerate(counts):
            counts[i] = starting_index
            starting_index += count

        sorted_lst = [0 for _ in range(self.len)]

        for element in self.arr:
            sorted_lst[counts[element]] = element
            # since we have placed an item in index counts[element], we need to
            # increment counts[element] index by 1 so the next duplicate element
            # is placed in appropriate index
            counts[element] += 1

        # common practice to copy over sorted list into original lst
        # it's fine to just return the sorted_lst at this point as well
        for i in range(self.len):
            self.arr[i] = sorted_lst[i]

    def