def linear_search(arr,val):
    for i in range(len(arr)):
        if arr[i] ==val:
            return "found"
    return "not found" 
print(linear_search([10,4,5,6,8,23,56,77],83))           