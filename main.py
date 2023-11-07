"""
driver class
"""

from enum import Enum

from dll import DLL
from view import Operation


class Command(str, Enum):
    play_song = 1
    play_last_song = 2
    print_cache = 3


"""
We will use DLL and dictionary to store the cache
Dict = {key-> song_name, value-> DLL node}
"""
song_node_map = {}
dll = DLL()

operation = Operation(dll, song_node_map)

while True:
    command = input(
        """
    Options:
    1. play_song 
    2. play_last_song
    3. print_cache
    """
    )
    if command == Command.play_song.value:
        song_name = input("song name: ")
        result = operation.play_song(song_name)
    elif command == Command.play_last_song.value:
        result = operation.play_last_song()
    elif command == Command.print_cache.value:
        result = operation.print_cache()
    else:
        result = "Invalid choice"

    print(result)
