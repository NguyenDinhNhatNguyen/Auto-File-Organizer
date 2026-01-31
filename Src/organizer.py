import os
import shutil

class FileMover:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        # Định nghĩa các thư mục và đuôi file tương ứng
        self.folders = {
            "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.heic'],
            "Documents": ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.pptx', '.csv'],
            "Videos": ['.mp4', '.mov', '.avi', '.mkv', '.flv'],
            "Music": ['.mp3', '.wav', '.flac', '.aac'],
            "Archives": ['.zip', '.rar', '.7z', '.tar', '.gz'],
            "Software": ['.exe', '.msi', '.apk', '.iso']
        }
        self.create_folders()

    def create_folders(self):
        # Tạo các thư mục đích nếu chưa có
        for folder in self.folders:
            folder_path = os.path.join(self.base_dir, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

    def get_unique_name(self, destination, filename):
      
        # Nếu file bị trùng tên, tự động thêm số đếm.
        # Ví dụ: a.jpg -> a(1).jpg -> a(2).jpg -> a(3).jpg
   
        name, ext = os.path.splitext(filename)
        counter = 1
        new_filename = filename
        
        # Vòng lặp kiểm tra: Nếu tên file đã tồn tại thì thêm số và kiểm tra tiếp
        while os.path.exists(os.path.join(destination, new_filename)):
            new_filename = f"{name}({counter}){ext}"
            counter += 1
            
        return new_filename

    def move_file(self, file_path):
        # Hàm chính để di chuyển file
        filename = os.path.basename(file_path)
        name, ext = os.path.splitext(filename)
        ext = ext.lower()

        moved = False
        for folder, extensions in self.folders.items():
            if ext in extensions:
                destination_dir = os.path.join(self.base_dir, folder)
                
                # 1. Tạo tên duy nhất để tránh ghi đè
                unique_filename = self.get_unique_name(destination_dir, filename)
                destination_path = os.path.join(destination_dir, unique_filename)
                
                try:
                    # 2. Di chuyển file
                    shutil.move(file_path, destination_path)
                    print(f"[OK] Đã chuyển: {filename} -> {folder}/{unique_filename}")
                    moved = True
                except Exception as e:
                    print(f"[ERROR] Lỗi khi chuyển {filename}: {e}")
                break
                
        if not moved:
             other_dir = os.path.join(self.base_dir, "Others")
             if not os.path.exists(other_dir): os.makedirs(other_dir)
             shutil.move(file_path, os.path.join(other_dir, self.get_unique_name(other_dir, filename)))