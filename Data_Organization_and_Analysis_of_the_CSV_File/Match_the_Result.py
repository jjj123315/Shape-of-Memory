import os
import shutil
import pandas as pd

# 讀取CSV檔案，並提取 'original_index' 和 'location' 欄位
csv_file = r'D:\重要資料\桌面\新增資料夾\馬祖\關鍵字401-600.csv'  # 替換為你的CSV檔案路徑
file2 = pd.read_csv(csv_file)

# 圖片資料夾路徑
image_folder = r'D:\重要資料\桌面\all'  # 替換為圖片所在資料夾的路徑

# 目標資料夾路徑
target_folder = r'D:\重要資料\桌面\新增資料夾\馬祖\sorted_images_3'  # 替換為你想創建新資料夾的路徑

# 確保目標資料夾存在
os.makedirs(target_folder, exist_ok=True)

# 列出圖片資料夾中的所有檔案，幫助我們檢查
image_files_in_folder = os.listdir(image_folder)
print(f'資料夾中存在的圖片檔案：{image_files_in_folder}')

# 遍歷csv檔案中的 'original_index' 和 'location'
for index, row in file2.iterrows():
    original_index = row['original_index']
    location = row['location']  # 'location' 這欄會用來創建資料夾
    
    # 根據original_index找到對應的圖片檔案名
    image_name = f'image_{original_index}_gradient_direction'  # 圖片名稱格式（不包含 .jpg）
    image_path = os.path.join(image_folder, image_name + '.png')  # 假設圖片是 .png 格式，根據實際情況調整
    
    # 檢查圖片是否存在於資料夾中
    if image_name + '.png' in image_files_in_folder:
        print(f'找到圖片：{image_name}.png')

        # 根據original_index找到對應的圖片檔案，並移動圖片
        destination_folder = os.path.join(target_folder, str(location))
        
        # 確保資料夾存在
        os.makedirs(destination_folder, exist_ok=True)
        print(f'已創建資料夾：{destination_folder}')

        # 定義新圖片的儲存路徑
        new_image_path = os.path.join(destination_folder, image_name + '.png')
        
        # 移動圖片
        try:
            shutil.move(image_path, new_image_path)
            print(f'圖片 {image_name}.png 已成功移動到 {new_image_path}')
        except Exception as e:
            print(f'移動圖片 {image_name}.png 失敗: {e}')
    else:
        print(f'圖片 {image_name}.png 不存在於資料夾中')

print("所有對應圖片處理完成。")