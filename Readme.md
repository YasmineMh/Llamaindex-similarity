# Testing some functionalities of [Llamaindex](https://github.com/jerryjliu/llama_index)

## Using Weaviate

- Run weaviate docker imagae

- Install poetry then do:
```
poetry install
poetry shell
```

- Export OpenAI key
```
export OPENAI_API_KEY=""
```

## Using Weaviate

### Run with_similarity_cutoff.py script

```
poetry run python WeaviateVectorStore/with_similarity_cutoff.py
```

### Output

```
#print(nodes)
[NodeWithScore(node=Node(text='A programming language is a system of notation for writing computer programs.[1] Most programming languages are text-based formal languages, but they may also be graphical. They are a kind of computer language.\n\nThe description of a programming language is usually split into the two components of syntax (form) and semantics (meaning), which are usually defined by a formal language. Some languages are defined by a specification document (for example, the C programming language is specified by an ISO Standard) while other languages (such as Perl) have a dominant implementation that is treated as a reference. Some languages have both, with the basic language defined by a standard and extensions taken from the dominant implementation being common.\n\nProgramming language theory is the subfield of computer science that studies the design, implementation, analysis, characterization, and classification of programming languages.\n', doc_id='ef0dc9a6-6c27-45aa-8333-7280c06968c3', embedding=None, doc_hash='ed8ce016d28e15f274702f07fc7d017cd4f8722a813c33c2e02c609941bad23c', extra_info={}, node_info={'start': 0, 'end': 933, '_node_type': '1'}, relationships={<DocumentRelationship.SOURCE: '1'>: '4f28b113-e1ab-4b3b-a26b-fc0922511575'}), score=None), NodeWithScore(node=Node(text='A programming language is a system of notation for writing computer programs.[1] Most programming languages are text-based formal languages, but they may also be graphical. They are a kind of computer language.\n\nThe description of a programming language is usually split into the two components of syntax (form) and semantics (meaning), which are usually defined by a formal language. Some languages are defined by a specification document (for example, the C programming language is specified by an ISO Standard) while other languages (such as Perl) have a dominant implementation that is treated as a reference. Some languages have both, with the basic language defined by a standard and extensions taken from the dominant implementation being common.\n\nProgramming language theory is the subfield of computer science that studies the design, implementation, analysis, characterization, and classification of programming languages.\n', doc_id='d2822624-a52e-45ae-8efe-2b6fb4bbbc24', embedding=None, doc_hash='ed8ce016d28e15f274702f07fc7d017cd4f8722a813c33c2e02c609941bad23c', extra_info={}, node_info={'start': 0, 'end': 933, '_node_type': '1'}, relationships={<DocumentRelationship.SOURCE: '1'>: 'acb6b0ce-af70-4f6f-b3a5-57170e4451ce'}), score=None)]

# print(response)
None
# print(len(response.source_nodes))
0
Done!
```

### Error1:
embedding=None

### Error2:
Similarity didn't work / score=None


### Run without_similarity_cutoff.py script

```
poetry run python WeaviateVectorStore/without_similarity_cutoff.py
```

### Output

```
#print(nodes)
[NodeWithScore(node=Node(text='A programming language is a system of notation for writing computer programs.[1] Most programming languages are text-based formal languages, but they may also be graphical. They are a kind of computer language.\n\nThe description of a programming language is usually split into the two components of syntax (form) and semantics (meaning), which are usually defined by a formal language. Some languages are defined by a specification document (for example, the C programming language is specified by an ISO Standard) while other languages (such as Perl) have a dominant implementation that is treated as a reference. Some languages have both, with the basic language defined by a standard and extensions taken from the dominant implementation being common.\n\nProgramming language theory is the subfield of computer science that studies the design, implementation, analysis, characterization, and classification of programming languages.\n', doc_id='9dc356e8-7120-4ecf-9299-ac1bde6ff859', embedding=None, doc_hash='ed8ce016d28e15f274702f07fc7d017cd4f8722a813c33c2e02c609941bad23c', extra_info={}, node_info={'start': 0, 'end': 933, '_node_type': '1'}, relationships={<DocumentRelationship.SOURCE: '1'>: 'fbdab0fe-4af3-4352-92a0-8b0c033755df'}), score=None), NodeWithScore(node=Node(text='A programming language is a system of notation for writing computer programs.[1] Most programming languages are text-based formal languages, but they may also be graphical. They are a kind of computer language.\n\nThe description of a programming language is usually split into the two components of syntax (form) and semantics (meaning), which are usually defined by a formal language. Some languages are defined by a specification document (for example, the C programming language is specified by an ISO Standard) while other languages (such as Perl) have a dominant implementation that is treated as a reference. Some languages have both, with the basic language defined by a standard and extensions taken from the dominant implementation being common.\n\nProgramming language theory is the subfield of computer science that studies the design, implementation, analysis, characterization, and classification of programming languages.\n', doc_id='d2822624-a52e-45ae-8efe-2b6fb4bbbc24', embedding=None, doc_hash='ed8ce016d28e15f274702f07fc7d017cd4f8722a813c33c2e02c609941bad23c', extra_info={}, node_info={'start': 0, 'end': 933, '_node_type': '1'}, relationships={<DocumentRelationship.SOURCE: '1'>: 'acb6b0ce-af70-4f6f-b3a5-57170e4451ce'}), score=None)]

# print(response)
A programming language is a system of notation used to write computer programs. It is usually text-based, but can also be graphical. It is defined by a formal language, which is split into two components: syntax (form) and semantics (meaning). Some languages are defined by a specification document, while others have a dominant implementation that is treated as a reference. Programming language theory is the subfield of computer science that studies the design, implementation, analysis, characterization, and classification of programming languages.

# print(len(response.source_nodes))
2
Done!
```

