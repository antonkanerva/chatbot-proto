# Chatbot Proto

Shared Protocol Buffer definitions for the chatbot project's gRPC services.

## Installation

```bash
pdm add chatbot-proto
```

## Development Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd chatbot-proto
```

2. Install PDM if you haven't already:
```bash
pip install pdm
```

3. Install dependencies:
```bash
pdm install
```

4. Install pre-commit hooks:
```bash
pdm run prepare
```

5. Generate proto files:
```bash
pdm run generate
```

## Usage

```python
from chatbot_proto import SearchRequest, SearchResponse, SearchHit
from chatbot_proto import ChatbotSearchServiceStub, ChatbotSearchServiceServicer

# For implementing the server
class SearchService(ChatbotSearchServiceServicer):
    async def Search(
        self, 
        request: SearchRequest, 
        context
    ) -> SearchResponse:
        # Implementation here
        pass

# For client usage
async with grpc.aio.insecure_channel('localhost:50051') as channel:
    stub = ChatbotSearchServiceStub(channel)
    response = await stub.Search(SearchRequest(
        query="search query",
        top_k=5
    ))
```