import pydantic

class RAGChunkAndSrc(pydantic.BaseModel):
    chunk: list[str]
    source_id: str=None

class RAGUpsertResult(pydantic.BaseModel):
    ingested: int 

class RAGSearchResult(pydantic.BaseModel):
    contexts: list[str]
    sourceS: list[str]

class RAQQueryResult(pydantic.BaseModel):
    answer: str
    sources: list[str]
    num_contexts: int