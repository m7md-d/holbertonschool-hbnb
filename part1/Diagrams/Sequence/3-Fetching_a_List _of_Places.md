```mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: Request List of Places
API->>BusinessLogic: Request Data Retrieval
BusinessLogic->>Database: Query All Places
Database-->>BusinessLogic: Return Place Records
BusinessLogic-->>API: Return List[Place]
API-->>User: Return JSON Response (200 OK)
```
