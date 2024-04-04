from flask_restful import Resource , reqparse , abort
from app.Model.CreateInvoce import ModelCreateInvoce
import datetime

parser = reqparse.RequestParser ()
parser.add_argument ('_id', type =str , help ='آیدی را وارد کنید ', required = True)



class DeleteCreateInvoce (Resource) :
            
    def post (self) :
        args = parser.parse_args ()
        data = ModelCreateInvoce.objects (_id = args ['_id']).first ()

        if data :
            ModelCreateInvoce.objects (_id = args ['_id']).delete ()

        return True
    
    