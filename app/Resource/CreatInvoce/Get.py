from flask_restful import Resource ,reqparse , abort
from app.Model.CreateInvoce import ModelCreateInvoce
from bson import ObjectId

parser = reqparse.RequestParser ()
parser.add_argument ('_id' , type = str , help = 'آیدی را وارد کنید' , required = True) 


class GetCreateInvoce (Resource) : 
    def post (self) :
        args = parser.parse_args ()
        data = ModelCreateInvoce.objects (_id = args ['_id'])
        if not data:
            abort(404, message="موردی با این _id یافت نشد")
        data_list = []
        for i in data :
             data_list.append({
                '_id': str (i._id),
                'Title': i.Title,
                'SellerId': i.SellerId,
                'BuyerNatiobalId': i.BuyerNatiobalId,
                'CreatDate': i.CreatDate,
                'IssuingDate': i.IssuingDate,
                'TypeOfInvoce': i.TypeOfInvoce,
                'SalesModel': i.SalesModel,
                'TypeOfBuyer': i.TypeOfBuyer,
                'Body': i.Body
            
            })
            
        return {'Create':data_list}
    

