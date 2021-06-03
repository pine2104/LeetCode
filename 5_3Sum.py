## two pointer method


def three_sum(nums): ## time complexicity O(n^2)
    nums.sort()
    n = len(nums)
    result = []
    if n <= 2:
        return result
    for i in range(0, n - 2):
        a = nums[i]
        if i > 0 and a == nums[i-1]: ## if a = previous a, skip this loop
            continue
        j, k = i + 1, n - 1
        while k > j:
            b = nums[j]
            c = nums[k]
            if a + b + c > 0:
                k -= 1
            elif a + b + c < 0:
                j += 1
            else:
                result += [[a, b, c]]
                k -= 1
                j += 1
                while j<k and nums[j]==nums[j-1]: ## if b = previous b, change to next
                    j += 1
                while j<k and nums[k]==nums[k+1]: ## if c = previous c, change to next
                    k -= 1
    return result

nums = [1,0,-1]
nums = [-1,0,1,2,-1,-4]
nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
nums = [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]
nums = [-2,0,1,1,2]

result = three_sum(nums)