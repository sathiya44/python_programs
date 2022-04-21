def get_combination(words,n):
    words=sorted(words)
    items=list(range(len(words)))
    old_combination=[[]]
    new_combinations=[]
    for i in range(n):
        new_combinations=[]
        for combination in old_combination:
            for item in items:
                if (combination and item>  combination[-1] or len(combination)==0):
                    new_combination.append(combination+[item])
            old_combination=new_combinations
    word_combinations=[]
    for combination in new_combinations:
        word_combination=[]
        for index in combination:
            word_combination.append(word[index])
        word_combinations.append(tuple(word_combination))
    return sorted(set(word_combinations))

    


n=input().split()
length=len(n)
for i in range(1,length+1):
    all_combination=get_combination(n,i)
    for combination in all_combination:
        print(" ".join(combination))
