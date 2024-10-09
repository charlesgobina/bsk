class Frame:

    def __init__(self, first_throw: int, second_throw: int):
        self._first_throw = first_throw
        self._second_throw = second_throw
        self._bonus_throw = 0
        self._is_final_frame = False

    def score(self) -> int:
        return self._first_throw + self._second_throw + self._bonus_throw

    def is_strike(self) -> bool:
        return self._first_throw == 10

    def is_spare(self) -> bool:
        return not self.is_strike() and (self._first_throw + self._second_throw == 10)

    def is_last_frame(self) -> bool:
        return self._is_final_frame

    def set_bonus(self, bonus_throw: int) -> None:
        self._bonus_throw = bonus_throw
