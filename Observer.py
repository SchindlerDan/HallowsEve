#```Python
from abc import ABCMeta, abstractmethod
 #copied from slides
class Observer(object):
        __metaclass__ = ABCMeta
 
        @abstractmethod
        def update(self):
                pass