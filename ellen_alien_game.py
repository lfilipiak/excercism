class Alien:
    total_alien_created = 0
    instances = []

    def __init__(self, x_coordinate, y_coordinate) -> None:
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        self.__class__.total_alien_created += 1
        self.__class__.instances.append(self)

    def hit(self):
        self.health -= 1
        return self.health

    def is_alive(self):
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(x_coordinate, y_coordinate):
        pass


def new_aliens_collection(alien_start_positions):
    return [Alien(x, y) for (x, y) in alien_start_positions]
