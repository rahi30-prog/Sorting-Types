#The algorithm for Bubble sort.
def BubbleSort(elements, steps = False):
    sorting_steps = [elements[:]]       #Sorting_steps contains a copy of 'elements'
    length = len(elements)
    for i in range(length):     #This loop tracks how many elements have been sorted
        swapped = False         # terminats early if no elements were swapped during an inner loop pass.
        for j in range(0, length-i-1):
            if elements[j] > elements[j + 1]:     #if the first element is greater than the second element then swap the elements(for ascending order only!)
                elements[j], elements[j + 1] = elements[j + 1], elements[j]     #swapping of the elements.
                sorting_steps.append(elements[:])       #Track the list at a particular stage
                swapped = True      #indiactes that a swap has taken place in inner loop
                if not swapped:
                    break
    return sorting_steps if steps else elements #this step is necessary to track the steps of sorting

   
