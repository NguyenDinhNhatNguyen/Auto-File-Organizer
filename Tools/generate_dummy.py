import os
import random
import time

# Đường dẫn đến folder TestZone
TEST_DIR = "TestZone"
EXTENSIONS = ['.jpg', '.png', '.docx', '.txt', '.pdf', '.exe', '.zip', '.mp4', '.mp3', '.sql', '.py', '.spv', '.pdsprj', '.c', '.sbss']

def create_dummy_files():
    if not os.path.exists(TEST_DIR):
        os.makedirs(TEST_DIR)
        print(f"Đã tạo thư mục: {TEST_DIR}")

    print(f"Đang tạo 50 file giả ngẫu nhiên vào {TEST_DIR}...")
    
    for i in range(1, 51):
        ext = random.choice(EXTENSIONS)
        filename = f"test_file_{i}{ext}"
        file_path = os.path.join(TEST_DIR, filename)
        
        with open(file_path, 'w') as f:
            f.write("Dummy content check.")
        
        print(f"   + Created: {filename}")
        time.sleep(0.5) # Delay để kịp nhìn bên màn hình log

    print("\nHoàn tất!")

if __name__ == "__main__":
    create_dummy_files()