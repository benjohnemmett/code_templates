from threading import Thread
from time import sleep


class ThreadClass(object):
    def __init__(self, name):
        self.name = name
        self.thread = None
        self.run_thread = False

    def __str__(self):
        return self.name
    
    def start(self, thread_msg="Thread running.."):
        self.thread = Thread(target=self.run, args=(thread_msg,))
        self.thread.start()

    def stop(self):
        self.run_thread = False

    def run(self, thread_msg):
        self.run_thread = True
        while self.run_thread:
            print(f"[{self.name}]: {thread_msg}")
            sleep(1)

        print("Exiting thread")


if __name__ == "__main__":
    print("Starting...")
    thread_obj = ThreadClass("test")

    print("Starting thread...")
    thread_obj.start("Custom thread update message...")
    sleep(4)

    print("Stopping thread...")
    thread_obj.stop()

    print("Exiting...")