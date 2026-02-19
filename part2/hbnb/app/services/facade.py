from app.persistence.repository import InMemoryRepository
from app.models.amenity import Amenity
from app.models.place import Place

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        # Logic will be implemented in later tasks
        pass



    # Amenity Methods
    def create_amenity(self, amenity_data):
        try:
            amenity = Amenity(**amenity_data)
            self.amenity_repo.add(amenity)
            return True, amenity
        except ValueError as e:
            return False, str(e)


    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def get_amenity_by_name(self, amenity_name):
        return self.amenity_repo.get_by_attribute('name', amenity_name)

    def update_amenity(self, amenity_id, amenity_data):
         try:
            check_amenity = self.amenity_repo.get(amenity_id)
            if not check_amenity:
                return False, 'Amenity Not Found'
   
            amenity = self.amenity_repo.update(amenity_id, amenity_data)
            return True, None
         except (ValueError, TypeError) as e:
            return False, str(e)
    
    # Place Methods
    def create_place(self, place_data):
        try:
            place = Place(**place_data)
            self.place_repo.add(place)
            return True, place
        except (TypeError, ValueError) as e:
            return False, str(e)

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        try:
            check_place = self.place_repo.get(place_id)
            if not check_place:
                return False, 'Place Not Found'
             
             place = self.place_repo.update(place_id, place_data)
             return True, None
        except (ValueError, TypeError) as e:
            return False, str(e)

