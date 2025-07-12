# Proton Pass Migrator: Scripts & Web Tool

A collection of Python scripts and a browser-based web tool to solve common issues when migrating passwords from Proton Pass to Firefox, Chrome, and other password managers.

一套用於解決從 Proton Pass 密碼管理器遷移到 Mozilla Firefox、Google Chrome 等平台時常見格式問題的 Python 腳本與網頁工具。

---

## 🚀 Live Web Tool / 立即可用的網頁工具

For the easiest experience, use our browser-based tool. No installation needed! All processing is done locally in your browser.

為了最簡單的使用體驗，請直接使用我們的網頁工具，無需任何安裝！所有處理都在您的瀏覽器本地完成，您的資料絕不會被上傳。

**👉 [Click here to use the Web Tool / 點此使用網頁工具][(https://yuki-sakura-0001.github.io/proton-pass-migrator/password-converter.html)** 

*(Note: This link will work after you set up GitHub Pages.)*
*(註：此連結將在您完成 GitHub Pages 設定後生效。)*

---

## 🐍 For Developers: Python Scripts / 給開發者：Python 腳本

If you prefer to run the scripts locally or want to inspect the code, you can use the Python scripts directly.

如果您偏好在本機執行腳本，或希望研究程式碼，可以直接使用 Python 腳本。

### Features / 功能特性

- **Handles Multiple URLs**: Splits a single login item with multiple URLs into separate entries.
- **Smart Username Filling**: If a login's `username` field is empty, it uses the `name` field as a fallback.
- **Generates Two Files**: `firefox_import_ready.csv` (for import) and `full_backup_processed.csv` (complete backup).
- **Merge Utility**: Includes `merge_csv.py` to merge existing passwords with new ones.

### How to Use / 如何使用

1.  **Prerequisites**: Make sure you have [Python](https://www.python.org/downloads/) installed.
2.  **Export Data**: Export your CSV files from Proton Pass and (optionally) your browser.
3.  **Run Script**: Place the CSV files in the same folder as the scripts and run:
    ```bash
    python process_passwords.py
    ```

---

## ⚠️ Security Warning / 安全警告

**Your passwords in CSV files are stored in plain text and are NOT secure.**

**CSV 檔案中的密碼是以純文字形式儲存的，極不安全！**

After you have successfully imported your passwords, you **MUST** permanently delete all CSV files (`.csv`) from your computer, including from the Recycle Bin / Trash.

在您成功將密碼匯入到密碼管理器之後，**必須**從您的電腦上**徹底刪除**所有的 CSV 檔案。

This program all come from ai studio model for Gemini 2.5 pro
I use most of the problems can be solved, but the problem of the lack of url of the Android application login has not yet thought about how to let ai modification, the probability of lack of data after use **so please make sure that the integrity of the deletion of any file**.
 
此程式皆來至ai studio 模型為Gemini 2.5 pro
本人使用大部分問題皆能解決，但安卓應用登入的缺少url的問題尚未思考如何讓ai修改
，使用完概率缺少數據**故請確認完整在刪除任何檔案**。

## 📄 License / 授權

This project is licensed under the MIT License. See the `LICENSE` file for details.
