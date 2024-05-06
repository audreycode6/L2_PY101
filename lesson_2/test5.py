# 5. a function that takes two lists of numbers and returns the result of merging the lists. 
# The elements of the first list should become the elements at the even indexes of the returned list, 
# while the elements of the second list should become the elements at the odd indexes. 
# For instance: merge([1, 2, 3], [4, 5, 6]) # => [1, 4, 2, 5, 3, 6]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
# GET 2 list of ints
def merge(list1, list2):
    # SET/READ zip_list --> use zip to merge lists
    zip_list = zip(list1, list2)
    # SET/READ new_list lists merged as list of tuples
    new_list = list(zip_list)
    # SET merge_list = to append values of tuple
    merge_list = []
    
    # WHILE for items in new_list index items from tuple and append to merge_list
    for element1, element2 in new_list:
        merge_list.append(element1)
        merge_list.append(element2)
    # PRINT merge_list
    return merge_list

print(merge(list1, list2))
