def bubble_sort(elements):
    size = len(elements)
   

    for j in range(size-1):

        swapped = False

        for i in range(size-1-j):

            if elements[i] > elements[i+1]:
                elements[i],elements[i+1]
                elements[i],elements[i+1] = elements[i+1],elements[i]

                swapped = True


        if not swapped:
            break           




if __name__ =='__main__':
    elements =[10,9,8,7,6,5,4,3,2]
    bubble_sort(elements)

    print(elements)
