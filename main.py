def mergeSort(n):
  if len(n) == 1 or len(n) == 0: #makes sure its not 1 or 0
    return n
  else: #if it is not one or zero it splits list
    mid = len(n) // 2
    left, right = mergeSort(n[:mid]), mergeSort(n[mid:])
    return merger(left, right)
    
def merger(left, right):
  index1 = 0 # variables used to compare list indexes
  index2 = 0
  sortedList = [] # creating sorted list

  for i in range(len(left) + len(right)): #compares for each number
    if index1 != len(left) and index2 != len(right): #checking if at end of list
      if left[index1] > right[index2]: #comparing indexes
        sortedList.append(right[index2]) # adding lower value to sorted list
        index2 += 1 #increasing to look at next index
      else:
        sortedList.append(left[index1]) 
        index1 += 1
    elif index1 == len(left): #if no value to compare too it adds it to the sorted list
      sortedList.append(right[index2])
      index2 += 1
    elif index2 == len(right):
      sortedList.append(left[index1])
      index1 += 1
    print()
    print(sortedList) #sorted list 
  return sortedList # returns sorted list

myList = [11,7,10,15,2,50] # test list
print("unsorted: " + str(myList)) #unsorted
print()
print(mergeSort(myList)) #sorted list