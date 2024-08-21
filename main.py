import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from win10toast_click import ToastNotifier

screenshot_dir = "C:/Users/abidu/OneDrive/Pictures/Screenshots"

class ScreenshotHandler(FileSystemEventHandler):
    def __init__(self):
        self.toaster = ToastNotifier()

    def on_created(self, event):
        # When a new screenshot is created, trigger this function
        if not event.is_directory:
            file_path = event.src_path
            print(f"New screenshot detected: {file_path}")
            self.send_notification(file_path)

    def send_notification(self, file_path):
        self.toaster.show_toast(
            "Screenshot Taken",
            "Click this notification to delete the screenshot",
            icon_path=None,
            duration=10,
            callback_on_click=lambda: self.delete_file(file_path)
        )

    def delete_file(self, file_path):
        os.remove(file_path)

def monitor_screenshots(directory):
    event_handler = ScreenshotHandler()
    observer = Observer()
    observer.schedule(event_handler, path=directory, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    monitor_screenshots(screenshot_dir)
