import unittest2


def add(a, b):
    # return a - b
    return a + b


class AddTest(unittest2.TestCase):

    def test_add(self):
        self.assertEquals(add(1, 1), 2)
        self.assertEquals(add(5, 2), 7)
        self.assertEquals(add(-1, -6), -7)

if __name__ == '__main__':
    unittest2.main()
