A, B, C = input().split()

if A == B == C:
    print("*")
elif A == B and C != A:
    print("C")
elif A == C and B != A:
    print("B")
elif B == C and A != B:
    print("A")
