

from collections import defaultdict
from typing import List
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

        edital_similarity = defaultdict(list)

        for result in chunks:
            edital_similarity[result.notice].append(result.distance)

        edital_avg_similarity = {}
        for edital, distances in edital_similarity.items():
            avg_distance = sum(distances) / len(distances)
            edital_avg_similarity[edital] = avg_distance

        sorted_notice_similarity = sorted(
            edital_avg_similarity.items(), key=lambda x: x[1])

        sorted_chunks = []
        for notice, _ in sorted_notice_similarity:
            first_chunk = next(
                chunk for chunk in reversed(chunks) if chunk.notice == notice)
            sorted_chunks.append(first_chunk)

        return sorted_chunks
