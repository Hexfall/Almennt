class Clock(object):
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def str_update(self, inp):
        inp = [int(i) for i in inp.split(':')]
        self.hours = inp[0]
        self.minutes = inp[1]
        self.seconds = inp[2]
    def add_clocks(self, inpClock):
        def divm(high, low):
            quo, mod = divmod(low, 60)
            high += quo
            low = mod
            return high, low
        newClock = self
        newClock.hours += inpClock.hours
        newClock.minutes += inpClock.minutes
        newClock.seconds += inpClock.seconds
        newClock.minutes, newClock.seconds = divm(newClock.minutes, newClock.seconds)
        newClock.hours, newClock.minutes = divm(newClock.hours, newClock.minutes)
        return newClock
    def __str__(self):
        return "{} hours, {} minutes and {} seconds".format(self.hours, self.minutes, self.seconds)

clock1 = Clock()
clock2 = Clock()
print(clock1)
print(clock2)
clock1.str_update("03:21:34")
clock2.str_update("05:45:52")
print(clock1)
print(clock2)
clock3 = clock1.add_clocks(clock2)
print(clock3)