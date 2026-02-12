```mermaid
classDiagram
    class PresentationLayer {
        +API Endpoints
        +Services
        API Endpoints
        Services
    }
    class BusinessLogicLayer {
        +User
        +Place
        +Amenity
        +Review
        User
        Place
        Amenity
        Review
    }
    class PersistenceLayer {
        +Repository
        +Database
        +Storage
        Repository
        Database
        Storage
    }

    PresentationLayer --> BusinessLogicLayer : Facade Pattern
