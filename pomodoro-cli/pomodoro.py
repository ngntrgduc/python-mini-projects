from time import sleep

import fire
from pydub import AudioSegment
from pydub.playback import play


def play_sound(file_name='completed.wav') -> None:
    """Play sound when comlete a pomodoro"""
    sound = AudioSegment.from_file(file_name, format='wav')
    play(sound)

def padding(time: int) -> str:
    """Add padding for time"""
    return str(time).zfill(2)

def display(time: int) -> None:
    """Display time to the console"""
    if time > 60:
        hours = padding(time // 60)
        minutes = padding(time %  60)
    else:
        hours = padding(0)
        minutes = padding(time %  60)
    
    print(f'{hours}:{minutes}')

def flow_mode() -> None:
    """Flowtime mode"""
    try:
        time = 0
        while True:
            print('Flowtime-ing - ', end='')
            display(time)
            sleep(60)
            time += 1
    except KeyboardInterrupt:
        print('Flowtime ended.')

def pomodoro(time: int) -> None:
    """Pomodoro mode"""
    try:
        while time > 0:
            print('Pomodoro-ing - ', end='')
            display(time)
            sleep(60)
            time -= 1

        print('End of pomodoro.')
        play_sound()
    except KeyboardInterrupt:
        print('Interupted by keyboard')

def main(
        time: int = 25,
        flow: bool = False,
    ) -> None:

    if not flow:
        pomodoro(time)
    else:
        flow_mode()
    
fire.Fire(main)