def arrayOfProducts(array):

    # Time: O(n) | Space: O(n)
    products = [1 for _ in range(len(array))]

    # Filling products array with products of all elements to the left of the current element (i)
    leftProducts = [1 for _ in range(len(array))]

    # Filling rightProducts array with products of all elements to the right of the current element (i)
    rightProducts = [1 for _ in range(len(array))]

    # Filling leftProducts array with products of all elements to the left of the current element
    leftRunningProduct = 1
    for i in range(len(leftProducts)):
        leftProducts[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    
    # Filling rightProducts array with products of all elements to the right of the current element
    rightRunningProduct = 1
    for i in reversed(range(len(rightProducts))):
        rightProducts[i] = rightRunningProduct
        rightRunningProduct *= array[i]

    # Filling products array with products of all elements to the left and right of the current element (i) 
    # This is done by multiplying the leftProducts[i] and rightProducts[i] at each index
    for i in range(len(array)):
        products[i] = leftProducts[i] * rightProducts[i]

    return products

# Example input:
array = [5, 1, 4, 2]
print(arrayOfProducts(array))

# Output: [8, 40, 10, 20]
