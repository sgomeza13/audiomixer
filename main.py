from pydub import AudioSegment
from multiprocessing import Pool

def combinar_canciones(cancion1):
    # Cargar las canciones utilizando pydub
    cancion1 = AudioSegment.from_mp3("/home/simon/dev/organizacion_computadores/proyecto_audio/files/Duvet.mp3")
    cancion2 = AudioSegment.from_mp3("/home/simon/dev/organizacion_computadores/proyecto_audio/files/UN_OWEN_WAS_HER.mp3")

    
    # Combinar las canciones
    cancion_combinada = cancion1.overlay(cancion2)

    # Guardar la canción combinada en un archivo MP3
    cancion_combinada.export("/home/simon/dev/organizacion_computadores/proyecto_audio/files/f3.mp3", format='mp3')

    print("¡Las canciones se han combinado correctamente!")
    return cancion_combinada

# Ejemplo de uso



def main():
    cancion1 = "cancion1.mp3"
    cancion2 = "cancion2.mp3"
    with Pool() as pool:
        results = pool.map(combinar_canciones,cancion1)
    #combinar_canciones(cancion1)


if __name__ == '__main__':
    main()