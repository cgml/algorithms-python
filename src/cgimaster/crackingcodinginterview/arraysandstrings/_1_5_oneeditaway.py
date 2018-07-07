def one_edit_away(s1,s2):
    if s1 == s2: return True
    if abs(len(s1)-len(s2))>1: return False
    editCounter = 0
    is1 =0
    is2 =0
    while is1<len(s1) and is2<len(s2) and editCounter < 2:
        if s1[is1]==s2[is2]:
            editCounter-=1
        elif len(s2)>is2+1 and s1[is1] == s2[is2+1]:
            is2+=1
        elif len(s1)>is1+1 and s1[is1+1]==s2[is2]:
            is1+=1
        editCounter+=1
        is1+=1
        is2+=1

    return editCounter+(len(s1)-is1 + len(s2)-is2)<2


assert one_edit_away("pale","ple")
assert one_edit_away("pale","pake")
assert not one_edit_away("pale","bake")