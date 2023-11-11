input=[1,2,4,5,6,8,9,11,13,15]

def missing_number(input):
    n=len(input)+1
    expected_sum=n*(n+1)//2
    actual_sum=sum(input)
    return expected_sum-actual_sum

def missing_number_set(input):
    n=max(input)
    expected_set=set(range(1,n+1))
    actual_set=set(input)
    return set(expected_set-actual_set)

def missing_number_list(input):
    n=max(input)
    expected_list=list(range(1,n+1))
    actual_list=list(input)
    return (x for x in expected_list if x not in actual_list)

out=missing_number_list(input)
print(out)