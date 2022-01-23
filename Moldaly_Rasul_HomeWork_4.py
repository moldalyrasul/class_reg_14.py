class TimeDesk:
    def __init__(self, seconds):
        self.seconds = seconds
        self.sec = seconds % 60
        self.min = seconds % 3600 // 60
        self.hour = seconds % 86400 // 3600
        self.day = seconds // 86400

    def __str__(self):
        return f'seconds: {self.sec},' \
               f'minute: {self.min},' \
               f'hours: {self.hour},' \
               f'day: {self.day}'

f = TimeDesk(seconds=70)
print(f)

#дз=2




