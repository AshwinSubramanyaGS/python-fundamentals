# Variable arguement functions

def top_scorer (*scores):
    if not scores:
        raise ValueError("The scores are empty need atleast 1")
    return max(scores)



maximum = top_scorer(90, 77 , 50, 80, 63, 99) 
print (maximum)