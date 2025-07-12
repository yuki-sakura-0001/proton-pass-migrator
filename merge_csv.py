import csv

# --- 設定 ---
file1 = 'firefox_existing_passwords.csv' # Firefox 舊資料
file2 = 'firefox_import_ready.csv'       # Proton Pass 新資料
output_file = 'merged_passwords_final.csv' # 最終合併檔案
# --- 結束 ---

# 讀取第一個檔案的內容（包括標頭）
with open(file1, 'r', encoding='utf-8') as f1:
    reader1 = csv.reader(f1)
    data1 = list(reader1)

# 讀取第二個檔案的內容（跳過標頭）
with open(file2, 'r', encoding='utf-8') as f2:
    reader2 = csv.reader(f2)
    next(reader2) # 跳過標頭行
    data2 = list(reader2)

# 合併資料並寫入新檔案
with open(output_file, 'w', encoding='utf-8', newline='') as f_out:
    writer = csv.writer(f_out)
    writer.writerows(data1) # 寫入檔案1的全部內容
    writer.writerows(data2) # 附加檔案2的資料行

print(f"🎉 合併完成！")
print(f"檔案 '{file1}' 和 '{file2}' 的內容已合併到 '{output_file}'。")
