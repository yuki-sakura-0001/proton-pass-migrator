import csv
import os

# --- 使用者設定區 ---
# 1. 將您從 Proton Pass 匯出的 CSV 檔案名稱填寫在這裡
INPUT_FILENAME = 'protonpass_export.csv'

# 2. 這是為 Firefox 準備的、乾淨的匯入檔案名稱
OUTPUT_FIREFOX_FILENAME = 'firefox_import_ready.csv'

# 3. 這是包含所有原始資訊的、處理過的完整備份檔案名稱
OUTPUT_BACKUP_FILENAME = 'full_backup_processed.csv'

# 4. Proton Pass CSV 中對應的欄位名稱 (通常不需要修改)
PROTONPASS_NAME_COL = 'name'
PROTONPASS_URL_COL = 'url'
PROTONPASS_USER_COL = 'username'
PROTONPASS_PASS_COL = 'password'

# 5. 多個網址之間的分隔符號
URL_SEPARATOR = ','
# --- 設定結束 ---


def process_and_preserve_all_data():
    """
    讀取 Proton Pass 的 CSV，處理多網址、空值和使用者名稱填充問題，
    同時產生一個 Firefox 專用檔案和一個包含所有資訊的完整備份檔案。
    """
    if not os.path.exists(INPUT_FILENAME):
        print(f"錯誤：找不到輸入檔案 '{INPUT_FILENAME}'。")
        print("請確認檔名是否正確，且檔案與腳本在同一個資料夾中。")
        return

    try:
        with open(INPUT_FILENAME, mode='r', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            
            original_fieldnames = reader.fieldnames
            if not original_fieldnames:
                print(f"錯誤：無法讀取 '{INPUT_FILENAME}' 的標頭，檔案可能是空的或格式不正確。")
                return

            firefox_fieldnames = ['url', 'username', 'password', 'httpRealm', 'formActionOrigin', 'guid', 'timeCreated', 'timeLastUsed', 'timePasswordChanged']

            with open(OUTPUT_FIREFOX_FILENAME, 'w', encoding='utf-8', newline='') as ff_outfile, \
                 open(OUTPUT_BACKUP_FILENAME, 'w', encoding='utf-8', newline='') as bk_outfile:
                
                firefox_writer = csv.DictWriter(ff_outfile, fieldnames=firefox_fieldnames)
                backup_writer = csv.DictWriter(bk_outfile, fieldnames=original_fieldnames)
                
                firefox_writer.writeheader()
                backup_writer.writeheader()
                
                print("開始處理檔案...")
                total_source_rows = 0
                total_output_rows = 0

                for row in reader:
                    total_source_rows += 1
                    
                    urls_string = row.get(PROTONPASS_URL_COL, '')
                    individual_urls = urls_string.split(URL_SEPARATOR) if urls_string else ['']
                    
                    for url in individual_urls:
                        cleaned_url = url.strip()
                        
                        # --- 1. 準備並寫入 Firefox 檔案 (包含智慧填充邏輯) ---
                        
                        # 智慧填充 username
                        # 優先使用 'username' 欄位
                        ff_username = row.get(PROTONPASS_USER_COL, '').strip()
                        # 如果 'username' 為空，則改用 'name' 欄位
                        if not ff_username:
                            ff_username = row.get(PROTONPASS_NAME_COL, '').strip()
                        
                        firefox_row = {
                            'url': cleaned_url,
                            'username': ff_username,  # 使用智慧填充後的 username
                            'password': row.get(PROTONPASS_PASS_COL, ''),
                            'httpRealm': '',
                            'formActionOrigin': '',
                            'guid': '',
                            'timeCreated': '',
                            'timeLastUsed': '',
                            'timePasswordChanged': ''
                        }
                        firefox_writer.writerow(firefox_row)
                        
                        # --- 2. 準備並寫入完整備份檔案 (保持原始數據) ---
                        backup_row = row.copy()
                        backup_row[PROTONPASS_URL_COL] = cleaned_url
                        backup_writer.writerow(backup_row)
                        
                        total_output_rows += 1
                
                print("-" * 40)
                print("🎉 處理完成！(v3 - 智慧使用者名稱)")
                print(f"原始檔案共 {total_source_rows} 筆記錄。")
                print(f"處理後共產生 {total_output_rows} 筆記錄。")
                print("-" * 40)
                print(f"✅ Firefox 匯入檔案：'{OUTPUT_FIREFOX_FILENAME}'")
                print("   => 已智慧填充使用者名稱，可直接匯入 Firefox。")
                print(f"✅ 完整備份檔案：'{OUTPUT_BACKUP_FILENAME}'")
                print("   => 保留了最原始的 name/username 結構，請妥善保管。")
                print("-" * 40)
                print("安全提醒：完成匯入後，請務必徹底刪除電腦上的所有 CSV 檔案！")

    except Exception as e:
        print(f"處理過程中發生嚴重錯誤: {e}")

# 執行主函數
if __name__ == "__main__":
    process_and_preserve_all_data()
