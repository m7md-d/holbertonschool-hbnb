from app.persistence.repository import InMemoryRepository
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.user import User
from app.models.review import Review


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user
    def get_all_users(self):
        return self.user_repo.get_all()
    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)



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
            owner_id = place_data.pop('owner_id', None)
            owner_obj = self.user_repo.get(owner_id)
            if not owner_obj:
                return False, "Owner not found. A valid User instance is required."
            place_data['owner'] = owner_obj
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


    # review methods
    def create_review(self, review_data):
        try:
            review = Review(**review_data)
        except (ValueError, TypeError):
            return False
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        return self.review_repo.get_by_attribute('place_id', place_id)

    def update_review(self, review_id, review_data):
        return self.review_repo.update(review_id, review_data)

    def delete_review(self, review_id):
        self.review_repo.delete(review_id)
