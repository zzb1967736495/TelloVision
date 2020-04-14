import abc
import socket
import threading


class Drone(abc.ABC):

    @abc.abstractmethod
    def connect(self):
        """
        connecting the drone

        Returns:
            True if responded, false if not
        """
        pass

    @abc.abstractmethod
    def __send_command(self, command: str):
        """Abstract method for command sending to the drone
        Args:
            command : the command you would like to send

        Returns:
            Response from the drone

        """
        pass

    @abc.abstractmethod
    def takeoff(self):
        """
        Initiate takeoff
        """
        pass

    @abc.abstractmethod
    def land(self):
        pass

    def move(self, direction: str, x: int):
        pass

    @abc.abstractmethod
    def emergency(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass

    @abc.abstractmethod
    def move_up(self, x: int):
        pass

    @abc.abstractmethod
    def move_down(self, x: int):
        pass

    @abc.abstractmethod
    def move_right(self, x: int):
        pass

    @abc.abstractmethod
    def move_left(self, x: int):
        pass

    @abc.abstractmethod
    def move_forward(self, x: int):
        pass

    @abc.abstractmethod
    def move_backward(self, x: int):
        pass

    @abc.abstractmethod
    def rotate_clockwise(self, x:int):
        pass

    @abc.abstractmethod
    def rotate_counter_clockwise(self, x:int):
        pass

    @abc.abstractmethod
    def go_to(self, x: int, y: int, z: int, speed: int):
        pass

    @abc.abstractmethod
    def go_to_curve (self, x1: int, x2: int, y1: int, y2: int, z1: int, z2: int, speed: int):
        pass





