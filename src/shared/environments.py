from enum import Enum
import os

from src.shared.domain.repositories.notice_rag_repository_interface import INoticeRagRepository


class STAGE(Enum):
    DOTENV = "DOTENV"
    DEV = "DEV"
    HOMOLOG = "HOMOLOG"
    PROD = "PROD"
    TEST = "TEST"


class Environments:
    """
    Defines the environment variables for the application. You should not instantiate this class directly. Please use Environments.get_envs() method instead.

    Usage:

    """
    stage: STAGE
    mongo_uri: str
    mongo_db_name: str

    def _configure_local(self):
        from dotenv import load_dotenv
        load_dotenv()
        os.environ["ENV"] = os.environ.get("ENV") or STAGE.DOTENV.value

    def load_envs(self):
        if "ENV" not in os.environ or os.environ["ENV"] == STAGE.DOTENV.value:
            self._configure_local()

        self.stage = STAGE[os.environ.get("ENV")]
        # self.mongo_uri = os.environ.get("MONGO_URI")
        # self.mongo_db_name = os.environ.get("DB_NAME")

    @staticmethod
    def get_notice_rag_repo() -> INoticeRagRepository:
        if Environments.get_envs().stage == STAGE.TEST:
            from src.shared.infra.repositories.notice_rag_repository_mock import NoticeRagRepositoryMock
            return NoticeRagRepositoryMock
        elif Environments.get_envs().stage in [STAGE.DEV, STAGE.HOMOLOG, STAGE.PROD]:
            from src.shared.infra.repositories.faiss.notice_rag_repository_faiss import NoticeRagRepositoryFaiss
            return NoticeRagRepositoryFaiss
        else:
            raise Exception("No repository found for this stage")

    @staticmethod
    def get_envs() -> "Environments":
        """
        Returns the Environments object. This method should be used to get the Environments object instead of instantiating it directly.
        :return: Environments (stage={self.stage}, s3_bucket_name={self.s3_bucket_name}, region={self.region}, endpoint_url={self.endpoint_url})

        """
        envs = Environments()
        envs.load_envs()
        return envs

    def __repr__(self):
        return self.__dict__
