class InvalidCoordinateError(Exception):
    def __init__(self, coord, *args: object) -> None:
        super().__init__(*args)
        self.coord = coord

    def __str__(self) -> str:
        return f"Invalid coordinate: {self.coord}!"


class InvalidFieldValue(Exception):
    def __init__(self, val, *args: object) -> None:
        super().__init__(*args)
        self.val = val

    def __str__(self) -> str:
        return f"Invalid coordinate: {self.val}!"
