class Timer:
    def __init__( self, hours=0 , minutes=0 , seconds =0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        hours =str(self.hours ).zfill(2)
        minutes =str(self.minutes).zfill(2)
        seconds = str(self.seconds ).zfill(2)
        return hours +" : "+ minutes +" : "+ seconds

    def next_second(self):
        self.seconds +=1
        if self.seconds <60:
            self.minutes = self.seconds // 60
            self.hours = self.seconds // 3600
        else:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
                if self.hours == 24:
                    self.hours = 0
                    
    def prev_second(self):
        if self.seconds >0:
            self.seconds -=1
        else:
            self.seconds =59
            self.minutes -= 1
            if self.minutes < 0:
                self.minutes = 59
                if self.hours == 0:
                    self.hours = 23
           

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
