import abc, copy
from fruits.geometry.vector2d import Vector2D
import fruits.geometry.angle as angle2d
from fruits.game_entity import GameEntity


class GameObjectTransform:
    def __init__(self,  position: Vector2D = None, velocity: Vector2D = None,
                 orientation: float = 0.0, angular_vel: float = 0.0):
        self.__position = position
        self.__velocity = velocity
        self.__orientation = orientation
        self.__angular_vel = angular_vel

        if self.__position is None:
            self.__position = Vector2D(0, 0)
        if self.__velocity is None:
            self.__velocity = Vector2D(0, 0)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value: Vector2D):
        if value is not None:
            self.__position = value

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, value: Vector2D):
        if value is not None:
            self.__velocity = value

    @property
    def orientation(self):
        return self.__orientation

    @orientation.setter
    def orientation(self, value: float):
        if value is not None:
            self.__orientation = angle2d.fit(value, angle2d.MODE_ZERO_2PI)

    @property
    def angular_vel(self):
        return self.__angular_vel

    @angular_vel.setter
    def angular_vel(self, value: float):
        if value is not None:
            self.__angular_vel = value


class GameObject(GameEntity, abc.ABC):
    def __init__(self, initial_transform: GameObjectTransform = None) -> None:
        GameEntity.__init__(self)

        self._transform = initial_transform
        if self._transform is None:
            self._transform = GameObjectTransform()
        self._enqueued_transform = None

        self.mesh = None
        self.collider = None
        self.rigid_body = None

    @property
    def transform(self):
        if self._enqueued_transform is None:
            self._enqueued_transform = copy.deepcopy(self._transform)
        return self._enqueued_transform

    @property
    def last_position(self):
        return self._transform.position

    @property
    def position(self):
        return self.transform.position

    @position.setter
    def position(self, value: Vector2D):
        self.transform.position = value

    @property
    def last_velocity(self):
        return self._transform.velocity

    @property
    def velocity(self):
        return self.transform.velocity

    @velocity.setter
    def velocity(self, value: Vector2D):
        self.transform.velocity = value

    @property
    def last_orientation(self):
        return self._transform.orientation

    @property
    def orientation(self):
        return self.transform.orientation

    @orientation.setter
    def orientation(self, value: float):
        self.transform.orientation = value

    @property
    def last_angular_vel(self):
        return self._transform.angular_vel

    @property
    def angular_vel(self):
        return self.transform.angular_vel

    @angular_vel.setter
    def angular_vel(self, value: float):
        self.transform.angular_vel = value

    @abc.abstractmethod
    def init(self) -> None:
        pass

    def flush_transform(self) -> None:
        if self._enqueued_transform is not None:
            self._transform = self._enqueued_transform
        self._enqueued_transform = None

    def update_components(self) -> None:
        if self.mesh is not None:
            self.mesh.rect.topleft = (self.position.x, self.position.y)
        if self.collider is not None:
            # TODO: Collider may have different rect than mesh
            self.collider.rect = self.mesh.rect



