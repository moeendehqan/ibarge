from flask_restful import Resource, reqparse
from GuardPyCaptcha.Captch import GuardPyCaptcha


class CaptchaGenerate(Resource):
    
    """
    این تابع تصویر کپچا که شامل کد 4 رقمی به عنوان کد کپچا هست نشان میدهد

    """
    def get(self):
        Captcha = GuardPyCaptcha()
        Captcha = Captcha.Captcha_generation(num_char=4,only_num=True)
        return Captcha,200

    
