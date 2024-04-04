from mongoengine import Document , ObjectIdField, StringField , IntField , DateTimeField,ListField
from bson import ObjectId



class ModelCreateInvoce (Document)  : 
    _id = ObjectIdField ()
    Title = StringField ()
    SellerId = StringField ()
    BuyerNatiobalId = StringField ()
    CreatDate = IntField ()
    IssuingDate = IntField ()
    TypeOfInvoce = IntField ()
    SalesModel = IntField ()
    TypeOfBuyer = IntField ()
    Body = ListField ()
    CreateAt = DateTimeField()


    def __repr__(self):
        return f'ModelCompanies({self.Title},{self.SellerId})'
