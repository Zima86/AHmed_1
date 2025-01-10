from vidstream import CameraClient
from vidstream import StreamingServer

import threading
import time



sending=CameraClient('192.168.1.206',9999)
t2=threading.Thread(target=sending.start_stream())
t2.start()
while input()!="STOP":
    continue
sending.stop_stream()