from flask_restful import Resource , reqparse 
from app.Model.Companies import ModelCompanies
import datetime


parser = reqparse.RequestParser()
parser.add_argument ('_id' , type = str , help = 'آیدی کاربر را وارد کنید' , required = True) 
parser.add_argument ('NameOfCompany' , type = str , help = 'نام شخصیت حقیقی یا حقوقی را وارد کنید' , required = True) 
parser.add_argument ('NationalId' , type = str , help = 'شناسه ملی یا شناسه اقتصادی را وارد کنید' , required = True) 
parser.add_argument ('TaxMemoryId' , type = str , help = 'شناسه حافظه مالیاتی را وارد کنید' , required = True) 
parser.add_argument ('Key' , type = str , help = 'کلید خصوصی را وارد کنید' , required = True) 
parser.add_argument ('Address' , type = str , help = 'آدرس را وارد کنید' , required = False) 
parser.add_argument ('Telephone' , type = str , help = 'تلفن را وارد کنید' , required = False) 


class SetCompanies (Resource) : 
    def post (self) :
        args = parser.parse_args ()
        data = ModelCompanies.objects (_id =args ['_id'] , NationalId = args['NationalId']).first()
        if data :
            ModelCompanies.objects (_id =args ['_id'] , NationalId = args['NationalId']).delete()
        Company = ModelCompanies (
            _id = args['_id'],
            NameOfCompany = args['NameOfCompany'],
            NationalId = args['NationalId'],
            TaxMemoryId = args['TaxMemoryId'],
            Key = args['Key'],
            Address = args['Address'],
            Telephone = args['Telephone'],
            CreateAt = datetime.datetime.now ()
        )
        Company.save ()
        return True