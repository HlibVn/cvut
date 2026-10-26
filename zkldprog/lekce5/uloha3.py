import math
data = [2, 4, 4, 4, 5, 5, 7, 9]
def mean(values):
    return(sum(values)/len(values))
print(mean(data))
def median(values):
    s=sorted(values)
    if len(values)%2==1:
        return s[n//2]
    else:
        m2=s[len(values)//2-1]
        m1=s[len(values)//2]
        return(m1+m2)/2
print(median(data))
def std_dev(values):
    m=mean(values)
    s=0
    for i in values:
        s += (i-m)**2
    return(math.sqrt(s/(len(values)-1)))
print(std_dev(data))
def min_max(values):
    min=values[0]
    max=values[0]
    for i in values:
        if i>max:
            max=i
        if i<min:
            min=i
    return(min,max)
print(min_max(data))
def summary(values):
    min, max = min_max(values)
    return f"mean = {mean(values)}, median = {median(values)}, std_dev = {std_dev(values):.3f}, min = {min}, max = {max}"

print(summary(data))