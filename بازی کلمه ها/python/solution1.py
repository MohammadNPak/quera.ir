# https://quera.org/problemset/87181/

def words_check(text):
    text = text.split()
    corrected_list=[]
    text_list=[]
    final_dict={}
    for word in text:
        spec_count=0
        for c in word:
            if c.isalpha():
                pass
            else:
                spec_count +=1
            
        if spec_count >= len(word)/2:
            pass
        else:
            corrected_list.append(word)

    for item in corrected_list:
        res=""
        for i in item:
            if i.isalpha():
                res+=i
        text_list.append(res.capitalize())
    text_list.sort()

    for i in text_list:
        final_dict.update({i:text_list.count(i)})
        if text_list.count(i)>1:
            text_list.remove(i)

    return final_dict

