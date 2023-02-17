def compare(str1,str2):
    f,s=1,1
    while (str1 != "") and (str2!= ""):
        if ord(str1[0])<ord(str2[0]):
            str1=str1[1:]
            str1=str1[::-1]
            if str1 != "":
                str2=str2[::-1]
        if str1!="":
            if ord(str1[0])>ord(str2[0]):
                str2=str2[1:]
                str2=str2[::-1]
                if str2 != "":
                    str1=str1[::-1]
        if str1!="" and str2!="":
            if ord(str1[0])==ord(str2[0]):
                str1=str1[1:]
                str2=str2[1:]
    if (str1 == "") and (str2 !=""):
        print(str2)
    if (str2 == "") and (str1 != ""):
        print(str1)
    if (str1 == "") and (str2 == ""):
        print('Both strings are empty!')

compare(input(),input())