# TODO this script should create a new Uniti station given an IP arg,
# port number and optional --test arg, then call a few as-yet-undefined things.
from naim_uniti_api import UnitiRemote
import os
import argparse
import readchar
import tkinter


def print_choices():
    print("\n")
    choices = get_choices_and_responses()
    for ch in choices:
        s = ch
        if len(choices[ch]) > 2:
            s = choices[ch][2]

        print("[{}] {}".format(s, choices[ch][0]))


def get_choices_and_responses():
    return {
        readchar.key.SPACE: ("Play/pause", "Playing/pausing.", " "),
        readchar.key.UP: ("Volume up", "Upping the volume.", '\u2191'),
        readchar.key.DOWN: ("Volume down", "Lowering it.", '\u2193'),
        "v": ("Current volume", "Here you go."),
        "m": ("Mute", "Toggling mute."),
        "n": ("What's playing", "Here's some info."),
        readchar.key.LEFT: ("Previous song", "Playing the previous song.", '\u2190'),
        readchar.key.RIGHT: ("Next song", "Playing the next song.", '\u2192'),
        "q": ("Quit", "Thanks for playing. Bye!"),
        "p": ("Power status", "Hope that helped."),
        "P": ("Power toggle", "Eek."),
    }


def make_choice(remote, choice):
    options = get_choices_and_responses()
    os.system('clear')
    valid = True
    if choice == readchar.key.SPACE:
        remote.play_pause()
    elif choice == "v":
        print("Volume: " + str(remote.current_volume()))
        valid = False
    elif choice == readchar.key.UP:
        remote.volume_up(increment=5)
    elif choice == readchar.key.DOWN:
        remote.volume_down(increment=5)
    elif choice == "m":
        remote.toggle_mute()
    elif choice == "n":
        print("Now playing:")
        np = remote.now_playing()
        track = np["name"]
        artist = np["artistName"]
        album = np["albumName"]
        print(f"{track} by {artist} from {album}")
        valid = False
    elif choice == "p":
        print("Power:")
        print(remote.power_status())
        valid = False
    elif choice == "P":
        remote.power_toggle()
    elif choice == readchar.key.LEFT:
        remote.previous_track()
    elif choice == readchar.key.RIGHT:
        remote.next_track()
    elif choice != "q":
        valid = False
        print(f"Choice invalid: {choice}")

    if valid:
        print(options[choice][1])

    return valid


def get_arguments():
    parser = argparse.ArgumentParser(description="Terminal Naim", formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--ip-address", required=True, type=str, dest="ip_address")
    parser.add_argument("--port", required=False, type=str, dest="port")

    return parser.parse_args()


def print_info(remote, print_playing=True, print_volume=True):
    if print_playing:
        np = remote.now_playing()
        track = np["name"]
        artist = np["artistName"]
        album = np["albumName"]
        print(f"Playing: {track} by {artist} from {album}")

    if print_volume:
        print("Volume: " + str(remote.current_volume()))

    muted = remote.mute_status()
    if muted is not None and muted > 0:
        print("Muted.")


### MAIN PROGRAM ###
if __name__ == '__main__':
    args = get_arguments()

    remote = None
    if args.port:
        remote = UnitiRemote(args.ip_address, port=args.port)
    else:
        remote = UnitiRemote(args.ip_address)

    # Set up a loop where users can choose what they'd like to do.
    choice = ""

    while choice != "q":

        # Let users know what they can do.
        print_choices()

        print("What would you like to do?")
        choice = readchar.readkey()

        # Respond to the user's choice.
        make_choice(remote, choice)
        print_info(remote, choice != "n", choice != "v")

