from src.modules.get_similar_notices.app.get_similar_notices_usecase import GetSimilarNoticesUsecase
from src.modules.get_similar_notices.app.get_similar_notices_viewmodel import GetSimilarNoticesViewmodel
from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError


class GetSimilarNoticesController:

    def __init__(self, usecase: GetSimilarNoticesUsecase):
        self.GetSimilarNoticesUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            query = request.data.get('query')
            if query is None:
                raise MissingParameters('query')
            similar_notices = self.GetSimilarNoticesUsecase(query=query)

            viewmodel = GetSimilarNoticesViewmodel(similar_notices)

            return OK(viewmodel.to_dict())

        except NoItemsFound as err:

            return NotFound(body=err.message)

        except MissingParameters as err:

            return BadRequest(body=err.message)

        except WrongTypeParameter as err:

            return BadRequest(body=err.message)

        except EntityError as err:

            return BadRequest(body=err.message)

        except Exception as err:

            return InternalServerError(body=err.args[0])
