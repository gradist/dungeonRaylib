import pyray as pr
from scenes import SceneMenu, SceneGame


class Application:
    def __init__(self, w: int, h: int, title: str, fps: int = 60):
        pr.init_window(w, h, title)
        pr.set_target_fps(fps)

        self.scenes = {
            'menu': SceneMenu(),
            'game': SceneGame()
        }
        self.current_scene = 'menu'

    def draw(self):
        pr.begin_drawing()
        self.scenes[self.current_scene].draw()
        pr.end_drawing()

    def update(self):
        next_scene = self.scenes[self.current_scene].update()
        if next_scene in self.scenes:
            self.current_scene = next_scene

    def run(self):
        while not pr.window_should_close():
            self.update()
            self.draw()
