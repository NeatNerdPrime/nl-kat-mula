import abc
import datetime
import logging
from typing import List, Optional, Tuple, Union

from scheduler import models


class Datastore:
    def __init__(self) -> None:
        self.logger: logging.Logger = logging.getLogger(__name__)


class TaskStorer(abc.ABC):
    def __init__(self) -> None:
        self.logger: logging.Logger = logging.getLogger(__name__)

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
    def create_task(self, task: models.Task) -> Optional[models.Task]:
        raise NotImplementedError

    @abc.abstractmethod
    def update_task(self, task: models.Task) -> Optional[models.Task]:
        raise NotImplementedError


class PriorityQueueStorer(abc.ABC):
    def __init__(self) -> None:
        self.logger: logging.Logger = logging.getLogger(__name__)

    @abc.abstractmethod
    def push(self, scheduler_id: str, item: models.PrioritizedItem) -> Optional[models.PrioritizedItem]:
        raise NotImplementedError

    @abc.abstractmethod
    def pop(self, scheduler_id: str, filters: List[models.Filter] = None) -> Optional[models.PrioritizedItem]:
        raise NotImplementedError

    @abc.abstractmethod
    def remove(self, scheduler_id: str, item_id: str) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def peek(self, scheduler_id: str, index: int) -> Optional[models.PrioritizedItem]:
        raise NotImplementedError

    @abc.abstractmethod
    def empty(self, scheduler_id: str) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def qsize(self, scheduler_id: str) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, scheduler_id: str, item: models.PrioritizedItem) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def get_item_by_hash(self, scheduler_id: str, item_hash: str) -> Optional[models.PrioritizedItem]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_items_by_scheduler_id(self, scheduler_id: str) -> List[models.PrioritizedItem]:
        raise NotImplementedError


class JobStorer(abc.ABC):
    def __init__(self) -> None:
        self.logger: logging.Logger = logging.getLogger(__name__)

    # TODO: filters
    def get_scheduled_jobs(self) -> Tuple[List[models.ScheduledJob], int]:
        raise NotImplementedError

    def create_scheduled_job(self, job: models.ScheduledJob) -> Optional[models.ScheduledJob]:
        raise NotImplementedError

    def get_scheduled_job(self, job_id: str) -> Optional[models.ScheduledJob]:
        raise NotImplementedError

    def update_scheduled_job(self, job: models.ScheduledJob) -> Optional[models.ScheduledJob]:
        raise NotImplementedError