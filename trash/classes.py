class TV():
    def __init__(self):
        self.channels = []
        self.is_on = False
        self.channel = ''
        channels = []
        self.channel_number = {}

    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False

    def set_channel(self,channel):
        self.channels.append(channel)

        
    def show_channels(self):
        for self.channel in self.channels:
            print(self.channel, self.channels.index(self.channel))
            self.channel_number.update({self.channel: self.channels.index(self.channel)+1})
        print(self.channel_number)
 
    def show_status(self):
        if self.is_on == True: 
            print(f'TV is on, channel {self.channel_number[self.channel]} {self.channel}')
        else:
            print('TV is off')
    
nigger = TV()
nigger.set_channel('nigger nation')
nigger.show_status()
nigger.set_channel('i hate niggers')
nigger.show_status()
nigger.set_channel('kys')
nigger.show_channels()
nigger.show_status()
nigger.turn_on()
nigger.show_status()
nigger.set_channel(1)
nigger.turn_off()
nigger.show_status()
nigger.turn_on()
nigger.show_status()