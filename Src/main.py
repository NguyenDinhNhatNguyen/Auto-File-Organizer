import time
import os
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from organizer import FileMover

# === CẤU HÌNH ĐƯỜNG DẪN ===
# Để an toàn, mặc định ta sẽ chạy trên folder "TestZone"
# Khi nào muốn chạy thật, bạn đổi dòng dưới thành đường dẫn Downloads thật
WATCH_DIRECTORY = os.path.join(os.getcwd(), "TestZone")

class Handler(FileSystemEventHandler):
    def __init__(self):
        self.organizer = FileMover(WATCH_DIRECTORY)

    def on_created(self, event):
        if not event.is_directory:
            # Delay 1s để file kịp ghi xong dữ liệu (tránh lỗi file đang được dùng)
            time.sleep(1) 
            self.organizer.move_file(event.src_path)

if __name__ == "__main__":
    # Đảm bảo folder TestZone tồn tại để chương trình không crash
    if not os.path.exists(WATCH_DIRECTORY):
        os.makedirs(WATCH_DIRECTORY)

    print(f"-------------------------------------------------")
    print(f"AUTO FILE ORGANIZER ĐANG CHẠY...")
    print(f"Đang theo dõi thư mục: {WATCH_DIRECTORY}")
    print(f"Log được ghi tại: logs/organization.log")
    print(f"Nhấn Ctrl + C để dừng chương trình")
    print(f"-------------------------------------------------")

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