import csv
import requests
import re

# 定義 Ollama 本地 API URL
OLLAMA_API_URL = "http://127.0.0.1:11434/v1/completions"

def clean_text(text):
    """
    清理文本中的雜訊，移除多餘字符如 '\n'、'*'、數字編號等。
    """
    # 移除換行符、星號、數字編號
    text = re.sub(r"[\n\*\d\.]+", "", text)
    return text.strip()

def split_keyword_string(text):
    """
    將返回的關鍵字字符串分割為列表，並清理每個關鍵字的雜訊。
    """
    try:
        # 假設格式為 "keywords: keyword1, keyword2, keyword3"
        keywords = text.split(":")[1]
        keywords = keywords.split(",")
        keywords = [clean_text(k) for k in keywords]
        return keywords
    except IndexError:
        return []

# 定義關鍵字提取函數
def extract_keywords(text):
    """
    使用 Ollama API 從給定文本中提取三個"情緒"或"感覺"的關鍵字。
    
    :param text: 要分析的文本
    :return: 包含三個關鍵字的列表
    """
    if not text.strip():
        return ["文本為空", "無法提取", "關鍵字"]

    # 提示詞 (Prompt)
    prompt = f"""
    please summarize the given text with one keywords related to emotions or feelings, and reply only the keywords separated by commas:
    {text}
    """

    # 定義請求數據
    data = {
        "model": "llama2:latest",  # 根據你的模型名稱設置
        "prompt": prompt,
    }

    try:
        # 發送 POST 請求
        response = requests.post(OLLAMA_API_URL, json=data)
        response.raise_for_status()  # 如果請求失敗，觸發異常

        # 解析結果
        result = response.json()
        raw_keywords = result["choices"][0]["text"]
        keywords = split_keyword_string(raw_keywords)

        # 確保返回三個關鍵字（不足補空字串）
        return (keywords + [""] * 3)[:3]

    except requests.exceptions.RequestException as e:
        print(f"API 請求錯誤: {e}")
        return ["API 請求", "錯誤", "發生"]

def process_csv(input_csv_path, output_csv_path):
    """
    從 CSV 文件讀取文本，提取關鍵字，並將結果寫入新的 CSV 文件。
    
    :param input_csv_path: 輸入 CSV 文件的路徑
    :param output_csv_path: 輸出 CSV 文件的路徑
    """
    try:
        with open(input_csv_path, mode='r', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames + ["keyword1", "keyword2", "keyword3"]  # 添加三個關鍵字欄位

            with open(output_csv_path, mode='w', newline='', encoding='utf-8') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()

                for row in reader:
                    text = row.get("Description", "")  # 假設輸入的 CSV 有一欄叫 "description"
                    print(f"正在分析文本: {text}")
                    keywords = extract_keywords(text)
                    
                    # 將關鍵字分別寫入對應欄位
                    row["keyword1"], row["keyword2"], row["keyword3"] = keywords
                    writer.writerow(row)
                    print(f"提取出的關鍵字: {keywords}")

        print(f"完成！結果已保存至 {output_csv_path}")

    except FileNotFoundError:
        print(f"文件未找到：{input_csv_path}")
    except KeyError:
        print(f"請確保輸入的 CSV 文件中有名為 'Description' 的欄位")

# 測試程式
if __name__ == "__main__":
    input_csv = r"D:\重要資料\桌面\v_s_img_0-200.csv"  # 輸入的 CSV 文件路徑
    output_csv = r"D:\重要資料\桌面\0-200_kw.csv"  # 輸出的 CSV 文件路徑

    process_csv(input_csv, output_csv)