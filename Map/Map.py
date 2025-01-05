import pandas as pd
import folium
from folium.plugins import MarkerCluster

# 讀取你的情緒分析資料
df = pd.read_csv(r'path/to/your/file.csv')  # 假設這是你的資料來源

# 定義情緒分數顏色映射
def get_color(score):
    if score == 1:
        return 'darkred'
    elif score == 2:
        return 'red'
    elif score == 3:
        return 'orange'
    elif score == 4:
        return 'lightgreen'
    elif score == 5:
        return 'green'
    else:
        return 'gray'  # 如果沒有情緒分數，就顯示灰色

# 創建地圖，選擇使用 'Stamen Toner' 底圖，並加上版權聲明
mymap = folium.Map(location=[23.5, 121], zoom_start=6, tiles='CartoDB positron',
                   attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.')

# 創建 MarkerCluster 來分組顯示地點標記
marker_cluster = MarkerCluster().add_to(mymap)

# 遍歷資料中的每一行，將地點和情緒分數顯示到地圖上
for index, row in df.iterrows():
    # 確保每行都有經緯度信息
    if pd.notna(row['latitude']) and pd.notna(row['longitude']):
        folium.Marker(
            location=[row['latitude'], row['longitude']],  # 地點座標
            popup=f"地點: {row['location']}<br>情緒分數: {row['sentiment_score']}",
            icon=folium.Icon(color=get_color(row['sentiment_score']))
        ).add_to(marker_cluster)

# 指定儲存路徑
map_output_path = "output/path/sentiment_analysis_map.html"

# 儲存地圖
mymap.save(map_output_path)

# 顯示結果儲存提示
print(f"地圖已成功儲存到: {map_output_path}")