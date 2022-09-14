import abc
import json
import logging
from enum import Enum
from typing import List, Optional, Tuple, Union

from scheduler import models


class DatastoreType(Enum):
    SQLITE = 1
    POSTGRES = 2


class Datastore:
    def __init__(self) -> None:
        self.logger: logging.Logger = logging.getLogger(__name__)


class TaskStorer(abc.ABC):
    @abc.abstractmethod
    def get_tasks(
        self,
        scheduler_id: Union[str, None],
        status: Union[str, None],
        offset: int = 0,
        limit: int = 100,
    ) -> Tuple[List[models.Task], int]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_task_by_id(self, task_id: str) -> Optional[models.Task]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_task_by_hash(self, task_hash: str) -> Optional[models.Task]:
        raise NotImplementedError

    @abc.abstractmethod
    def add_task(self, task: models.Task) -> Optional[models.Task]:
        raise NotImplementedError

    @abc.abstractmethod
    def update_task(self, task: models.Task) -> Optional[models.Task]:
        raise NotImplementedError


class PriorityQueueStorer(abc.ABC):

    @abc.abstractmethod
    def push(self, scheduler_id: str, task: models.PrioritizedItem) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def pop(self, scheduler_id: str) -> Optional[models.PrioritizedItem]:
        raise NotImplementedError

    @abc.abstractmethod
    def remove(self, scheduler_id: str) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def peek(self, scheduler_id: str) -> Optional[models.PrioritizedItem]:
        raise NotImplementedError

    @abc.abstractmethod
    def empty(self, scheduler_id: str) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def qsize(self, scheduler_id: str) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def search(self, scheduler_id: str) -> List[models.PrioritizedItem]:
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, scheduler_id: str, task: models.PrioritizedItem) -> Optional[models.PrioritizedItem]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_item_by_hash(self, scheduler_id: str, item_hash: str) -> Optional[models.PrioritizedItem]:
        raise NotImplementedError
