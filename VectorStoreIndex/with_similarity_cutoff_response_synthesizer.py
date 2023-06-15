from llama_index import SimpleDirectoryReader, VectorStoreIndex, ResponseSynthesizer
from llama_index.indices.postprocessor import SimilarityPostprocessor
from llama_index.retrievers import VectorIndexRetriever
from llama_index.query_engine import RetrieverQueryEngine

# print(documents)
documents = SimpleDirectoryReader('./files').load_data()
print(documents)
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine(
    node_postprocessors=[
        SimilarityPostprocessor(similarity_cutoff=0.7)
    ]
)
retriever = VectorIndexRetriever(
    index=index )
# set a breakpoint to inspect
# import pdb
# pdb.set_trace()
question = "what is a programming language?"
nodes = retriever.retrieve(question)
print(nodes)
print("len of nodes :", len(nodes))

# configure response synthesizer
response_synthesizer = ResponseSynthesizer.from_args(
    node_postprocessors=[
        SimilarityPostprocessor(similarity_cutoff=0.7)
    ]
)

# assemble query engine
query_engine = RetrieverQueryEngine(
    retriever=retriever,
    response_synthesizer=response_synthesizer,
)

response = query_engine.query(question)
print(response)
print("len of response nodes :", len(response.source_nodes)) #nodes
print("Done!")