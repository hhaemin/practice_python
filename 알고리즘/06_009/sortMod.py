def sortNumber(ns, asc=True):

    if asc:
        for i1 in range(1, len(ns)):
            i2 = i1 - 1
            cNum = ns[i1]

            while ns[i2] > cNum and i2 >= 0:
                ns[i2 + 1] = ns[i2]
                i2 -= 1

            ns[i2+1] = cNum
    else:
        for i1 in range(1, len(ns)):
            i2 = i1 - 1
            cNum = ns[i1]

            while ns[i2] < cNum and i2 >= 0:
                ns[i2 + 1] = ns[i2]
                i2 -= 1

            ns[i2 + 1] = cNum

    return ns


# def sortNumber(ns, asc=True):
#
#     for i1 in range(1, len(ns)):
#         i2 = i1 - 1
#         cNum = ns[i1]
#
#         if asc:
#             while ns[i2] > cNum and i2 >= 0:
#                 ns[i2 + 1] = ns[i2]
#                 i2 -= 1
#         else:
#             while ns[i2] < cNum and i2 >= 0:
#                 ns[i2 + 1] = ns[i2]
#                 i2 -= 1
#
#         ns[i2+1] = cNum
#
#     return ns