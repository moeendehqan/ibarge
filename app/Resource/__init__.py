from flask_restful import Api
from .Invoce.InvoceSend import InvoceSend
from .Invoce.InvoiceInquiry import InvoiceInquiry
from .Auth.Captcha import CaptchaGenerate
from .Auth.ApplyCaptcha import ApplyCaptcha
from .Auth.Login import Login
from .Auth.Uid import Uid
from .Notifivation.GetAllNotifUser import GetAllNotifUser
from .Notifivation.MarkAllRead import MarkAllRead
from .Notifivation.GetLastNotifUser import GetLastNotifUser

api = Api()

api.add_resource (InvoceSend,'/invoice/send') 
api.add_resource (InvoiceInquiry,'/invoice/inquiry')
api.add_resource (CaptchaGenerate,'/auth/captcha')
api.add_resource (ApplyCaptcha,'/auth/applycaptcha')
api.add_resource (Login,'/auth/login')
api.add_resource (Uid,'/auth/uid')
api.add_resource (GetLastNotifUser,'/notifivation/getlastuser')
api.add_resource (MarkAllRead,'/notifivation/markallread')
