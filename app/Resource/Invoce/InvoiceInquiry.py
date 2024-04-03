from flask_restful import Resource , reqparse 
from moadian import Moadian



parser = reqparse.RequestParser()

parser.add_argument ('referenceNumber', type = str , help = 'شناسه را وارد کنید ' , required = True)
parser.add_argument ('MemoryId', type = str , help = 'ایدی  را وارد کنید ' , required = True)
parser.add_argument ('key', type = str , help = 'کلید  را وارد کنید ' , required = True)

class InvoiceInquiry (Resource) : 
    def post (self) :
        args = parser.parse_args ()        
        moadian = Moadian (args ['MemoryId'], args ["key"])
        inquiry = moadian.inquiry_by_reference_number('referenceNumber')
        return inquiry 




