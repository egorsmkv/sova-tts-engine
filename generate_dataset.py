CSV_FILE = '/home/yehor/TTS-Tacotron/metadata_not.csv'
DS_FILE = '/home/yehor/TTS-Tacotron/dataset.txt'

def clean_text(v):
    v = v.replace('«','')
    v = v.replace('»','')
    return v

with open(DS_FILE, 'w') as x:
    with open(CSV_FILE) as f:
        for line in f:
            parts = line.strip().split('|')
            print(parts)

            filename = f'wavs/{parts[0]}.wav'
            text = clean_text(parts[1])

            x.write(f'{filename}|{text}\n')
