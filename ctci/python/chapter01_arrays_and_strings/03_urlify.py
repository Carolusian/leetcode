# Solution:
#  The basic idea is to traverse backward as enough empty slots is reserved 
#  thinks blow strings:
#  _I_am_Ali
#  _I_am_Ali______   (6 more slots added for extra character)
#  
#  will be changed 
#  _I_am_Ali___Ali 
#  _I_am_Ali%20Ali
#  _I_am_Alm%20Ali
#  ..
#  %20I%20am%20Ali

import unittest


def urlify_common(s: str, length: int) -> str:
    # the traverse backward way

    # make `s` mutable first, and expand the capacity
    old_len = len(s)
    s = list(s) + [' '] * (length - len(s))
    
    index = length - 1
    for i in reversed(range(old_len)):
        if s[i] == ' ':
            s[index] = '0'
            s[index - 1] = '2'
            s[index - 2] = '%'
            index = index - 3
        else:
            s[index] = s[i]
            index = index - 1

    return "".join(s)
        

def urlify_pythonic(s: str, length: int) -> str:
    return "%20".join(s.split())


class Test(unittest.TestCase):
    test_cases = (
        ("I am Ali", 12, "I%20am%20Ali"),
    )

    test_funcs = (
        urlify_pythonic,
        urlify_common
    )

    def test_urlify(self):
        for test_case in self.test_cases:
            s, length, expected = test_case
            for func in self.test_funcs:
                result = func(s, length)
                assert result == expected, f"expected: {expected}"


if __name__ == "__main__":
    unittest.main()
