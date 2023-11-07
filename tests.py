from unittest import TestCase

from dll import DLL
from view import Operation


class TestOperation(TestCase):
    def setUp(self):
        self.song_node_map = {}
        self.dll = DLL()

        self.operation = Operation(self.dll, self.song_node_map)

    def test_play_song_one_song(self):
        self.operation.play_song("q")
        cache = self.operation.print_cache()
        self.assertEqual(["q"], cache)

    def test_play_song_multiple_song(self):
        self.operation.play_song("q")
        self.operation.play_song("w")
        self.operation.play_song("u")
        self.operation.play_song("q")

        cache = self.operation.print_cache()
        self.assertEqual(["w", "u", "q"], cache)

    def test_play_song_full(self):
        self.operation.play_song("q")
        self.operation.play_song("w")
        self.operation.play_song("u")
        self.operation.play_song("o")
        self.operation.play_song("t")

        cache = self.operation.print_cache()
        self.assertEqual(["w", "u", "o", "t"], cache)

    def test_play_last_song(self):
        self.operation.play_song("q")
        self.operation.play_song("w")
        self.operation.play_song("u")
        self.operation.play_song("q")

        song = self.operation.play_last_song()
        self.assertEqual(song, "Last song was q")

    def test_play_last_song_empty(self):
        song = self.operation.play_last_song()
        self.assertEqual(song, "No song was played")

    def test_print_cache_empty(self):
        cache = self.dll.print_dll()
        self.assertEqual(cache, [])
