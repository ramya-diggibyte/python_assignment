def second_max_number(arr):
   return (sorted(list(set(arr)))[-2]) #set removes the duplicates and sorted (by default sort in ascending) and slicing done based on index
