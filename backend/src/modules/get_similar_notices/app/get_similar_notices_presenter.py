
from src.modules.get_similar_notices.app.get_similar_notices_controller import GetSimilarNoticesController
from src.modules.get_similar_notices.app.get_similar_notices_usecase import GetSimilarNoticesUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse

repo = Environments.get_notice_rag_repo()()
usecase = GetSimilarNoticesUsecase(repo=repo)
controller = GetSimilarNoticesController(usecase=usecase)


def get_similar_notices_presenter(request):
    request_data = request.body or dict(request.query_params)
    request = HttpRequest(body=dict(request_data))

    response = controller(request=request)

    return HttpResponse(body=response.body, status_code=response.status_code)
