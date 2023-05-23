from pydub import AudioSegment

def combinar_canciones(cancion1, cancion2, salida):
    # Cargar las canciones utilizando pydub
    cancion1 = AudioSegment.from_mp3("/home/simon/dev/organizacion_computadores/proyecto_audio/files/Duvet.mp3")
    cancion2 = AudioSegment.from_mp3("/home/simon/dev/organizacion_computadores/proyecto_audio/files/UN_OWEN_WAS_HER.mp3")

    # Combinar las canciones
    cancion_combinada = cancion1 + cancion2

    # Guardar la canción combinada en un archivo MP3
    cancion_combinada.export(salida, format='mp3')

    print("¡Las canciones se han combinado correctamente!")

# Ejemplo de uso
cancion1 = "cancion1.mp3"
cancion2 = "cancion2.mp3"
salida = "canciones_combinadas.mp3"

combinar_canciones(cancion1, cancion2, salida)