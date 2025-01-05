import pandas as pd

# 1. 讀取原始 CSV 檔案，假設資料中有 'latitude', 'longitude', 'sentiment_score' 欄位
input_csv_path = r'path/to/your/file.csv'  # 輸入你的CSV檔案路徑
output_csv_path = r'output/path/to/your/file.csv'  # 輸出結果的CSV檔案路徑

# 讀取CSV檔案
df = pd.read_csv(input_csv_path)

# 2. 檢查資料的基本情況
print("原始資料：")
print(df.head())  # 顯示資料的前幾行，檢查是否包含所需的欄位

# 3. 處理缺失值
# 去除 'sentiment_score' 欄位為 NaN 的資料
df = df.dropna(subset=['sentiment_score'])
print("\n處理缺失值後的資料：")
print(df.head())  # 再次檢查資料

# 4. 計算每個經緯度的情緒分數平均值
df_avg = df.groupby(['latitude', 'longitude'])['sentiment_score'].mean().reset_index()

# 5. 儲存計算結果為新的 CSV 檔案
df_avg.to_csv(output_csv_path, index=False)

# 6. 顯示計算後的結果
print(f"\n情緒分析平均值已經儲存至 {output_csv_path}")
print(df_avg.head())  # 顯示計算後的前幾行結果
