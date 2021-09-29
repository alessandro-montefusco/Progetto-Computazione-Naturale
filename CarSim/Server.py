import os
from threading import Thread
import shutil
import time

class Server(Thread):
    def __init__(self, visual=False):
        Thread.__init__(self)
        self.visual = visual

    def run(self):
        if self.visual:
            cmds = "cd \"C:\Program Files (x86)\\torcs\"&wtorcs.exe -r quickrace.xml -nofuel -nodamage -t 1000000" #1 ms
        else:
            cmds = "cd \"C:\Program Files (x86)\\torcs\"&wtorcs.exe -r quickrace.xml -nofuel -nodamage -T -t 1000000 >NUL"
        os.system(cmds)

def start_server():
    server = Server(visual=False)
    server.start()

def start_server_single():
    path_start = "C:\\Program Files (x86)\\torcs\\config\\raceman\\" + str(3001) + "\\quickrace.xml"
    path_dest = "C:\\Program Files (x86)\\torcs\\config\\raceman\\"
    shutil.copy(path_start, path_dest)
    server = Server(visual=True)
    server.start()

def start_multiple_server(nserv=2, visual=False):
    Servers = []
    for i in range(nserv):
        path_start = "C:\\Program Files (x86)\\torcs\\config\\raceman\\" + str(3001 + i) + "\\quickrace.xml"
        path_dest = "C:\\Program Files (x86)\\torcs\\config\\raceman\\"
        shutil.copy(path_start, path_dest)
        server = Server(visual=visual)
        server.start()
        Servers.append(server)
        print("Starting Server n.", i + 1)
        time.sleep(2)