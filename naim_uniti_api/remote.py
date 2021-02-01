from .utils import get_current_value, put_new_value

class UnitiRemote:
    """A scaled-down API for functions that only appear on the remote."""

    def __init__(self, ip_address, port=15081):
        self.ip_address = ip_address
        self.base_url = f"http://{self.ip_address}:{port}/"

    def __str__(self):
        return f"Remote to control Uniti device at {self.ip_address}"

    def current_volume(self):
        # tested works
        return int(get_current_value(self.base_url, "levels/room", "volume"))

    def _change_volume(self, new_value):
        # tested works
        path = f"levels/room?volume={new_value}"
        return put_new_value(self.base_url, path)

    def volume_up(self, increment=1):
        # tested works
        vol = self.current_volume()
        if vol is not None:
            return self._change_volume(min(vol + increment, 100))

        return None

    def volume_down(self, increment=1):
        # tested works
        vol = self.current_volume()
        if vol is not None:
            return self._change_volume(max(vol - increment, 0))

        return None

    def mute_status(self):
        # tested works
        return int(get_current_value(self.base_url, "levels/room", "mute"))

    def toggle_mute(self):
        # tested works
        # get the current mute status
        current_status = self.mute_status()

        # set it to the opposite
        if current_status is not None:
            new_status = 0 if current_status > 0 else 1
            data = { "mute": new_status }
            path = f"levels/room?mute={new_status}"
            response = put_new_value(self.base_url, path)
            return response

        return None

    def power_status(self):
        """Returns power status of the Uniti device - 0 for OFF, 1 for ON."""
        # tested works
        current_state = get_current_value(self.base_url, "power", "system")
        return current_state

    def power_toggle(self):
        """Toggles the power status of the Uniti device."""
        # tested works
        # get the current power status
        is_on = self.power_status() == "on"

        # set it to the opposite
        action = "lona" if is_on else "on"
        path = f"power?system={action}"
        response = put_new_value(self.base_url, path)

        return self.power_status() == "on"

    def _control_playback(self, action):
        # tested works
        return get_current_value(
                self.base_url,
                "nowplaying",
                params={ "cmd": action }
        )

    def play_pause(self):
        # tested works
        return self._control_playback("playpause")

    def previous_track(self):
        # tested works
        return self._control_playback("prev")

    def next_track(self):
        # tested works
        return self._control_playback("next")

    def now_playing(self):
        """Returns information about the current track."""
        path = get_current_value(self.base_url, "inputs/playqueue", value="current")
        return get_current_value(self.base_url, path)

    def home(self):
        """Show the Home screen on the Uniti device."""
        # TODO implement
        return None

    def favourite_button(self):
        """Hit the favourite button on the remote."""
        # TODO implement
        return None

    def change_brightness(self):
        """Change the brightness level of the Uniti device."""
        # TODO implement
        return None

