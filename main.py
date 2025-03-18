k , n = map (int , input().split())

i = 1 
list = []
while i <= k and len(list) <= k-1 :
    list = list + [1]
    if len(list) <= k-1 :
        list = list +[0]
    i = i + 1

b = n - i + 1
i = 1
c = 1
while i <= b :
    #list [c] = 1
    if c < len(list):
        list[c] = 1
    c = c + 2
    i = i + 1
# print (b)
# print (list)

i = 0
count = 0
while i < k - 1 :
    d = i + 1
    if list[i] == list[d] == 1 :
        count = count + 1
    i = i + 1

if k%2 == 0 and n > k/2 and k != n :
    count = count - 1

if k == 2 and n == 1 :
    count = 0




#print (list)
print (count)
