from threading import Thread
from time import sleep


class CliThreadClass(object):
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
            cmd = input("> ")

            if not cmd:
                continue

            if "exit" in cmd.split(" "):
                self.stop()
            else:
                print(f"  (You typed {len(cmd.split(' '))} words)")
                

        print("Exiting thread")



if __name__ == "__main__":
    print("Starting...")
    cli_obj = CliThreadClass("test")

    print("Starting thread...")
    cli_obj.start("Custom thread update message...")

    count = 0
    while cli_obj.run_thread:
        count += 1
        print(f" - Counted {count} sheep...")
        sleep(2)

    print("Exiting...")