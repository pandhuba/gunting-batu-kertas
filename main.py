# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 14:53:44 2020

@author: Tulenesia
"""

import fungsi
# import module random
import random

print('Memulai permainan Batu Kertas Gunting!')
player_name = input('Masukkan nama Anda: ')

print('Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)')
player_hand = int(input('Masukkan nomor (0-2): '))

if fungsi.validate(player_hand):
    # Tetapkan nomor acak antara 0 dan 2 ke computer_hand menggunakan randint
    computer_hand = random.randint(0,2)
    
    fungsi.print_hand(player_hand, player_name)
    fungsi.print_hand(computer_hand, 'Komputer')

    result = fungsi.judge(player_hand, computer_hand)
    print('Hasil: ' + result)
else:
    print('Mohon masukkan nomor yang benar')
