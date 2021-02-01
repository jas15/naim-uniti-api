from .remote import UnitiRemote

class NaimUniti(UnitiRemote):
    """Class that adds functionality to what is already created in the UnitiRemote class."""

    def __init__(self, ip_address, port=None):
        if port is None:
            super().init(ip_address)
        else:
            super().init(ip_address, port)
