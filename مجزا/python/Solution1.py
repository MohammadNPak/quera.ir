def separator(ls):

    # even = []
    # odd = []

    # for i in ls:
    #     if i%2==0:
    #         even.append(i)

    # for i in ls:
    #     if i%2!=0:
    #         odd.append(i)

    return ([x for x in ls if x % 2 == 0], [x for x in ls if x % 2 != 0])
