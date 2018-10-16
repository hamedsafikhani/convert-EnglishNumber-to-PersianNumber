

def enNumbertoPrnumber(enstring):

    dic = {
        '0':'۰',
        '1':'١',
        '2':'٢',
        '3':'۳',
        '4':'۴',
        '5':'۵',
        '6':'۶',
        '7':'۷',
        '8':'۸',
        '9':'۹',
    }



    for i in enstring:
        for j in dic:
            if i == j:
                # print(en.replace(i,dic[j]))
                enstring = enstring.replace(i,dic[j])


    return enstring


# print(enNumbertoPrnumber("""hamed856658safikhani8521
# 686453
# asdg
# 2"""))
