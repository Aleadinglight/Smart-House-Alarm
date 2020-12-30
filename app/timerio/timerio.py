from pathlib import Path
import sys

print(sys.path[0])
print(Path.cwd())
print(Path(__file__).resolve().parents[2].joinpath("resources","timers"))

class TimerIO:
    def __init__(self, timer_directory=None):
        if (timer_directory != None):
            self.timer_directory = timer_directory
        else:
            self.timer_directory = Path(__file__).resolve().parents[2].joinpath("resources","timers")