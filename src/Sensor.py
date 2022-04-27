import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def on_created(event):
    f = open("C:\\Users\\Pablo\\Code-Workspace\\g2\\log.txt", "a")
    f.write(f"NEW FILE: {event.src_path}")
    f.close()

def create_observer():
    observer = Observer()
    return observer

def sensor(observer):
    event_handler = FileSystemEventHandler()
    event_handler.on_created = on_created
    
    path = "C:\\Users\\Pablo\\Code-Workspace\\g2\\."
    observer.schedule(event_handler, path, recursive=True)
    
    observer.start()
    #while observer.is_alive():
       #time.sleep(1)


def stop_sensor(observer):
    observer.stop()
    observer.join()

#if __name__ == '__main__' :
 #   sensor(create_observer())