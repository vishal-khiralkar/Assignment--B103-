#1. Find the second-largest unique element in an array without using sort() or max().
def second_largest(nums):
    first = second = float('-inf')

    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return second if second != float('-inf') else None

print(second_largest([10, 20, 30, 30, 40]))


#2. Find all pairs in an array whose sum equals a given target.

def find_pairs(nums, target):
    seen = set()
    pairs = set()

    for num in nums:
        comp = target - num

        if comp in seen:
            pairs.add((min(num, comp), max(num, comp)))

        seen.add(num)

    return list(pairs)

print(find_pairs([1, 2, 3, 4, 5], 6))

# #3. Move all zeros to the end of an array without changing the order of other elements.

def move_zeros(nums):
    pos = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1

    return nums

print(move_zeros([0, 1, 0, 3, 12]))

#4. Find the missing number from an array containing numbers from 1 to N.

def missing_number(nums):
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2

    return expected_sum - sum(nums)

print(missing_number([1, 2, 4, 5]))

#5. Find all duplicate elements in a list without using nested loops.

def find_duplicates(nums):
    seen = set()
    dups = set()

    for num in nums:
        if num in seen:
            dups.add(num)

        seen.add(num)

    return list(dups)

print(find_duplicates([1, 2, 3, 2, 4, 3, 5]))

#6. Find the first non-repeating character in a string.

from collections import Counter

def first_unique_char(s):
    counts = Counter(s)

    for ch in s:
        if counts[ch] == 1:
            return ch

    return None

print(first_unique_char("programming"))

#7. Check whether two strings are anagrams without using sorted().

from collections import Counter

def is_anagram(s1, s2):
    return len(s1) == len(s2) and Counter(s1) == Counter(s2)

print(is_anagram("listen", "silent"))

#8. Merge two sorted arrays without using sort().

def merge_sorted(a, b):
    res = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1

    res.extend(a[i:])
    res.extend(b[j:])

    return res

print(merge_sorted([1, 3, 5], [2, 4, 6]))

#9. Rotate an array to the right by K positions.

def rotate_right(nums, k):
    n = len(nums)

    if n == 0:
        return nums

    k %= n

    def reverse(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)

    return nums

print(rotate_right([1, 2, 3, 4, 5], 2))

#10. Find the intersection of two arrays, including duplicate occurrences.

from collections import Counter

def intersect(nums1, nums2):
    counts = Counter(nums1)
    res = []

    for num in nums2:
        if counts[num] > 0:
            res.append(num)
            counts[num] -= 1

    return res

print(intersect([1, 2, 2, 3], [2, 2, 4]))


#11. Find the maximum sum of a contiguous subarray.

def max_subarray_sum(nums):
    if not nums:
        return 0

    curr_sum = max_sum = nums[0]

    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)

    return max_sum

print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


#12. Find the longest substring without repeating characters.

def length_of_longest_substring(s):
    seen = {}
    left = max_len = 0

    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1

        seen[ch] = right
        max_len = max(max_len, right - left + 1)

    return max_len

print(length_of_longest_substring("abcabcbb"))

#13. Find the longest common prefix among multiple strings.
def longest_common_prefix(strs):
    if not strs:
        return ""

    for i, ch in enumerate(strs[0]):
        for s in strs[1:]:
            if i >= len(s) or s[i] != ch:
                return strs[0][:i]

    return strs[0]

print(longest_common_prefix(["flower", "flow", "flight"]))


#14. Group a list of strings into anagram groups.

from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)

    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)

    return list(groups.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


#15. Find the Kth largest element in an unsorted array.

import heapq

def find_kth_largest(nums, k):
    if k < 1 or k > len(nums):
        return None

    heap = nums[:k]
    heapq.heapify(heap)

    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)

    return heap[0]

print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))


#16. Check whether a given string contains balanced parentheses using a stack.

def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in "({[":
            stack.append(ch)

        elif ch in ")}]":
            if not stack or stack.pop() != mapping[ch]:
                return False

        else:
            return False

    return len(stack) == 0

print(is_valid_parentheses("{[()]}"))


#17. Find all subarrays whose sum equals a given target.
from collections import defaultdict

def find_subarrays_sum(nums, target):
    prefix_map = defaultdict(list)
    prefix_map[0].append(-1)

    curr_sum = 0
    result = []

    for i, num in enumerate(nums):
        curr_sum += num

        if curr_sum - target in prefix_map:
            for start_idx in prefix_map[curr_sum - target]:
                result.append(nums[start_idx + 1:i + 1])

        prefix_map[curr_sum].append(i)

    return result

print(find_subarrays_sum([1, 2, 3, -2, 2], 3))


#18. Merge overlapping intervals in a list.

def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged = [[intervals[0][0], intervals[0][1]]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged

print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))

# 19. Search for an element in a rotated sorted array.

def search_rotated(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1

    return -1

print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))



# 20. Find the longest consecutive sequence in an unsorted array.

def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:
            curr = num
            streak = 1
            while curr + 1 in num_set:
                curr += 1
                streak += 1
            longest = max(longest, streak)
    return longest

print(longest_consecutive([100, 4, 200, 1, 3, 2]))
