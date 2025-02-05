# Yunis Nabiyev
# 2/3/25
# Python Homework 1
# Section 04

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
    print(permutations, "| Possibilities:", len(permutations))
    print()

    print("a) All results are the same")
    a = same_results(permutations, 4)
    print(a)
    print()
    print("b) Exactly one head occurs")
    b = exactly_one(permutations, "H")
    print(b)
    print()
    print("c) At least two heads occur")
    c = atleast_two(permutations, "H")
    print(c)
    print()
    
    print("Calculate P(a), P(b), and P(c)")
    print(f"P(a) = {len(a)}/{len(permutations)}")
    print(f"P(b) = {len(b)}/{len(permutations)}")
    print(f"P(c) = {len(c)}/{len(permutations)}")
    print("Add P(a), P(b), and P(c)")
    print(f"{len(a)}/{len(permutations)} + {len(b)}/{len(permutations)} + {len(c)}/{len(permutations)} = {len(a)+len(b)+len(c)}/{len(permutations)}")
    print()

    print("2. Obtain the sample space of an experiment that consists of a fair coin tossed 5 times.")
    permutations = sample_space(["H","T"], 5)
    print(permutations, "| Possibilities:", len(permutations))
    print()

    print("a) All results are the same")
    a = same_results(permutations, 5)
    print(a)
    print()
    print("b) Exactly one head occurs")
    b = exactly_one(permutations, "H")
    print(b)
    print()
    print("c) At least two heads occur")
    c = atleast_two(permutations, "H")
    print(c)
    print()
    
    print("Calculate P(a), P(b), and P(c)")
    print(f"P(a) = {len(a)}/{len(permutations)}")
    print(f"P(b) = {len(b)}/{len(permutations)}")
    print(f"P(c) = {len(c)}/{len(permutations)}")
    print("Add P(a), P(b), and P(c)")
    print(f"{len(a)}/{len(permutations)} + {len(b)}/{len(permutations)} + {len(c)}/{len(permutations)} = {len(a)+len(b)+len(c)}/{len(permutations)}")
    print()

    

if __name__ == "__main__":
    main()