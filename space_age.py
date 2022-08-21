class SpaceAge:
    def __init__(self, seconds) -> None:
        self.seconds = seconds

    def on_earth(self):
        return float(f"{self.seconds / 31557600:.2f}")
    
    def on_mercury(self):
        return float(f"{self.seconds / 31557600 / 0.2408467:.2f}")

    def on_venus(self):
        return float(f"{self.seconds / 31557600 / 0.61519726:.2f}")

    def on_mars(self):
        return float(f"{self.seconds / 31557600 / 1.8808158:.2f}")

    def on_jupiter(self):
        return float(f"{self.seconds / 31557600 / 11.862615:.2f}")

    def on_saturn(self):
        return float(f"{self.seconds / 31557600 / 29.447498:.2f}")

    def on_uranus(self):
        return float(f"{self.seconds / 31557600 / 84.016846:.2f}")

    def on_neptune(self):
        return float(f"{self.seconds / 31557600 / 164.79132:.2f}")

alien = SpaceAge(2134835688)
print(alien.on_mercury())