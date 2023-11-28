from terminal_layout.extensions.progress import *
import time


x = input('Mari kita tebak: ')

with Loading('Analisis jawaban :))', 20) as l:
    for i in range(10):
        if l.is_finished():
            break
        time.sleep(0.3)
        l.add_progress(i)
print(f'Kamu menulis "{x}"')
print('Benar kan :))')