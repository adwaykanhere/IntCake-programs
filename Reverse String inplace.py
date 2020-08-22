# Code to program Reverse characters in list inplace
def revcharinplace():
    charlist = ["a","d","w","a","y","k"]
    lastindex = len(charlist)

    if lastindex % 2 != 0:
        lastindex1 = (lastindex-1)//2
    else:
        lastindex1 = (lastindex)//2
    # 5 -> 0 4 -> 1 3 -> 2 2 -> 3 1 -> 4 0 -> 5
    for i in range(lastindex1):
        temp = charlist[i]
        charlist[i] = charlist[lastindex - 1 - i]
        charlist[lastindex -1 - i] = temp

    print(charlist)
revcharinplace()