### Error1:
embedding=None

### Error2:
score=None



## Using Default local index

### Run with_similarity_cutoff.py script

```
poetry run python VectorStoreIndex/with_similarity_cutoff.py
```

### Output

```
#print(nodes)
[NodeWithScore(node=Node(text='A programming language is a system of notation for writing computer programs.[1] Most programming languages are text-based formal languages, but they may also be graphical. They are a kind of computer language.\n\nThe description of a programming language is usually split into the two components of syntax (form) and semantics (meaning), which are usually defined by a formal language. Some languages are defined by a specification document (for example, the C programming language is specified by an ISO Standard) while other languages (such as Perl) have a dominant implementation that is treated as a reference. Some languages have both, with the basic language defined by a standard and extensions taken from the dominant implementation being common.\n\nProgramming language theory is the subfield of computer science that studies the design, implementation, analysis, characterization, and classification of programming languages.\n', doc_id='625b008a-840e-46a2-b800-a7b56c863de1', embedding=None, doc_hash='a063007b2f680eb99a1117c60fd87b7620966ac84a1ea2a88ebfaee8ae287dd8', extra_info=None, node_info={'start': 0, 'end': 933, '_node_type': <NodeType.TEXT: '1'>}, relationships={<DocumentRelationship.SOURCE: '1'>: 'd6d6f178-b5e9-45ba-b6f7-18bb5d33468d'}), score=0.8882626537130287), NodeWithScore(node=Node(text='A psychologist/detective finds themselves ensnared in an intricate web of cascading dreams, each layer more elusive and surreal than the last. The concept of delving into the depths of the subconscious mind, unraveling secrets and solving mysteries within dreams, was ingeniously explored in the film "Inception." Drawing inspiration from this visionary masterpiece, our psychologist/detective embarks on a mind-bending journey where the boundaries of reality blur and the very fabric of their own existence hangs in the balance. With each successive dream within a dream, the stakes intensify, challenging their sanity and forcing them to confront their deepest fears, unresolved traumas, and the enigmatic clues hidden within this labyrinthine realm. In this nightmarish odyssey, where the line between the conscious and the subconscious dissolves, our intrepid protagonist must navigate the intricate layers of their own psyche to uncover the truth that lies buried deep within the recesses of their mind.\n', doc_id='2cdf0510-84bc-4ea9-bc88-feebe25a7670', embedding=None, doc_hash='639a9e2792bcaff0b2c3e389278b2879fd408d2a4720ef352822969d2ff0c508', extra_info=None, node_info={'start': 0, 'end': 1009, '_node_type': <NodeType.TEXT: '1'>}, relationships={<DocumentRelationship.SOURCE: '1'>: '35977c45-8b0b-493f-b2d8-018cea3bde09'}), score=0.7289089733281329)]

# print(response)
A programming language is a system of notation for writing computer programs. It is a kind of computer language that is usually text-based or graphical, and is defined by a formal language. It is split into two components: syntax (form) and semantics (meaning). Programming language theory is the subfield of computer science that studies the design, implementation, analysis, characterization, and classification of programming languages.

# print(len(response.source_nodes))
2
Done!
```

### Error:
embedding=None
