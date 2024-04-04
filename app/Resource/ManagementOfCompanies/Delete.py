from flask_restful import Resource , reqparse , abort
from app.Model.Companies import ModelCompanies
import datetime

parser = reqparse.RequestParser ()
parser.add_argument ('_id', type =str , help ='آیدی را وارد کنید ', required = True)
parser.add_argument ('NationalId', type = str , help = 'شناسه ملی وارد کنید ' , required = True)



class DeleteCompanies (Resource) :
            
    def post (self) :
        args = parser.parse_args ()
        data = ModelCompanies.objects (_id = args ['_id'],NationalId = args ['NationalId'] ).first ()

        if data :
            ModelCompanies.objects (_id = args ['_id'],NationalId = args ['NationalId'] ).delete ()

        return True
    
    