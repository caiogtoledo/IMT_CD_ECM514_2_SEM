from typing import Optional
from src.shared.domain.entities.notice_chunk import NoticeChunk


class NoticeViewmodel:
    notice: str
    document: str
    chunk: str
    distance: float

    def __init__(self, notice: NoticeChunk):
        self.notice = notice.notice
        self.document = notice.document
        self.chunk = notice.chunk
        self.distance = notice.distance

    def to_dict(self):
        return {
            'notice': str(self.notice),
            'document': self.document,
            'chunk': self.chunk,
            'distance': str(self.distance)
        }


class GetSimilarNoticesViewmodel:
    similar_notices: list[NoticeViewmodel]

    def __init__(self, notices: list[NoticeChunk]):
        self.similar_notices = [NoticeViewmodel(
            notice).to_dict() for notice in notices]

    def to_dict(self):
        return {
            'similar_notices': self.similar_notices
        }
