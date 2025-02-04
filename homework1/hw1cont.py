# Yunis Nabiyev
# 2/3/25
# Python Homework 1 Continued
# Section 04


# 1. Obtain the sample space of an experiment that consists of a fair coin tossed 4 times. Consider the following events:
# a) All four results are the same
# b) Exactly one head occurs
# c) At least two heads occur

# Calculate P(a), P(b), and P(c)
# Add P(a) + P(b) + P(c) = 17/16 (?)

# 2. Flipped 5 times (2^5 = 32 possibilities)

def sample_space(possibilities:list[str], times:int):
    '''Returns a list of all permutations of 'possibilities' rolled 'times' amount '''
    perms:list[str] = [""]

    for _ in range(times):
        this_iteration:list[str] = perms[::1]
        for existing in perms:
            for possibility in possibilities:
                this_iteration.append(existing+possibility)
            this_iteration.remove(existing)
        perms = this_iteration[::1]

    return perms

def same_results(perms:list[str], times:int):
    '''Returns a subset of 'perms' where all 'times' results are the same'''
    subset:list[str] = []
    for perm in perms:
        if perm == perm[0]*times:
            subset.append(perm)
    return subset

def exactly_one(perms:list[str], target:str):
    '''Returns a subset of 'perms' where exactly one occurance of 'target' exists'''
    subset:list[str] = []
    for perm in perms:
        if perm.count(target) == 1:
            subset.append(perm)
    
    return subset

def atleast_two(perms:list[str], target:str):
    '''Returns a subset of 'perms' where at least two occurances of 'target' exists'''
    subset:list[str] = []
    for perm in perms:
        if perm.count(target) >= 2:
            subset.append(perm)
    
    return subset


def main():
    print("1. Obtain the sample space of an experiment that consists of a fair coin tossed 4 times.")
    permutations = sample_space(["H","T"], 4)
    print(permutations, "| Length:", len(permutations)) # ['HHHH', 'HHHT', 'HHTH', 'HHTT', 'HTHH', 'HTHT', 'HTTH', 'HTTT', 'THHH', 'THHT', 'THTH', 'THTT', 'TTHH', 'TTHT', 'TTTH', 'TTTT']

    print("a) All four results are the same")
    print(same_results(permutations, 4))# 'HHHH', 'TTTT'
    print("b) Exactly one head occurs")
    print(exactly_one(permutations, "H"))# 'HTTT', 'THTT', 'TTHT', 'TTTH'
    print("c) At least two heads occur")
    print(atleast_two(permutations, "H"))# 'HHHH', 'HHHT', 'HHTH', 'HHTT', 'HTHH', 'HTHT', 'HTTH', 'THHH', 'THHT', 'THTH', 'TTHH'
    
    # Calculate P(a), P(b), and P(c)
        # P(a) = 2/16 
        # P(b) = 4/16
        # P(c) = 11/16
    # Add P(a) + P(b) + P(c) = 17/16
        # 2/16 + 4/16 + 11/16 = 17/16

    print("2. Obtain the sample space of an experiment that consists of a fair coin tossed 5 times.")
    permutations = sample_space(["H","T"], 5)
    print(permutations, "| Length:", len(permutations)) #

if __name__ == "__main__":
    main()