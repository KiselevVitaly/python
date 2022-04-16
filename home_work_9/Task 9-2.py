class Road:
    _length, _width = 0, 0

    def __init__(self, length, width, weight_sr_mt, thickness):
        self._width_sq_mt, self._thickness, self._length, self._width = weight_sr_mt / 1000, thickness, length, width

    def asphalt(self):
        return self._length * self._width * self._width_sq_mt * self._thickness


calc = Road(5000, 20, 25, 5)
print(calc.asphalt())