a = 3
b = 5

end = max(a,b)
start = min(a,b)
sum = 0

for i in range(start, end + 1):
    sum += i
    if start == end :
        return start

return sum