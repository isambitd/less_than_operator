def get_index(l):
    try:
        if isinstance(l, list):
            if len(l) == 0:
                return None
            i = 0
            j = len(l) - 1
            while i < j:

                if l[i] < l[i+1]:
                    return i
                if l[j] < l[j-1]:
                    return j
                i += 1
                j -= 1
            return i
        else:
            return None
    except:
        return None

def get_minimum(l):
    try:
        if isinstance(l, list):
            if len(l) == 0:
                return None
            i = 0
            j = len(l) - 1
            while i < j:

                if l[i] < l[i+1]:
                    return l[i]
                if l[j] < l[j-1]:
                    return l[j]
                i += 1
                j -= 1
            return l[i]
        else:
            return None
    except:
        return None
