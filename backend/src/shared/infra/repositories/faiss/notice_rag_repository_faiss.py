from typing import List

from src.shared.domain.entities.notice_chunk import NoticeChunk
from src.shared.domain.repositories.notice_rag_repository_interface import INoticeRagRepository

import faiss

import pandas as pd
from langchain.schema import Document
from langchain_community.vectorstores import FAISS
# from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

model_name = 'all-MiniLM-L6-v2'
embeddings_model = HuggingFaceEmbeddings(model_name=model_name)


class SimpleDocstore:
    def __init__(self, docstore):
        self.docstore = docstore

    def search(self, doc_id):
        metadata = self.docstore.get(doc_id)
        if metadata is not None:
            return Document(page_content="", metadata=metadata)
        return None


class NoticeRagRepositoryFaiss(INoticeRagRepository):
    chunks: List[NoticeChunk]

    def __init__(self):
        # self.index = faiss.read_index("editais_faiss_index.bin")

        self.df_rag = pd.read_csv(
            'src/shared/infra/repositories/faiss/editais_finep_textos_embeddings.csv')
        self.df_rag['pdf_text'] = self.df_rag['pdf_text'].fillna('')
        self.df_rag['pdf_text'] = self.df_rag['pdf_text'].astype(str)
        self.loaded_faiss_index = self.load_faiss_index(
            'src/shared/infra/repositories/faiss/faiss_index.index', embeddings_model, self.df_rag)

    def find_similar_chunks(self, query: str, top_k: int = 100) -> List[NoticeChunk]:
        results = self.loaded_faiss_index.similarity_search_with_score(
            query, k=top_k)

        formatted_results = []
        for doc, score in results:
            # formatted_results.append({
            #     'edital_number': doc.metadata['edital_number'],
            #     'pdf_link': doc.metadata['pdf_link'],
            #     'score': score  # Agora, temos acesso ao score
            # })
            formatted_results.append(NoticeChunk(
                notice=doc.metadata['edital_number'],
                document=doc.metadata['pdf_link'],
                chunk=doc.page_content,
                distance=score
            ))

        return formatted_results

    def load_faiss_index(self, file_path, embeddings_model, df):
        index = faiss.read_index(file_path)
        docstore = {i: {'edital_number': df['edital_number'].iloc[i],
                        'pdf_link': df['pdf_link'].iloc[i]} for i in range(len(df))}
        custom_docstore = SimpleDocstore(docstore)
        index_to_docstore_id = {i: i for i in range(len(df))}
        return FAISS(embedding_function=embeddings_model, index=index, docstore=custom_docstore, index_to_docstore_id=index_to_docstore_id)

    # def insert(self, chunk: NoticeChunk) -> None:
    #     self.chunks.append(alert)
