from mongoengine import Document, StringField, IntField, ListField, DateTimeField, ObjectIdField, BooleanField
from bson import ObjectId

#  است و برای ورود کاربر است NAME , MOBILE این ماژول بر اساس 

class OTP(Document):
    _id = ObjectIdField()
    mobile = StringField()
    code = StringField()
    createAt = DateTimeField()

    @classmethod
    def get_last_otp(cls, mobile_number):
        last_otp = cls.objects(mobile=mobile_number).order_by('-createAt').first()
        return last_otp['code']
    
    def __repr__(self):
        return f'UserAdmin({self.mobile}, {self.code}, {self.createAt})'
    