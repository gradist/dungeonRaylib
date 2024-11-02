import pyray

class SceneMenu:
    def __init__(self, fps = 60):
        pass

    def draw(self):
        pyray.clear_background(pyray.BROWN)

    def update(self) -> str | None:
        return None


class SceneGame:
    def __init__(self):
        pass

    def draw(self):
        pyray.clear_background(pyray.BLACK)

    def update(self) -> str | None:
        return None
