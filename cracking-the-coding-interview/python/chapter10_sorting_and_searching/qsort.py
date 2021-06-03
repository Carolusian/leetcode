def qsort(l):
    if len(l) <= 1:
        return l
    return qsort([lt for lt in l if lt < l[0]]) + l[0:1] + \
            qsort([ge for ge in l if ge >= l[0]])
