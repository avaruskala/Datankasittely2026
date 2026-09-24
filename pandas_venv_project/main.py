import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [25, 30, 35, 28],
    "City": ["Helsinki", "Stockholm", "Oslo", "Copenhagen"],
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Full DataFrame:")
print(df)
