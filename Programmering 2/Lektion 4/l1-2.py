def List(list):
    newList = []
    for element in list:
        newElement = pow(element, 2)
        newList.append(newElement)
    return newList
print(List([1,2,3,4,5,6]))