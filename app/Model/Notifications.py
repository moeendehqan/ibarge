from mongoengine import Document, StringField, IntField, ListField, DateTimeField, ObjectIdField, BooleanField
from bson import ObjectId

#  است و برای ورود کاربر است NAME , MOBILE این ماژول بر اساس 

class Notifications(Document):
    _id = ObjectIdField()
    mobile = StringField()
    title = StringField()
    description = StringField()
    avatar = StringField()
    type = StringField()
    createAt = DateTimeField()
    isUnRead = BooleanField()

    @classmethod
    def get_last_five_by_phone(cls, mobile_number):
        notif = cls.objects(mobile=mobile_number).order_by('-createAt')[:5]
        lst = []
        for n in notif:
            dict = {
                '_id': str(n._id),
                'mobile': n.mobile,
                'title': n.title,
                'description': n.description,
                'avatar': n.avatar,
                'type': n.type,
                'createAt': str(n.createAt),
                'isUnRead': n.isUnRead
            }
            lst.append(dict)
        return lst
    
    @classmethod
    def get_by_phone(cls, mobile_number):
        notif = cls.objects(mobile=mobile_number)
        lst = []
        for n in notif:

            dict = {
                '_id': str(n._id),
                'mobile': n.mobile,
                'title': n.title,
                'description': n.description,
                'avatar': n.avatar,
                'type': n.type,
                'createAt': str(n.createAt),
                'isUnRead': n.isUnRead
            }
            lst.append(dict)
        return lst
    
    @classmethod
    def mark_as_read_by_phone(cls, mobile_number):
        notif = cls.objects(mobile=mobile_number)
        for n in notif:
            n.isUnRead = False
            n.save()