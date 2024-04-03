from flask_restful import Resource, reqparse, abort
from app.Model.OTP import OTP
from app.Model.Users import User
import datetime
from ast  import literal_eval
from app.Service.config import expier_new_user
from persiantools.jdatetime import JalaliDate

parser = reqparse.RequestParser()
parser.add_argument('uid', type=str, help='شماره همراه را وارد کنید',required=True)

class Uid(Resource):

    def post(self):
        args = parser.parse_args()
        user_one = User.get_user_one_by_id(args['uid'])
        if user_one == None:
            abort(400, message={'uid':'notfind'})

        try:
            user_one['credit'] = (user_one['expier'] - datetime.datetime.now()).days
        except:
            user_one['credit'] = 0

        user_one['expier'] = str(JalaliDate(user_one['expier']))
        user_one['createAt'] = str(JalaliDate(user_one['createAt']))
        return user_one,200
    


    