# import datetime

# from src.modules.get_similar_notices.app.get_similar_notices_controller import GetAllAlertsController
# from src.modules.get_similar_notices.app.get_similar_notices_usecase import GetAllAlertsUsecase
# from src.shared.helpers.external_interfaces.http_models import HttpRequest


# class Test_GetAllAlertsController:

#     def test_get_all_alerts_controller(self):
#         repo = AlertsRepositoryMock()
#         usecase = GetAllAlertsUsecase(repo=repo)
#         controller = GetAllAlertsController(usecase=usecase)

#         request = HttpRequest(body={})

#         response = controller(request=request)

#         assert response.status_code == 200
#         assert type(response.body['alerts']) == list
#         assert len(response.body['alerts']) == len(repo.alerts)
