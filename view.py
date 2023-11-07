from dll import Node, DLL

CACHE_LIMIT = 4  # limit of cache. Only these many songs will be stored at a time


class Operation:
    def __init__(self, dll: DLL, song_node_map: dict):
        self.dll = dll
        self.song_node_map = song_node_map

    def play_song(self, song_name: str):
        """

        :param song_name: song name to be played
        :return:

        If song is present in cache (song_node_map) then we need to bring the node to latest
        If song is not present in the class then create a new Node and add a new key to song_node_map
        """
        node = self.song_node_map.get(song_name)
        if node:
            self.dll.remove_element(node)
            self.dll.add_node_at_end(node)

        else:
            node = Node(song_name)
            self.dll.add_node_at_end(node)
            self.song_node_map[song_name] = node
            if len(self.song_node_map) > CACHE_LIMIT:
                self.dll.remove_element(self.dll.HEAD_NODE)
                self.song_node_map.pop(song_name)

        return f"Song {song_name} Started..."

    def play_last_song(self):
        """
        Last node of DLL will be played
        :return:
        """
        last_song_node = self.dll.END_NODE
        if not last_song_node:
            return "No song was played"
        return f"Last song was {last_song_node.val}"

    def print_cache(self):
        """
        Print all the songs in the cache
        :return:
        """
        value_list = self.dll.print_dll()
        return value_list
