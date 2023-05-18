import queue
import sounddevice as sd
import vosk

q = queue.Queue()

device = sd.default.device = 0, 4    # sd.default.device = 1, 3   /////input, output [1, 4]
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])


def callback(indata, frames, time, status):
    q.put(bytes(indata))


with sd.RawInputStream(samplerate=args.samplerate, blocksize=8000, device=args.device,
                       dtype="int16", channels=1, callback=callback):
    rec = vosk.KaldiRecognizer(model, args.samplerate)
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            print(rec.Result())
        else:
            print(rec.PartialResult())
