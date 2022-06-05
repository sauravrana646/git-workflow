# Dummy python code 

def categorize_dict(x, y=0):
    # x Requires string or numerical input
    # y is a boolean that specifices whether to return category names along with the dict.
    # default is no
    cats = list(set(x))
    n = len(cats)
    m = len(x)
    outs = {}
    for i in cats:
        outs[i] = [0]*m
    for i in range(len(x)):
        outs[x[i]][i] = 1
    if y:
        return outs,cats
    return outs