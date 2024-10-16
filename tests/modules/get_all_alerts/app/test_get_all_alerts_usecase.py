# import datetime
# import pytest

# from src.modules.get_similar_notices.app.get_similar_notices_usecase import GetAllAlertsUsecase
# from src.shared.domain.entities.notice_chunk import NoticeChunk
# from src.shared.helpers.errors.usecase_errors import CreationError
# from src.shared.infra.repositories.notice_rag_repository_mock import AlertsRepositoryMock


# class Test_GetAllAlertsUsecase:

#     def test_get_all_alerts(self):
#         repo = AlertsRepositoryMock()
#         usecase = GetAllAlertsUsecase(repo)

#         alerts = usecase()

#         assert all(type(alert) == Alert for alert in alerts)
#         assert len(alerts) == len(repo.alerts)
#         assert type(repo.alerts) == list
