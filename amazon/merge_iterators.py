from typing import List, Iterator


def merge_two_iterators(itr1: Iterator, itr2: Iterator) -> List:
    """
    Merge two sorted iterators, return a list
    """

    result = []
    elem1, elem2 = next(itr1), next(itr2)

    def rest_elems(itr):
        for _, el in enumerate(itr):
            result.append(el)

    while True:
        if elem1 < elem2:
            result.append(elem1)
            try:
                elem1 = next(itr1)
            except StopIteration:
                result.append(elem2)
                rest_elems(itr2)
                return result
        elif elem1 == elem2:
            result.append(elem1)
            result.append(elem2)
            try:
                elem1 = next(itr1)
            except StopIteration:
                rest_elems(itr2)
                return result

            try:
                elem2 = next(itr2)
            except StopIteration:
                rest_elems(itr1)
                return result
        else:
            result.append(elem2)
            try:
                elem2 = next(itr2)
            except StopIteration:
                result.append(elem1)
                rest_elems(itr1)
                return result


# optimise the algorithm to merge multiple iterators to a single iterator
import operator
from collections import defaultdict

def imerge_iterators(*iterators):
    """
    Merge multiple iterators into a single iterator
    """
    
    # [next_value, index, iterator]
    ptr = defaultdict()
    for idx, itr in enumerate(iterators):
        try:
            ptr[idx] = [next(itr), idx, itr]
        except StopIteration:
            pass

    # get value function
    get_func = operator.itemgetter(1)
    while ptr:
        idx, itr_ptr = min(ptr.items(), key=get_func)
        value, _, itr = itr_ptr
        yield value
        try:
            itr_ptr[0] = next(itr)
        except StopIteration:
            # reach the end of the iteration
            del ptr[idx]


import unittest
import heapq

class MergeIteratorsTestCase(unittest.TestCase):

    def test_merge_two_iterators(self):
        result1 = merge_two_iterators(iter([1, 3, 4]), iter([2, 4, 5, 6, 7]))
        result2 = merge_two_iterators(iter([2, 3, 5, 100, 101]), iter([1, 2, 6, 7]))
        self.assertEqual(result1, [1, 2, 3, 4, 4, 5, 6, 7])
        self.assertEqual(result2, [1, 2, 2, 3, 5, 6, 7, 100, 101])

    def test_imerge_iterators(self):
        result1 = list(imerge_iterators(iter([1, 3, 4]), iter([2, 4, 5, 6, 7])))
        result2 = list(imerge_iterators(iter([2, 3, 5, 100, 101]), iter([1, 2, 6, 7])))

        compare1 = list(heapq.merge(iter([1, 3, 4]), iter([2, 4, 5, 6, 7])))
        compare2 = list(heapq.merge(iter([2, 3, 5, 100, 101]), iter([1, 2, 6, 7])))

        self.assertEqual(result1, compare1) 
        self.assertEqual(result2, compare2)
        

if __name__ == '__main__':
    unittest.main()

