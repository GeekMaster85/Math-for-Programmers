from sinusoid import *

pygame.mixer.init(frequency=44100, size=-16, channels=1)

size = 44100
buffer = np.random.randint(-3000, 3000, size * 2)
buffer = buffer.reshape(size, 2)


def modified(t):
    return 8000 * sawtooth(441 * t)


arr = sample(modified, 0, 1, 44100)
arr = np.repeat(arr.reshape(size, 1), 2, axis=1)
sound = pygame.sndarray.make_sound(arr)
sound.play()
pygame.time.wait(int(sound.get_length() * 1000))
