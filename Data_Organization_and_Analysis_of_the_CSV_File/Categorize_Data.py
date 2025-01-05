import pandas as pd

# 讀取 CSV 檔案
df = pd.read_csv(r'path/to/your/file.csv')

# 增加一個新欄位，標記原始資料中的行號
df['original_index'] = df.index

# 根據 'location' 欄位進行排序
df_sorted = df.sort_values(by='location')

# 儲存整理後的 CSV 檔案
df_sorted.to_csv(r'path/to/your/file/sorted_file.csv', index=False)

print("資料已經按照地理位置排序並儲存，並標記了原始排序位置。")