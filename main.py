# https://leetcode.com/problems/sort-list/

def sort(sorted_lst, lst):
    try:
        current = lst[0]

        for ele in lst:
            if ele < current:
                current = ele
    
        sorted_lst.append(current)
        lst.remove(current)

        return sorted_lst if lst == [] else sort(sorted_lst, lst)
    except IndexError:
        return []

print(sort([], [-1,5,3,4,0]))
print(sort([], []))
print(sort([], [5, 4, 3, 2, 1]))