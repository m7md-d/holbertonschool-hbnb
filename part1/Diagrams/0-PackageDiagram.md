classDiagram
    class PresentationLayer {
        +API_Endpoints
        +Services
    }
    class BusinessLogicLayer {
        +User
        +Place
        +Amenity
        +Review
    }
    class PersistenceLayer {
        +Repository
        +Database
        +Storage
    }

    PresentationLayer --> BusinessLogicLayer : Facade_Pattern
    BusinessLogicLayer --> PersistenceLayer : Database_Operations