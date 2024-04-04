from flask_restful import Resource , reqparse 
from app.Model.CreateInvoce import ModelCreateInvoce
import datetime


parser = reqparse.RequestParser()
parser.add_argument ('_id' , type = str , help = 'نام شخصیت حقیقی یا حقوقی را وارد کنید' , required = True) 
parser.add_argument ('Title' , type = str , help = 'عنوان صورتحساب را وارد کنید' , required = True) 
parser.add_argument ('SellerId' , type = str , help = 'اطلاعات فروشنده را وارد کنید' , required = True) 
parser.add_argument ('BuyerNatiobalId' , type = str , help = 'شناسه خریدار را وارد کنید' , required = True) 
parser.add_argument ('CreatDate' , type = int , help = 'تاریخ ایجاد صورتحساب را وارد کنید' , required = True) 
parser.add_argument ('IssuingDate' , type = int , help = 'تاریخ صدور صورتحساب را وارد کنید' , required = True) 
parser.add_argument ('TypeOfInvoce' , type = int , help = 'نوع صورتحساب را وارد کنید' , required = True , choices=list(range(1, 23))) 
parser.add_argument ('SalesModel' , type = int , help = 'الگو فروش را وارد کنید' , required = True , choices=list(range(1, 6))) 
parser.add_argument ('TypeOfBuyer' , type = int , help = 'نوع خریدار را وارد کنید' , required = True ,choices=list(range(1, 5))) 
parser.add_argument ('Body', type=dict, action='append', help = 'بدنه را وارد کنید ' , required = True)


class SetCreateInvoce (Resource) : 
    def post (self) :
        args = parser.parse_args ()
        Create = ModelCreateInvoce (
            _id = args['_id'],
            Title = args['Title'],
            SellerId = args['SellerId'],
            BuyerNatiobalId = args['BuyerNatiobalId'],
            CreatDate = args['CreatDate'],
            IssuingDate = args['IssuingDate'],
            TypeOfInvoce = args['TypeOfInvoce'],
            SalesModel = args['SalesModel'],
            TypeOfBuyer = args['TypeOfBuyer'],
            Body = args['Body'],
            CreateAt = datetime.datetime.now ()
        )
        Create.save ()
        return True