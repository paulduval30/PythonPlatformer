import pymunk


class Plateforme:
    def __init__(self,x1, y1, width, height, space, elasticity):
        self.x1 = x1
        self.x2 = x1 + width
        self.y1 = y1
        self.y2 = y1
        self.width = width
        self.height = height
        self.thick = width if width < height else height
        self.segment = pymunk.Segment(space.static_body, (x1, y1), (self.x2, self.y2), self.thick)
        self.segment.elasticity = elasticity

