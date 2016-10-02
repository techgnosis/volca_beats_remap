import mido

# Volca Beats has ridiculous note mappings
# 36 - C2 - Kick
# 38 - D2 - Snare
# 43 - G2 - Lo Tom
# 50 - D3 - Hi Tom
# 42 - F#2 - Closed Hat
# 46 - A#2 - Open Hat
# 39 - D#2 - Clap
# 75 - D#5 - Claves
# 67 - G4 - Agogo
# 49 - C#3 - Crash


note_mapping = {
    48 : 36,
    49 : 38,
    50 : 43,
    51 : 50,
    52 : 42,
    53 : 46,
    54 : 39,
    55 : 75,
    56 : 67,
    57 : 49    
}


mido.set_backend('mido.backends.rtmidi')

inport = mido.open_input('RemapInput', virtual=True)
print(inport)

print(mido.get_output_names())

outport = mido.open_output('UM-ONE 24:0', virtual=False)
print(outport)

for msg in inport:
    if msg.type in ['note_on','note_off']:
        if msg.channel == 1:
            print('Recieved {} on channel {}'.format(msg.note, msg.channel))
            if msg.note in note_mapping:
                print('Found note in note_mapping')
                new_note = note_mapping[msg.note]
                print('New note is {}'.format(new_note))
                msg.note = new_note
            outport.send(msg)
