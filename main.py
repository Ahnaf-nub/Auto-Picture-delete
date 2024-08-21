import os
import time
from plyer import notification
screenshot_dir = "C:/Users/abidu/OneDrive/Pictures/Screenshots"

# Function to send push notification
def send_notification(file_path):
    notification.notify(
        title="Screenshot Detected",
        message=f"Click here to delete: {file_path}",
        timeout=10,
        app_name="Screenshot Manager"
    )

# Function to monitor the directory for new files
def monitor_directory(directory):
    print(f"Monitoring directory: {directory}")
    known_files = set(os.listdir(directory))
    
    while True:
        time.sleep(2)  # Check every 2 seconds
        current_files = set(os.listdir(directory))
        new_files = current_files - known_files
        
        for new_file in new_files:
            file_path = os.path.join(directory, new_file)
            print(f"New file detected: {file_path}")
            send_notification(file_path)
            user_input = input(f"Do you want to delete the file {file_path}? (yes/no): ").strip().lower()
            if user_input == "yes":
                os.remove(file_path)
                print(f"{file_path} has been deleted.")
        
        known_files = current_files

if __name__ == "__main__":
    monitor_directory(screenshot_dir)
