from abc import ABC, abstractmethod
from typing import List
from src.shared.domain.entities.notice_chunk import NoticeChunk


class INoticeRagRepository(ABC):

    @abstractmethod
    def find_similar_chunks(self, query: str, top_k: int = 100) -> List[NoticeChunk]:
        pass

    # @abstractmethod
    # def insert(self, alert: Alert) -> None:
    #     pass
