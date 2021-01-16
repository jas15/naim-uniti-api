from .utils import get_current_value, put_new_value

class UnitiRemote:
    """A scaled-down API for functions that only appear on the remote."""

    def __init__(self, ip_address, port=15081):
        self.ip_address = ip_address
        self.base_url = f"http://{self.ip_address}:{port}/"

    def __str__(self):
        return f"Remote to control Uniti device at {self.ip_address}"

    def current_volume(self):
        return int(get_current_value(self.base_url, "levels/room", "volume"))

    def volume_up(self):
        return self.current_volume()

    def volume_down(self):
        return self.current_volume()

    def mute_status(self):
        return int(get_current_value(self.base_url, "levels/room", "mute"))

    def toggle_mute(self):
        # get the current mute status
        current_status = self.mute_status()

        # set it to the opposite
        if current_status is not None:
            new_status = 0 if current_status > 0 else 1
            data = { "mute": new_status }
            response = put_new_value(self.base_url, "levels/room", data)
            return response

        return None

    def power_status(self):
        """Returns power status of the Uniti device - 0 for OFF, 1 for ON."""
        current_state = get_current_value(self.base_url, "power", "system")
        return current_state == "on"

    def power_toggle(self):
        """Toggles the power status of the Uniti device."""
        # get the current power status
        is_on = self.power_status()

        # set it to the opposite
        action = "lona" if is_on else "on"
        data = { "system": action }
        response = put_new_value(self.base_url, "power", data=data)

        return self.power_status()

    def previous_track(self):
        return self.current_track()

    def next_track(self):
        return self.current_track()

    def current_track(self):
        """Returns information about the current track."""
        return None

    def home(self):
        """Show the Home screen on the Uniti device."""
        return None

    def favourite_button(self):
        """Hit the favourite button on the remote."""
        return None

    def change_brightness(self):
        """Change the brightness level of the Uniti device."""
        return None

