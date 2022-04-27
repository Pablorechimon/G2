import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def on_created(event):
    f = open("log.txt", "a")
    f.write(f"NEW FILE: {event.src_path}")
    f.close()

def sensor():
    event_handler = FileSystemEventHandler()
    event_handler.on_created = on_created
    
    path = "."
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    
    observer.start()
    try:
        while observer.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()