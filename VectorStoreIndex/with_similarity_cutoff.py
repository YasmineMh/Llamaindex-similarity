from llama_index import SimpleDirectoryReader, VectorStoreIndex
from llama_index.indices.postprocessor import SimilarityPostprocessor

# print(documents)
documents = SimpleDirectoryReader('./files').load_data()
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine(
    node_postprocessors=[
        SimilarityPostprocessor(similarity_cutoff=0.7)
    ]
)
retriever = index.as_retriever()

# set a breakpoint to inspect
# import pdb
# pdb.set_trace()
question = "what is a programming language?"
nodes = retriever.retrieve(question)
print(nodes)
response = query_engine.query(question)
print(response)
print(len(response.source_nodes)) #nodes
print("Done!")