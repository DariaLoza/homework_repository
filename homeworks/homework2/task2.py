"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.
You may assume that the array is non-empty and the most common element
always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3, 2
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""


def major_and_minor_elem(el_list):
    """This function find the most common and the least common elements"""
    condition = len(el_list) / 2
    for element in el_list:
        if el_list.count(element) >= condition:
            return element, min(set(el_list), key=el_list.count)