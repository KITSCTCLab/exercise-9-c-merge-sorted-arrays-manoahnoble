from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
  new_arr_1 = nums1[0:m]
  new_arr_2 = nums2[0:n]
  sorted_array = []
  i = 0
  j = 0
  k = 0     
  while i < len(new_arr_1) and j < len(new_arr_2):
      if new_arr_1[i] <= new_arr_2[j]:
        sorted_array[k] = new_arr_1[i]
        i += 1
      else:
          sorted_array[k] = new_arr_2[j]
          j += 1
      k += 1

  while i < len(new_arr_1):
      sorted_array[k] = new_arr_1[i]
      i += 1
      k += 1

  while j < len(new_arr_2):
      sorted_array[k]=new_arr_2[j]
      j += 1
      k += 1
  nums1 = sorted_array
  
# Do not change the following code
nums1 = []
nums2 = []
for item in input().split(', '):
  nums1.append(int(item))
for item in input().split(', '):
  nums2.append(int(item))
m = int(input())
n = int(input())
merge(nums1, m, nums2, n)
print(nums1)
