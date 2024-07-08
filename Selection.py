def SelectionSort(array, steps = False): #If size parameter is declared here, in the test section, I will have to add size parameter diffrently!!
    size = len(array) 
    sorted_steps = [array[:]]  #List to store the sortes steps


    for position in range(size-1):
        smallest_element = position #Assume the element at first position is smallest.

        for j in range(position + 1, size):   #step + 1 because the 0th element is set to smallest element.
            if array[smallest_element] > array[j]:  #Checking if the smallest elements is truly the smallest.

                smallest_element = j     #Not array[j] because we want to keep track of the position of the element & not the value.

        array[smallest_element], array[position] = array[position], array[smallest_element] #Swapping the positions of the smallest element & first place.

        if steps:
            sorted_steps.append(array[:])   #Track the list at a particular stage.

    return sorted_steps if steps else array #Tracks the steps of selection sorting.