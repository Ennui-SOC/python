class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initializes a Television object with default values.
        Status and muted are set to False; volume and channel are set to their minimum values.

        Returns:
            None
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggles the power status of the television between on and off.

        Returns:
            None
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Toggles the mute status of the television when it is on.
        Has no effect when the television is off.

        Returns:
            None
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increases the channel by one when the television is on.
        If the channel is at the maximum, it cycles back to the minimum channel.
        Has no effect when the television is off.

        Returns:
            None
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decreases the channel by one when the television is on.
        If the channel is at the minimum, it cycles back to the maximum channel.
        Has no effect when the television is off.

        Returns:
            None
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increases the volume by one when the television is on.
        If the television is muted, it will unmute before adjusting.
        Volume will not exceed the maximum value.
        Has no effect when the television is off.

        Returns:
            None
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume by one when the television is on.
        If the television is muted, it will unmute before adjusting.
        Volume will not go below the minimum value.
        Has no effect when the television is off.

        Returns:
            None
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Returns a string representation of the television's current state.

        Returns:
            str: A formatted string displaying the power status, current channel,
            and current volume (shown as 0 if muted).
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume if not self.__muted else 0}"