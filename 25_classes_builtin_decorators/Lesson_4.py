# Task 1. Transport 2

from abc import ABC, abstractmethod


class TransportPark(ABC):
    """
    Abstract base class for transport

    Args:
        color (str): color of transport
        speed (int): speed of transport
    """

    def __init__(self, color: str, speed: int = 0) -> None:
        self._color = color
        self._speed = speed

    @abstractmethod
    def move(self) -> None:
        """Any transport may move"""
        pass

    @abstractmethod
    def signal(self) -> None:
        """Any transport may do signal"""
        pass

    @property
    def color(self):
        return self._color

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, val):
        self._speed = val


class AudioPlayerMixin:
    """
    Mixin class for additional feature as an audio system

    Attributes:
        _music_on (bool): Audio system status (default: False)
    """
    _music_on: bool = False

    def audio_on(self) -> str:
        """
        Turn audio player ON

        :return: result of this action
        :rtype: str
        """
        self._music_on = True
        return 'Audio player is on'

    def audio_off(self) -> str:
        """
        Turn audio player OFF

        :return: result of this action
        :rtype: str
        """
        self._music_on = False
        return 'Audio player is off'


class Car(TransportPark):
    """
    Class Car. Parent: TransportPark

    Args:
        color (str): color of transport
        speed (int): speed of transport
        ttype (str): mark of the car
    """

    def __init__(self, color: str, ttype: str, speed: int = 0) -> None:
        super().__init__(color, speed)
        self._ttype = ttype

    def __str__(self) -> str:
        return 'This is the{ttype}'.format(ttype=self._ttype)

    def move(self, way_to_move='ground') -> str:
        """
        Do move

        :param way_to_move: area for moving
        :type way_to_move: str
        :return: result of this action
        :rtype: str
        """
        if way_to_move == 'ground':
            self.speed = 630
            return 'the car is driving now\nspeed: {} km/h'.format(self.speed)
        else:
            return 'the car may drive only on ground!'

    def signal(self) -> str:
        return 'Boo!'


class Boat(TransportPark):
    """
    Class boat. Parent TransportPark

    Args:
        color (str): color of transport
        speed (int): speed of transport
        name (str): name of the boat
    """

    def __init__(self, color: str, speed: int, name: str) -> None:
        super().__init__(color, speed)
        self._name = name

    def __str__(self) -> str:
        return 'This is the {color} {name} boat'.format(color=self._color, name=self._name)

    def move(self, way_to_move='water') -> str:
        if way_to_move == 'water':
            self._speed = 70
            return 'the boat went into the sea\nspeed: {} km/h'.format(self._speed)
        else:
            return 'the boat may move only on water!'

    def signal(self) -> str:
        return 'Bam!'


class Amphibian(TransportPark, AudioPlayerMixin):

    def __str__(self) -> str:
        return 'This is the {color} amphibian'.format(color=self._color)

    def move(self, way_to_move: str = 'water') -> str:
        """
        Do move

        :param way_to_move: area for moving
        :type way_to_move: str
        :return: result of this action
        :rtype: str
        """
        if way_to_move == 'water':
            self._speed = 40
            return 'the amphibian went into the sea\nspeed: {} km/h'.format(self._speed)
        else:
            self._speed = 60
            return 'the amphibian is driving now\nspeed: {} km/h'.format(self._speed)

    def signal(self) -> str:
        return 'Bim!'


sport_car = Car(color='red', ttype='Ford')
amph = Amphibian('blue')
print(amph)
print(sport_car)
print(sport_car.move())
print(amph.move())
print(sport_car.move())

print()

print(amph.color, amph.speed)
