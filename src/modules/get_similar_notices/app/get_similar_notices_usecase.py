

import datetime
from typing import List, Optional
from src.shared.domain.entities.notice_chunk import NoticeChunk
from src.shared.domain.repositories.notice_rag_repository_interface import INoticeRagRepository
from src.shared.helpers.errors.usecase_errors import CreationError


class GetSimilarNoticesUsecase:
    def __init__(self, repo: INoticeRagRepository):
        self.repo = repo

    def __call__(self, query: str) -> List[NoticeChunk]:
        chunks = self.repo.find_similar_chunks(query)

        if not chunks:
            raise CreationError('No similar notices found')

        return chunks
