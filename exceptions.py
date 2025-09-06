class InvalidCoordinateError(Exception):
    def __init__(self, coord, *args: object) -> None:
        super().__init__(*args)
        self.coord = coord

    def __str__(self) -> str:
        return f"Invalid coordinate: {self.coord}!"
