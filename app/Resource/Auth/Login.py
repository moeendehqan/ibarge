from flask_restful import Resource, reqparse, abort
from app.Model.OTP import OTP
from app.Model.Users import User
import datetime
from ast  import literal_eval
from app.Service.config import expier_new_user
from persiantools.jdatetime import JalaliDate
from app.Model.Notifications import Notifications
from app.Service.AvatarCreatoe import AvatarCreator
parser = reqparse.RequestParser()
parser.add_argument('phone', type=str, help='شماره همراه را وارد کنید',required=True)
parser.add_argument('otp', type=str, help='کد تایید',required=True)

class Login(Resource):

    def post(self):
        args = parser.parse_args()
        try:
            last_otp = OTP.get_last_otp(args['phone'])
        except:
            abort(400, message={'otp':'کد تایید صحیح نیست'})
        if str(last_otp) != str(args['otp']):
            abort(400, message={'otp':'کد تایید صحیح نیست'})

        user_one = User.get_user_one_by_phone(args['phone'])
        if user_one == None:
            createAt=datetime.datetime.now()
            expier = createAt + datetime.timedelta(days=expier_new_user)
            user_new = User(mobile=args['phone'], name='', createAt=createAt, expier=expier, avatar=AvatarCreator(), limit=1)
            user_new.save()
            notif_new_user = Notifications(mobile=args['phone'],title='اشتراک هدیه',description=f'برای ثبت نام شما {expier_new_user} روز اشتراک هدیه برای شما لحاظ شد',avatar='assets/icons/glass/gift.png',type=None,createAt=datetime.datetime.now(),isUnRead=True)
            notif_new_user.save()
            user_one = User.get_user_one_by_phone(args['phone'])
        
        try:
            user_one['credit'] = (user_one['expier'] - datetime.datetime.now()).days
        except:
            user_one['credit'] = 0

        user_one['expier'] = str(JalaliDate(user_one['expier']))
        user_one['createAt'] = str(JalaliDate(user_one['createAt']))
        return user_one,200
    


    