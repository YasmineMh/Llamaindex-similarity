from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, StorageContext
from llama_index.indices.postprocessor import SimilarityPostprocessor
from llama_index.vector_stores import WeaviateVectorStore


import weaviate
from langchain import OpenAI


WEAVIATE_URN = "http://127.0.0.1:8083"
client = weaviate.Client(url=WEAVIATE_URN)
vector_store = WeaviateVectorStore(weaviate_client=client, class_prefix="Similarity_cutoff")
storage_context = StorageContext.from_defaults(vector_store=vector_store)


documents = SimpleDirectoryReader('./files').load_data()
index = GPTVectorStoreIndex.from_documents(documents, storage_context=storage_context)

query_engine = index.as_query_engine(
)
retriever = index.as_retriever()


question = "what is a programming language?"
nodes = retriever.retrieve(question)
print(nodes)
response = query_engine.query(question)
print(response)
print(len(response.source_nodes)) #nodes
print("Done!")