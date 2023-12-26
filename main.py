import mido 
from mido import Message
msg = Message('note_on', note=60)
ports = mido.get_output_names()
print(ports)
print(msg)