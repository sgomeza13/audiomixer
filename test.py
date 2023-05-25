import numpy as np
import struct

g = np.sqrt(2)/2
def audio_mixer(f1,f2):
    with open(f1,'rb') as f_mp3:
        first_mp3 = f_mp3.read()
        
    with open(f2,'rb') as f_mp3:
        second_mp3 = f_mp3.read()

    entry1 = first_mp3[0xA7:0xAC+1]
    print (struct.unpack("{}b".format(len(entry1)), entry1))

    entry2 = second_mp3[0xA7:0xAC+1]
    print (struct.unpack("{}b".format(len(entry2)), entry2))



    with open("/home/simon/dev/organizacion_computadores/proyecto_audio2/files/f3.mp3","wb") as f_mp3:
        for i in first_mp3:
            f_mp3.write(bytes(first_mp3[i]+second_mp3[i]))

audio_mixer("/home/simon/dev/organizacion_computadores/proyecto_audio2/files/Duvet.mp3","/home/simon/dev/organizacion_computadores/proyecto_audio2/files/UN_OWEN_WAS_HER.mp3")