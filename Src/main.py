import time
import os
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from organizer import FileMover

# === CẤU HÌNH ĐƯỜNG DẪN ===
# Để an toàn, mặc định ta sẽ chạy trên folder "TestZone"
# Khi nào muốn chạy thật, bạn đổi dòng dưới thành đường dẫn Downloads thật
# WATCH_DIRECTORY = r"C:\Users\YourName\Downloads"
WATCH_DIRECTORY = os.path.join(os.getcwd(), "TestZone")
class Handler(FileSystemEventHandler):
    def __init__(self):
        self.organizer = FileMover(WATCH_DIRECTORY)

    def on_created(self, event):
        if not event.is_directory:
            self.process_file(event.src_path)

    def process_file(self, file_path):
        """Hàm xử lý chung cho cả file mới và file cũ"""
        filename = os.path.basename(file_path)
        
        # 1. Bỏ qua file rác/file đang tải
        ignore_exts = ('.tmp', '.crdownload', '.part', '.ini', 'desktop.ini')
        if filename.endswith(ignore_exts):
            return

        # 2. Delay nhẹ để đảm bảo file đã tải xong. Quan trọng: với các file nặng
        # Với file quét cũ thì không cần delay, nhưng để chung cho an toàn
        time.sleep(1) 
        
        try:
            self.organizer.move_file(file_path)
        except Exception as e:
            print(f"Lỗi xử lý file {filename}: {e}")

def clean_existing_files():
    """Quét và xử lý các file đã có sẵn trong folder trước khi chạy tool"""
    print(">>> Đang quét dọn các file cũ...")
    organizer = FileMover(WATCH_DIRECTORY)
    
    # Lấy tất cả file trong thư mục gốc
    if os.path.exists(WATCH_DIRECTORY):
        files = [f for f in os.listdir(WATCH_DIRECTORY) if os.path.isfile(os.path.join(WATCH_DIRECTORY, f))]
        
        for filename in files:
            file_path = os.path.join(WATCH_DIRECTORY, filename)
            # Sử dụng logic bỏ qua file rác
            ignore_exts = ('.tmp', '.crdownload', '.part', '.ini', 'desktop.ini')
            if not filename.endswith(ignore_exts):
                organizer.move_file(file_path)
    print(">>> Đã dọn xong file cũ.")

if __name__ == "__main__":
    # Kiểm tra thư mục có tồn tại không
    if not os.path.exists(WATCH_DIRECTORY):
        print(f"Lỗi: Đường dẫn '{WATCH_DIRECTORY}' không tồn tại.")
        print("Vui lòng sửa biến WATCH_DIRECTORY trong code.")
        sys.exit(1)

    print(f"-------------------------------------------------")
    print(f"AUTO FILE ORGANIZER - STARTED")
    print(f"Theo dõi: {WATCH_DIRECTORY}...")
    print(f"-------------------------------------------------")

    # BƯỚC 1: Dọn dẹp file cũ trước
    clean_existing_files()

    # BƯỚC 2: Bắt đầu theo dõi file mới
    print(">>> Đang chờ file mới (Nhấn Ctrl+C để dừng)...")
    event_handler = Handler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_DIRECTORY, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
        print("\nChương trình đã dừng.")
    observer.join()