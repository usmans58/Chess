from __future__ import annotations

from typing import TYPE_CHECKING, Iterator

from Coordinate import Coordinate as C
from Move import Move
from Piece import Piece

if TYPE_CHECKING:
    from Board import Board

WHITE = True
BLACK = False


class Rook(Piece):
    stringRep = 'R'
    value = 5

    def __init__(self, board: Board, side: bool, position: C, movesMade: int = 0):
        super(Rook, self).__init__(board, side, position)
        self.movesMade = movesMade

    def getPossibleMoves(self) -> Iterator[Move]:
        currentPosition = self.position

        directions = [C(0, 1), C(0, -1), C(1, 0), C(-1, 0)]
        for direction in directions:
            for move in self.movesInDirectionFromPos(
                    currentPosition, direction, self.side
            ):
                yield move
