class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        Television object initialized with default values. Volume and Channel are set to their minimum values
        while status and muted are set to False
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """
        Toggles the power status of the television to off or on
        """
        self.__status = not self.__status

    def mute(self):
        """
        Toggle the mute status of the television when on, this has no effect when the television is off
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        """
        When the television is on, the channel is increased by one.
        If the channel is already at the maximum, it cycles back to the minimum channel
        doesn't apply when television is off
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        """
        When the television is off, the channel is decreased by one.
        If the channel is already at the minimum, it cycles back to the maximum channel
        doesn't apply when television is off
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        """
        Increase the volume by one when the television is on and if television is muted, it will unmute and adjust
        Volume will not exceed the maximum volume
        doesn't apply when television is off
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """
        Decrease the volume by one when the television is on and if television is muted, it will unmute and adjust
        volume will not exceed the minimum volume
        doesn't apply when television is off
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """
        Return the string representation of the television's status: Power, Channel and Volume
        :return:
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume if not self.__muted else 0}"