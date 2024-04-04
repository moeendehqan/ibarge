from mongoengine import Document , ObjectIdField, StringField , IntField , DateTimeField
from bson import ObjectId



class ModelCompanies (Document)  : 
    _id = ObjectIdField ()
    NameOfCompany = StringField ()
    NationalId = StringField ()
    TaxMemoryId = StringField ()
    Key = StringField ()
    Address = StringField ()
    Telephone = StringField ()
    CreateAt = DateTimeField()


    def __repr__(self):
        return f'ModelCompanies({self._id},{self.NationalId})'
