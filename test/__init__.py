import unittest

from main import Tetris

class TestTetris(unittest.TestCase):

    def test_new_shape(self):
        game = Tetris(20, 10)
        game.new_shape()
        self.assertTrue(game.shape is not None)

    def test_block_intersects(self):
        game = Tetris(20, 10)
        game.new_shape()
        game.shape.y = 19
        self.assertTrue(game.block_intersects())

    def test_go_down(self):
        game = Tetris(20, 10)
        game.new_shape()
        game.go_down()
        self.assertTrue(game.shape.y == 1)

    def test_go_space(self):
        game = Tetris(20, 10)
        game.new_shape()
        game.go_space()
        self.assertTrue(game.shape.y == 19)

    def test_freeze(self):
        game = Tetris(20, 10)
        game.new_shape()
        game.shape.y = 19
        game.freeze()
        self.assertTrue(game.grid[19][0] == 1)

    def test_go_side(self):
        game = Tetris(20, 10)
        game.new_shape()
        game.go_side(-1)
        self.assertTrue(game.shape.x == -1)

    def test_rotate(self):
        game = Tetris(20, 10)
        game.new_shape()
        game.rotate()
        self.assertTrue(game.shape.rotation == 1)

if __name__ == '__main__':
    unittest.main()