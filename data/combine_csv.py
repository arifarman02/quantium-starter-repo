import glob
import pandas as pd

data_frames = []

csv_files = glob.glob('*.csv')

for csv_file in csv_files:
    sales = pd.read_csv(csv_file)
    data_frames.append(sales)

combined_csv = pd.concat(data_frames, ignore_index=True)

combined_csv.to_csv('sales.csv', index=False)