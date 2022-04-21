a = list(map(int, input().split()))
if not a:
    print(0)
else:
    sum_dict={}
    for i in range(len(a)+1):
        for j in range(i+1,len(a)+1):
            sum_dict[tuple(a[i:j])]=sum(a[i:j])
    keys=list(sum_dict.keys())
    values=list(sum_dict.values())
    max_value_index=values.index(max(values))
    print(*keys[max_value_index])

