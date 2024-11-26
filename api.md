# Search

Types:

```python
from justement.types import SearchResultSnippets
```

Methods:

- <code title="get /api/search">client.search.<a href="./src/justement/resources/search.py">execute</a>(\*\*<a href="src/justement/types/search_execute_params.py">params</a>) -> <a href="./src/justement/types/search_result_snippets.py">SearchResultSnippets</a></code>

# Count

Types:

```python
from justement.types import CountExecuteResponse
```

Methods:

- <code title="get /api/count">client.count.<a href="./src/justement/resources/count.py">execute</a>(\*\*<a href="src/justement/types/count_execute_params.py">params</a>) -> <a href="./src/justement/types/count_execute_response.py">CountExecuteResponse</a></code>

# Documents

Types:

```python
from justement.types import Document
```

Methods:

- <code title="get /api/document">client.documents.<a href="./src/justement/resources/documents.py">retrieve</a>(\*\*<a href="src/justement/types/document_retrieve_params.py">params</a>) -> <a href="./src/justement/types/document.py">Document</a></code>
- <code title="get /api/documentByRef">client.documents.<a href="./src/justement/resources/documents.py">reference_retrieve</a>(\*\*<a href="src/justement/types/document_reference_retrieve_params.py">params</a>) -> <a href="./src/justement/types/document.py">Document</a></code>
