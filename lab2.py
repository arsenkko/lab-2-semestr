def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                nums[k] = left_half[i]
                i += 1
            else:
                nums[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            nums[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            nums[k] = right_half[j]
            j += 1
            k += 1

def binary_search(nums, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True, nums[mid]
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False, None

def suma(nums, target):
    merge_sort(nums)
    size = len(nums)
    
    for i in range(size - 2):  
        for j in range(i + 1, size - 1):  
            required_value = target - (nums[i] + nums[j])
            
            found, third_number = binary_search(nums, j + 1, size - 1, required_value)
            if found:
                print(f"Трійка знайдена: {nums[i]}, {nums[j]}, {third_number}")
                return True
    
    print("Трійка не знайдена")
    return False

nums = [9, 0, 1, 18, 20, 7]
target = 10
suma(nums, target)