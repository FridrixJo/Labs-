from abc import abstractmethod


class AbstractSerializer:
    @abstractmethod
    def create_serializer(self):
        raise NotImplemented
