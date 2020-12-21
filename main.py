import winsound # only works on windows

frequency_dict = {'C4':261.63,
                  'D4':293.66,
                  'E4':329.63,
                  'F4':349.23,
                  'G4':392.00,
                  'A4':440,
                  'B4':493.88}

def main():
    note_duration = 500 # in milliseconds
    for i in frequency_dict.items():
        winsound.Beep(int(i[1]), note_duration)



if __name__ == '__main__':
    main()