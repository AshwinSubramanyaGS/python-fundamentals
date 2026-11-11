import copy

original = [ ["Rahul", 85], ["Priya", 90]]
copied = copy.deepcopy(original)
shallow_copy = original.copy()
copied[0][1] = 95
print("Original:",original)
print("Deep copy",copied)

shallow_copy[0][1] = 25
print("Original:",original)
print("Shallow copy",shallow_copy)