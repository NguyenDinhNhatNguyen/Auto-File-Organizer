# 📂 Python Auto File Organizer

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Status](https://img.shields.io/badge/Status-Stable-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

A lightweight **Automation Script** that keeps your **Downloads** folder clean by automatically organizing files into specific subfolders in real-time.

## 🌟 Key Features

* **⚡ Real-time Monitoring:** Uses the `watchdog` library to detect and organize files the moment they are downloaded (Event-driven architecture). As soon as a file lands in your folder, it gets sorted.
* **🧹 Startup Cleanup:** Unlike basic scripts, this tool scans and organizes existing files immediately when launched, ensuring a clutter-free environment from second zero.
* **🗂️ Smart Sorting:** Automatically sorts files by extension:
    * `Images`: .jpg, .png, .gif, .svg...
    * `Documents`: .pdf, .docx, .txt, .pptx...
    * `SSoftware`: .exe, .msi, .apk...
    * `Archives`: .zip, .rar, .7z...
    * `Videos`/`Music`: .mp4, .mp3, .wav, ...
    * `...`: ...
* **📝 Logging System:** Tracks all file movements in `logs/organization.log` for easy debugging and auditing.
* **🛡️ Safe Handling:**
    * **Duplicate Resolution:** Never overwrites files. If `file.jpg` exists, the new file becomes `file(1).jpg`.
    * **Ignore Temp Files:** Intelligently ignores temporary browser files (`.tmp`, `.crdownload`, `.part`) to prevent corrupting unfinished downloads.

## 🛠️ Installation

1.  **Clone the repository:**
    ```bash
    git clone (https://github.com/NguyenDinhNhatNguyen/Auto-File-Organizer.git)
    cd python-auto-file-organizer
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 📖 Usage Guide

You can run this tool in 3 different modes depending on your needs:

### 🔰 Mode 1: Test Mode (Safe Sandbox)
*Recommended for first-time users or developers who want to test the logic without affecting real files.*

1.  Open `main.py` and ensure the path is set to the test folder:
    ```python
    # main.py
    WATCH_DIRECTORY = os.path.join(os.getcwd(), "TestZone")
    ```

2.  **🧪 Advanced Testing Scenario (Simulating Real Life):**
    To verify that the script handles **existing files**, **new files**, and **duplicates** correctly, follow this sequence:

    * **Step 1: Simulate Clutter**
        Run the generator *before* starting the main program.
        ```bash
        python tools/generate_dummy.py
        ```
        *(Your `TestZone` is now filled with random messy files).*

    * **Step 2: Test Startup Cleanup**
        Now run the main script.
        ```bash
        python main.py
        ```
        *(Observation: The script instantly cleans up the existing mess from Step 1).*

    * **Step 3: Test Real-time & Duplicates**
        While `main.py` is still running, open a **second terminal** and run the generator again.
        ```bash
        python tools/generate_dummy.py
        ```
        *(Observation: New files are sorted instantly. Since filenames are identical to Step 1, the script auto-renames them like `image(1).png` instead of crashing).*

---

### 🚀 Mode 2: Manual Run (Active Monitoring)
*Use this when you want to clean up your actual Downloads folder immediately and monitor the process via the console.*

1.  **Configuration:** Open `main.py` and update the path to your actual Downloads folder:
    ```python
    # Note: Use r"" (raw string) to avoid Windows path errors
    WATCH_DIRECTORY = r"C:\Users\YourName\Downloads"
    ```
2.  **Execution:**
    ```bash
    python main.py
    ```
    * The script will first scan and clean up **existing old files**.
    * Then, it enters "Watchdog mode" to wait for **new downloads**.

---

### 👻 Mode 3: Background Service (Recommended)
*Best for daily use. The script will run silently in the background and start automatically when you turn on your computer.*

1.  **Rename File:** Change the extension of `main.py` to `main.pyw`.
    *(The `.pyw` extension allows Python scripts to run without a console window).*
2.  **Open Startup Folder:**
    * Press `Windows + R`.
    * Type `shell:startup` and hit **Enter**.
3.  **Create Shortcut:**
    * Create a **Shortcut** of your `main.pyw` file.
    * Move this shortcut into the **Startup** folder you just opened.
4.  **Done:** From now on, the organizer will run automatically every time you boot up your PC.

## 📂 Project Structure

```text
File-Organizer/
├── Src/
│   ├── main.py             # Entry point & Watchdog configuration
│   └── organizer.py        # Core logic for moving and sorting files
├── Tools/
│   └── generate_dummy.py   # Tool to generate fake files for testing
├── Logs/                   # Operation logs are stored here
└── requirements.txt        # List of dependencies
```
## ⚠️ Note
1. The script will ignore hidden files and system files (starting with a dot `.`).
2. Make sure you have Write permissions for the target folder.
3. To stop the program, press `Ctrl + C` in the terminal.

## 🤝 Contributing
Contributions are welcome! If you find any bugs or want to add new features, feel free to open a Pull Request.

## 👤 Author
Nguyen Dinh Nhat Nguyen - Computer Engineering Student @ UIT-VNUHCM
