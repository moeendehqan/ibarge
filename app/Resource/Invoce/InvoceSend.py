from flask_restful import Resource , reqparse 
from moadian import Moadian


parser = reqparse.RequestParser()
parser.add_argument ('MemoryId', type = str , help = 'ایدی  را وارد کنید ' , required = True)
parser.add_argument ('key', type = str , help = 'کلید  را وارد کنید ' , required = True)
parser.add_argument ('invoice', type=dict, action='append', help = 'فاکتور را وارد کنید ' , required = True)


class InvoceSend (Resource) : 
    def post (self) :
        args = parser.parse_args ()
        moadian = Moadian (args ['MemoryId'], args ["key"])
        result = moadian.send_invoice(args ['invoice'][0])
        return result 
    