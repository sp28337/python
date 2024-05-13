# nums = [x for x in range(1, 101) if x % 10 == 0]
# new_nums = nums[:]
# new_nums[3] = 0
#
# for i in range(2, 8):
#     print(nums[i], end=' ')
#
# print()
#
# for i in range(2, 8):
#     print(new_nums[i], end=' ')


# def is_palindrom(num_list):
#     reverse_list = num_list[::-1]
#     if num_list == reverse_list:
#         return True
#     else:
#         return False
#
#
# nums = [1, 2, 3, 4, 3, 2]
# answer = []
#
# for i in range(0, len(nums)):
#     if is_palindrom(nums[i:len(nums)]):
#         answer = nums[:i]
#         answer.reverse()
#         break
#
# print(f"Based list: {nums}")
# print(f"Need numbers for palindrome: {len(answer)}")
# print(f"List of these numbers: {answer}")


# import random
# original_prices = [random.randint(-100, 101) for x in range(5)]
# new_prices1 = [x for x in original_prices if x < 0]
# print("Мы потеряли: ", abs(sum(new_prices1)))


# nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
# print(nums[:5])
# print(nums[:-2])
# print(nums[::2])
# print(nums[1::2])
# print(nums[::-1])
# print(nums[-1:0:-2])


# import random
# nums = [random.randint(-100, 101) for x in range(10)]
# print(nums)
# b_num = random.randint(0, 9)
# a_num = random.randint(0, b_num)
# print(a_num)
# print(b_num)
# nums = nums[:a_num] + nums[b_num + 1:]
# print(nums)