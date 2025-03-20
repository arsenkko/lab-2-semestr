import unittest

def binary_search(nums, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def suma(nums, target):
    nums.sort() 
    size = len(nums)

    for i in range(size - 2):  
        for j in range(i + 1, size - 1):  
            required_value = target - (nums[i] + nums[j])
            
            if binary_search(nums, j + 1, size - 1, required_value):
                return True

    return False
class TestContainsThreeNumbersWithSum(unittest.TestCase):
    def test_triplet_found(self):
        self.assertTrue(suma([2, 4, 6], 12))

    def test_no_triplet_found(self):
        self.assertFalse(suma([3, 5, 7, 9], 25))

    def test_unsorted_input(self):
        self.assertTrue(suma([8, 1, 6], 15))

if __name__ == "__main__":
    unittest.main()