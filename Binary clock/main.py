import time
import datetime
import os

def convert_to_bin(number):
    if number == 0:
        return '0000'
    converted = ''
    while (number > 0):
        converted += str(number % 2)
        number = int(number / 2)
    while (len(converted) != 4):
        converted += '0';
    return converted[::-1]

def create_clock(rows):
    os.system('cls')
    for i in range(4):
        print()
        j = col = 0
        while (col < 9):
            if col == 0 or col == 2 or col == 6 or col == 8:
                row = rows[j]
                if row[i] == '1':
                    print('*', end='')
                    j += 1
                else:
                    print('.', end='')
                    j += 1
            else:
                print(' ', end='')
            col += 1
    print('   ', end='')
    return

def init():
    day = datetime.datetime.now()
    time_now = day.strftime('%H%M')
    sec = day.strftime('%S')
    binary_time = []
    for i in time_now:
        binary_time.append(convert_to_bin(int(i)))
    create_clock(binary_time)
    return

def main():
    init()
    while(True):
        time.sleep(1)
        
        # Get time
        day = datetime.datetime.now()
        time_now = day.strftime('%H%M')
        sec = day.strftime('%S')

        # Create clock
        if sec == '00':
            binary_time = []
            for i in time_now:
                binary_time.append(convert_to_bin(int(i)))
            create_clock(binary_time)
    return 

main()