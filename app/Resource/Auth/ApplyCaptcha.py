from flask_restful import Resource, reqparse, abort
from GuardPyCaptcha.Captch import GuardPyCaptcha
from app.Model.OTP import OTP
import random
import datetime
from ast  import literal_eval


parser = reqparse.RequestParser()
parser.add_argument('phone', type=str, help='شماره همراه را وارد کنید',required=True)
parser.add_argument('input_captcha', type=str, help='کد کپچا را وارد کنید',required=True)
parser.add_argument('encrypted_response', type=str, help=' خطا در دریافت اطلاعات کپچا',required=True)

class ApplyCaptcha(Resource):
    
    """
    تایید شماره موبایل : در صورت تایید کاربر بر اساس شماره موبایل 
    عکس کپچا ارسال میکند
    در صورت تایید کد کپچا  کد به شماره موبایل کاربر ارسال میکند

    """
    def post(self):
        args = parser.parse_args()
        Captcha = GuardPyCaptcha()
        try:
            encrypted_response = literal_eval(args['encrypted_response'])['encrypted_response']
            Captcha = Captcha.check_response(encrypted_response,args['input_captcha'])
        except:
            abort(400, message={'input_captcha':'کد کپچا صحیح نیست'})
        if Captcha == False:
            abort(400, message={'input_captcha':'کد کپچا صحیح نیست'})
        code = str(random.randint(1000,9999))
        print(args['phone'],code)
        new_otp = OTP(mobile=args['phone'], code=code, createAt=datetime.datetime.now())
        new_otp.save()
        text = f'کد تایید: {code}\nبرگه\nibarge.work'
        print(text)
        return True,200
    


    