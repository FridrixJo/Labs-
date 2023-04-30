from abc import abstractmethod


class Parser:
    @abstractmethod
    def dump(self, obj, fp):
        raise NotImplemented

    @abstractmethod
    def dumps(self, obj):
        raise NotImplemented

    @abstractmethod
    def load(self, s):
        raise NotImplemented

    @abstractmethod
    def loads(self, s):
        raise NotImplemented
