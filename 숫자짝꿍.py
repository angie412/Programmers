x = "55225"
y = "122255"


new_num = []
xcnt = 0
ycnt = 0
for xnum in x :
    for ynum in y:
        if xnum == ynum:
            xcnt = x.count(xnum)
            ycnt = y.count(ynum)      
            if xcnt > ycnt :
                new_num.append(xnum)  
            elif xcnt < ycnt :
                new_num.append(xnum)
            elif xcnt == ycnt :
                new_num.append(xnum)
        
print(new_num)
new_list = []
xnum_cnt = 0
ynum_cnt = 0
       
print(new_list)

if "0" in new_num :
    print("0")


for xnum in x :
    for ynum in y :
        if xnum and ynum == "0":
            print("0")



