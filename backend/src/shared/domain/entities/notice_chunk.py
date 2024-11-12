import abc
from typing import Optional
import uuid

from src.shared.helpers.errors.domain_errors import EntityError


class NoticeChunk(abc.ABC):
    notice: str
    document: str
    chunk: str
    distance: float

    def __init__(self,
                 notice: str,
                 document: float,
                 chunk: str,
                 distance: float
                 ):
        self.notice = notice
        self.document = document
        self.chunk = chunk
        self.distance = distance

    def __repr__(self):
        return (f"NoticeChunk(notice={self.notice}, document={self.document}, "
                f"message={self.message}, "
                f"chunk={self.chunk}, "
                f"distance={self.distance}"
                )
