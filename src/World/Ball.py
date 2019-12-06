import pymunk


class Ball:
    def __init__(self, x1, y1, masse, rayon, elasticity):
        self.x1 = x1
        self.y1 = y1
        self.masse = masse
        self.rayon = rayon
        self.moment = pymunk.moment_for_circle(masse, 0, rayon, (x1, y1))
        self.body = pymunk.Body(masse, self.moment)
        self.body.position = x1, y1
        self.shape = pymunk.Circle(self.body, rayon)
        self.shape.elasticity = elasticity
