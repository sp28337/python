#for i in range(1, 10):
#    for j in range(1, 10):
#        print(f"{i} * {j} = {i * j}")
#    print()


# def calculator(n1, n2, s):
#     if s == '+':
#         print(f"{n1} {s} {n2} =", n1 + n2)
#     elif s == '-':
#         print(f"{n1} {s} {n2} =", n1 - n2)
#     elif s == '*':
#         print(f"{n1} {s} {n2} =", n1 * n2)
#     elif s == '/':
#         print(f"{n1} {s} {n2} =", n1 / n2)
#
#
# s = input('Enter operation: ')
# while True:
#     if s == '+' or s == '-' or s == '*' or s == '/':
#         number_a = float(input('Enter first number: '))
#         number_b = float(input('Second number: '))
#         calculator(number_a, number_b, s)
#         break
#     else:
#         print('Error! Try again!')
#         s = input('Enter operation: ')