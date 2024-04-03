from mongoengine import Document, StringField, IntField, ListField, DateTimeField, ObjectIdField, BooleanField
from bson import ObjectId

#  است و برای ورود کاربر است NAME , MOBILE این ماژول بر اساس 

class User(Document):
    _id = ObjectIdField()
    mobile = StringField()
    name = StringField()
    createAt = DateTimeField()
    expier = DateTimeField()
    avatar = StringField()
    limit = IntField()

    @classmethod
    def get_user_one_by_phone(cls, mobile_number):
        user_one = cls.objects(mobile=mobile_number).first()
        if user_one:
            user_dict = {
                '_id': str(user_one._id),
                'mobile': user_one.mobile,
                'name': user_one.name,
                'createAt': user_one.createAt,
                'expier': user_one.expier,
                'avatar':user_one.avatar
            }
            return user_dict
        else:
            return None
    @classmethod
    def get_user_one_by_id(cls, id):
        user_one = cls.objects(_id=ObjectId(id)).first()
        if user_one:
            user_dict = {
                'id': str(user_one._id),
                'mobile': user_one.mobile,
                'name': user_one.name,
                'createAt': user_one.createAt,
                'expier': user_one.expier,
                'avatar':user_one.avatar
            }
            return user_dict
        else:
            return None
    
    def __repr__(self):
        return f'UserAdmin({self.name}, {self.mobile}, {self.mobile}, {self.createAt}, {self.expier})'
    