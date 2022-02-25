# https://leetcode.com/problems/sort-list/

def sort(sorted_lst, lst):
    try:
        current = lst[0]

        for ele in lst:
            if ele < current:
                current = ele
    
        sorted_lst.append(current)    # Updating lists.
        lst.remove(current)

        # if nothing to sort, stop... else keep sorting.
        return sorted_lst if lst == [] else sort(sorted_lst, lst)
    
    except IndexError:    # NOTE: This error only shows up for empty lists.
        return []

# --- Test Cases ---

print(sort([], [-1,5,3,4,0]))
print(sort([], []))
print(sort([], [5, 4, 3, 2, 1]))
print(sort([], list(range(10))[::-1]))
print(sort([], list(range(100))[::-1]))