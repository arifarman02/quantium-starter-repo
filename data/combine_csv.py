import glob
import pandas as pd

data_frames = []

csv_files = glob.glob('*.csv')

for csv_file in csv_files:
    sales = pd.read_csv(csv_file)
    data_frames.append(sales)

combined_csv = pd.concat(data_frames, ignore_index=True)

# Filter for pink morsel only
combined_csv = combined_csv[combined_csv['product'] == 'pink morsel']

# Remove the $ sign from price
combined_csv['price'] = combined_csv['price'].str.replace('$', '')

print(combined_csv.dtypes)

# Convert price to float
combined_csv['price'] = combined_csv['price'].astype(float)
combined_csv['sales'] = combined_csv['price'] * combined_csv['quantity']

# Drop the price and quantity columns
combined_csv = combined_csv.drop(['product', 'price', 'quantity'], axis=1)


# Rearrange the position of columns
combined_csv = combined_csv.iloc[:, [2, 0, 1]]
print(combined_csv.head())

# Save cleaned data to a csv file
combined_csv.to_csv('sales.csv', index=False)