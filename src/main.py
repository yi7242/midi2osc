import sys
import time

from rtmidi.midiconstants import NOTE_ON
from rtmidi.midiutil import open_midiinput

import sender, oscbuilder

IP = "localhost"
PORT = 9000

def midiin_callback(event, data=None):
    message, deltatime = event

    # 下1桁はチャンネル番号
    if message[0] & 0xF0 == NOTE_ON:
        status, note, velocity = message
        channel = (status & 0xF) + 1
        msg = oscbuilder.OscBuilder('/midi/%i/noteon' % channel, note, velocity).build()
        sender.send_udp(IP, PORT, msg)
        print(channel, note,velocity)


try:
    port = sys.argv[1] if len(sys.argv) > 1 else None

    with open_midiinput(port, client_name='midi2osc')[0] as midiin:
        midiin.set_callback(midiin_callback)

        while True:
            time.sleep(1)
except (EOFError, KeyboardInterrupt):
    print("Bye.")
