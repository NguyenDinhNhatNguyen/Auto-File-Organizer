import os
import shutil
import logging
from datetime import datetime

# 1. Cấu hình ánh xạ đuôi file
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.doc'],
    'SetupFiles': ['.exe', '.msi', '.apk', '.dmg', '.iso'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'Music': ['.mp3', '.wav', '.flac']
}

class FileMover:
    def __init__(self, source_dir):
        self.source_dir = source_dir
        # Tạo folder logs nếu chưa có
        if not os.path.exists('logs'):
            os.makedirs('logs')
            
        # Cấu hình ghi log
        logging.basicConfig(filename='logs/organization.log', 
                            level=logging.INFO, 
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')

    def move_file(self, file_path):
        filename = os.path.basename(file_path)
        name, ext = os.path.splitext(filename)
        
        # Bỏ qua file hệ thống, file tạm, hoặc chính folder đích
        if ext in ['.tmp', '.crdownload'] or filename.startswith('.') or os.path.isdir(file_path):
            return

        destination_folder = "Others" # Mặc định
        
        # Tìm folder đích dựa trên đuôi file
        for category, extensions in FILE_CATEGORIES.items():
            if ext.lower() in extensions:
                destination_folder = category
                break
        
        # Tạo đường dẫn đích
        dest_path = os.path.join(self.source_dir, destination_folder)
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)

        # Xử lý trùng tên (Thêm timestamp)
        final_path = os.path.join(dest_path, filename)
        if os.path.exists(final_path):
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            final_path = os.path.join(dest_path, f"{name}_{timestamp}{ext}")

        # Thực hiện di chuyển
        try:
            # Chờ 1 chút để đảm bảo file không bị lock bởi tiến trình khác
            shutil.move(file_path, final_path)
            log_msg = f"SUCCESS: Moved '{filename}' to '{destination_folder}'"
            print(log_msg)
            logging.info(log_msg)
        except Exception as e:
            err_msg = f"ERROR: Could not move '{filename}'. Reason: {str(e)}"
            print(err_msg)
            logging.error(err_msg)
            