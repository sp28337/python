# Task 1. Patter
# import re
#
# text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'
# starts_wo = re.match(r'wo', text)
#
# if starts_wo:
#     print('[+] "wo"', starts_wo)
# else:
#     print('[-] "wo"', starts_wo)
#
# first_wo = re.search(r'wo', text)
#
# if first_wo:
#     print('[+] "wo"', first_wo)
# else:
#     print('[-] "wo"', first_wo)
#
# print(first_wo.group(0))
# print(first_wo.start())
# print(first_wo.end())
# all_wo = re.findall(r'wo', text)
# if all_wo:
#     print('[+]', all_wo)
# else:
#     print('[-]', all_wo)
#
# print(text)
# print(re.sub(r'wo', r'CHANGE', text))


# Task 2. Escaping special characters
# import re
#
#
# text = (r'How much \wwood+?, would a \wwood+?chuck \dwwood+, '
#         r'chuck if a \wwood+?,chuck could chuck \wwood?,')
#
# lst = re.findall(r"\\wwood\+\?,", text)
# print(lst)
