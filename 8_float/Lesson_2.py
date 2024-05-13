# chatles = int(input('Enter how much chatles do you have: '))
# cr_we_have = chatles / 2200
# cr = 1
# print(f"This is {cr_we_have} CR")
# ship = cr / 2
# print(f"You can bay {cr_we_have // ship} ship(s)")


# print('Enter coordinates of the figure')
# horizontal = float(input('Horizontal coordinates: '))
# vertical = float(input('Vertical coordinates: '))
# if 0 <= horizontal < 1 and 0 <= vertical < 1:
#     print(f"Figure is at point({int(horizontal * 10)}, {int(vertical * 10)})")
# else:
#     print(f'There are not such coordinates like {horizontal}, {vertical}')
# fix_h = int(horizontal * 1000) % (int(horizontal * 10) * 100)
# fix_v = int(vertical * 1000) % (int(vertical * 10) * 100)
# if fix_h != 50 or fix_v != 50:
#     print(f"Change figure place on ({(50 - fix_h) / 10 ** 3}, {(50 - fix_v) / 10 ** 3})")