from flask_restful import Resource ,reqparse , abort
from app.Model.Companies import ModelCompanies
from bson import ObjectId

parser = reqparse.RequestParser ()
parser.add_argument ('_id' , type = str , help = 'آیدی را وارد کنید' , required = True) 


class GetCompanies (Resource) : 
    def post (self) :
        args = parser.parse_args ()
        data = ModelCompanies.objects (_id = args ['_id'])
        data_list = []
        for i in data :
             data_list.append({
                '_id': str (i._id),
                'NameOfCompany': i.NameOfCompany,
                'NationalId': i.NationalId,
                'TaxMemoryId': i.TaxMemoryId,
                'Key': i.Key,
                'Address': i.Address,
                'Telephone': i.Telephone,
            
            })
    
        return {'companies':data_list}
    

