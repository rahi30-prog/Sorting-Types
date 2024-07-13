def BubbleSort(elements, steps=False):
    sorting_steps = [elements[:]]  # sorting_steps contains a copy of 'elements'
    length = len(elements)

    for i in range(length - 1):  # This loop tracks how many elements have been sorted
        swapped = False  # terminates early if no elements were swapped during an inner loop pass

        for j in range(0, length - i - 1):
            if elements[j] > elements[j + 1]:  # if the first element is greater than the second element then swap the elements(for ascending order only!)
                elements[j], elements[j + 1] = elements[j + 1], elements[j]  # swapping of the elements.
                swapped = True  # indicates that a swap has taken place in the inner loop

        if steps:
            sorting_steps.append(elements[:])  # Track the list at the end of each outer loop iteration

        if not swapped:
            break
        
    return sorting_steps if steps else elements  # this step is necessary to track the steps of sorting
