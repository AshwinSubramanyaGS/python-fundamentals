import pandas as pd

df = pd.DataFrame({
"name": ["Rahul", "Priya", "Kiran", "Meera"],
"department": ["IT", "HR", "IT", "HR"],
"score": [85, 90, 75, 95]
})
result = df.groupby("department")["score"].mean()

print(result)