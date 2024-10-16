from typing import List

from src.shared.domain.entities.notice_chunk import NoticeChunk
from src.shared.domain.repositories.notice_rag_repository_interface import INoticeRagRepository


class NoticeRagRepositoryMock(INoticeRagRepository):
    chunks: List[NoticeChunk]

    def __init__(self):
        self.chunks = [
            NoticeChunk(
                notice='745',
                document='http://finep.gov.br/images/chamadas-publicas/2024/07_08_2024_Regulamento_Conhecimento_Brasil.pdf',
                chunk='A presente ação encontra-se prevista no âmbito dos Programas Estruturantes e \nMobilizadores do MCTI, vinculada ao Programa 5 - Repatriação de Talentos (Conhecimento Brasil), \nque busca a repatriação de talentos científicos, tecnológicos e inovadores a serem alocados em \nInstitutos de Ciência e Tecnologia (ICTs) e empresas brasileiras para o desenvolvimento de projetos \nfocados em programas estratégicos nacionais, no desenvolvimento industrial em áreas prioritárias e \nna redução de assimetrias do Sistema Nacional de Ciência, Tecnologia e Inovação. 1.3. Entende-se por risco tecnológico a possibilidade de insucesso no desenvolvimento de \nsolução, decorrente de processo em que o resultado é incerto em função do conhecimento técnico-\ncientífico insuficiente à época em que se decide pela realização da ação (art. 2°, inciso III, decreto \n9.283/18). 1.4.',
                distance=0.8844807
            ),
            NoticeChunk(
                notice='649',
                document='http://finep.gov.br/images/chamadas-publicas/2024/07_08_2024_Regulamento_Conhecimento_Brasil.pdf',
                chunk='A presente ação encontra-se prevista no âmbito dos Programas Estruturantes e \nMobilizadores do MCTI, vinculada ao Programa 5 - Repatriação de Talentos (Conhecimento Brasil), \nque busca a repatriação de talentos científicos, tecnológicos e inovadores a serem alocados em \nInstitutos de Ciência e Tecnologia (ICTs) e empresas brasileiras para o desenvolvimento de projetos \nfocados em programas estratégicos nacionais, no desenvolvimento industrial em áreas prioritárias e \nna redução de assimetrias do Sistema Nacional de Ciência, Tecnologia e Inovação. 1.3. Entende-se por risco tecnológico a possibilidade de insucesso no desenvolvimento de \nsolução, decorrente de processo em que o resultado é incerto em função do conhecimento técnico-\ncientífico insuficiente à época em que se decide pela realização da ação (art. 2°, inciso III, decreto \n9.283/18). 1.4.',
                distance=0.88670546
            ),
            NoticeChunk(
                notice='598',
                document='http://finep.gov.br/images/chamadas-publicas/2024/07_08_2024_Regulamento_Conhecimento_Brasil.pdf',
                chunk='A presente ação encontra-se prevista no âmbito dos Programas Estruturantes e \nMobilizadores do MCTI, vinculada ao Programa 5 - Repatriação de Talentos (Conhecimento Brasil), \nque busca a repatriação de talentos científicos, tecnológicos e inovadores a serem alocados em \nInstitutos de Ciência e Tecnologia (ICTs) e empresas brasileiras para o desenvolvimento de projetos \nfocados em programas estratégicos nacionais, no desenvolvimento industrial em áreas prioritárias e \nna redução de assimetrias do Sistema Nacional de Ciência, Tecnologia e Inovação. 1.3. Entende-se por risco tecnológico a possibilidade de insucesso no desenvolvimento de \nsolução, decorrente de processo em que o resultado é incerto em função do conhecimento técnico-\ncientífico insuficiente à época em que se decide pela realização da ação (art. 2°, inciso III, decreto \n9.283/18). 1.4.',
                distance=0.92455703
            ),
            NoticeChunk(
                notice='738',
                document='http://finep.gov.br/images/chamadas-publicas/2024/07_08_2024_Regulamento_Conhecimento_Brasil.pdf',
                chunk='A presente ação encontra-se prevista no âmbito dos Programas Estruturantes e \nMobilizadores do MCTI, vinculada ao Programa 5 - Repatriação de Talentos (Conhecimento Brasil), \nque busca a repatriação de talentos científicos, tecnológicos e inovadores a serem alocados em \nInstitutos de Ciência e Tecnologia (ICTs) e empresas brasileiras para o desenvolvimento de projetos \nfocados em programas estratégicos nacionais, no desenvolvimento industrial em áreas prioritárias e \nna redução de assimetrias do Sistema Nacional de Ciência, Tecnologia e Inovação. 1.3. Entende-se por risco tecnológico a possibilidade de insucesso no desenvolvimento de \nsolução, decorrente de processo em que o resultado é incerto em função do conhecimento técnico-\ncientífico insuficiente à época em que se decide pela realização da ação (art. 2°, inciso III, decreto \n9.283/18). 1.4.',
                distance=0.93397856
            ),
            NoticeChunk(
                notice='735',
                document='http://finep.gov.br/images/chamadas-publicas/2024/07_08_2024_Regulamento_Conhecimento_Brasil.pdf',
                chunk='A presente ação encontra-se prevista no âmbito dos Programas Estruturantes e \nMobilizadores do MCTI, vinculada ao Programa 5 - Repatriação de Talentos (Conhecimento Brasil), \nque busca a repatriação de talentos científicos, tecnológicos e inovadores a serem alocados em \nInstitutos de Ciência e Tecnologia (ICTs) e empresas brasileiras para o desenvolvimento de projetos \nfocados em programas estratégicos nacionais, no desenvolvimento industrial em áreas prioritárias e \nna redução de assimetrias do Sistema Nacional de Ciência, Tecnologia e Inovação. 1.3. Entende-se por risco tecnológico a possibilidade de insucesso no desenvolvimento de \nsolução, decorrente de processo em que o resultado é incerto em função do conhecimento técnico-\ncientífico insuficiente à época em que se decide pela realização da ação (art. 2°, inciso III, decreto \n9.283/18). 1.4.',
                distance=0.9369565
            ),
        ]

    def find_similar_chunks(self, query: str, top_k: int = 100) -> List[NoticeChunk]:
        return self.chunks

    # def insert(self, chunk: NoticeChunk) -> None:
    #     self.chunks.append(alert)
