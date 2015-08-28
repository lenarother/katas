"""
http://codekata.com/kata/kata02-karate-chop/

"""

def recoursive_chop(elem, elem_list):
	list_len = len(elem_list)
	if list_len == 0:
		return -1
	elif list_len == 1:
		if elem_list[0] == elem:
			return 0
		return -1
	chop_point = int(list_len/2.0)
	if elem_list[chop_point] > elem:
		new_elem_list = elem_list[0:chop_point] 
		return recoursive_chop(elem, new_elem_list)
	else:
		new_elem_list = elem_list[chop_point:]
		new_result = recoursive_chop(elem, new_elem_list)
		if new_result == -1:
			return -1
		return int(list_len/2.0) + new_result
'''
Bugs for recoursive_chop:
- recursively called function needs to be returned
- if the elem is in the second part of the list len of the first part must be added to the result
- but if the result from second half is -1, the it is returned and the len of first hlf should not be added
'''