from __future__ import annotations

from typing import TYPE_CHECKING, Iterator

from Coordinate import Coordinate as C
from Piece import Piece

if TYPE_CHECKING:
    from Board import Board
    from Move import Move

WHITE = True
BLACK = False


class Bishop(Piece):
    stringRep = 'B'
    value = 3

    def __init__(self, board: Board, side: bool, position: C, movesMade: int = 0):
        super(Bishop, self).__init__(board, side, position)
        self.movesMade = movesMade

    def getPossibleMoves(self) -> Iterator[Move]:
        currentPosition = self.position
        directions = [C(1, 1), C(1, -1), C(-1, 1), C(-1, -1)]
        for direction in directions:
            for move in self.movesInDirectionFromPos(
                    currentPosition, direction, self.side
            ):
                yield move
