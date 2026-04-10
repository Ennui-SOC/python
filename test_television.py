import pytest
from television import Television


class TestInit:
    def test_init(self):
        tv = Television()
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"


class TestPower:
    def test_power_on(self):
        tv = Television()
        tv.power()
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    def test_power_off(self):
        tv = Television()
        tv.power()
        tv.power()
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"


class TestMute:
    def test_mute_on_with_volume(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.mute()
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    def test_unmute(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.mute()
        tv.mute()
        assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    def test_mute_when_off(self):
        tv = Television()
        tv.mute()
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    def test_unmute_when_off(self):
        tv = Television()
        tv.mute()
        tv.mute()
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"


class TestChannelUp:
    def test_channel_up_off(self):
        tv = Television()
        tv.channel_up()
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    def test_channel_up_on(self):
        tv = Television()
        tv.power()
        tv.channel_up()
        assert str(tv) == "Power = True, Channel = 1, Volume = 0"

    def test_channel_up_past_max(self):
        tv = Television()
        tv.power()
        tv.channel_up()
        tv.channel_up()
        tv.channel_up()
        tv.channel_up()
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"


class TestChannelDown:
    def test_channel_down_off(self):
        tv = Television()
        tv.channel_down()
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    def test_channel_down_past_min(self):
        tv = Television()
        tv.power()
        tv.channel_down()
        assert str(tv) == "Power = True, Channel = 3, Volume = 0"


class TestVolumeUp:
    def test_volume_up_off(self):
        tv = Television()
        tv.volume_up()
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    def test_volume_up_on(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    def test_volume_up_muted(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.mute()
        tv.volume_up()
        assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    def test_volume_up_past_max(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.volume_up()
        tv.volume_up()
        assert str(tv) == "Power = True, Channel = 0, Volume = 2"


class TestVolumeDown:
    def test_volume_down_off(self):
        tv = Television()
        tv.volume_down()
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    def test_volume_down_on(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.volume_up()
        tv.volume_down()
        assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    def test_volume_down_muted(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.mute()
        tv.volume_down()
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    def test_volume_down_past_min(self):
        tv = Television()
        tv.power()
        tv.volume_down()
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"