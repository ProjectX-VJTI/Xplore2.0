import cv2 as cv
import numpy as np

img = cv.imread(r'H:\Engineering 2024\Coding\ProjectX\Answers_Nathan\OpenCV-Clone\Answers_Nathan\Task2.png', cv.IMREAD_GRAYSCALE)

morse = ''
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i][j] == 255:
            morse = morse + '.'
        elif img[i][j] == 0:
            morse = morse + '-'
        else:
            morse = morse + ' '


print(morse)

def morse_reader(morse):
    morse_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
        '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
        '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
        '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z'
    }

    return ''.join(morse_dict.get(code) for code in morse.strip().split())


print(f'The Morse Code gives us: {morse_reader(morse)}')
    