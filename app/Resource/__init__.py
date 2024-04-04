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
from .ManagementOfCompanies.Set import SetCompanies
from .ManagementOfCompanies.Get import GetCompanies
from .ManagementOfCompanies.Delete import DeleteCompanies
from .CreatInvoce.Set import SetCreateInvoce
from .CreatInvoce.Get import GetCreateInvoce
from .CreatInvoce.Delete import DeleteCreateInvoce

api = Api()

api.add_resource (InvoceSend,'/invoice/send') 
api.add_resource (InvoiceInquiry,'/invoice/inquiry')
api.add_resource (CaptchaGenerate,'/auth/captcha')
api.add_resource (ApplyCaptcha,'/auth/applycaptcha')
api.add_resource (Login,'/auth/login')
api.add_resource (Uid,'/auth/uid')
api.add_resource (GetLastNotifUser,'/notifivation/getlastuser')
api.add_resource (MarkAllRead,'/notifivation/markallread')
api.add_resource (SetCompanies,'/companies/set')
api.add_resource (GetCompanies,'/companies/get')
api.add_resource (DeleteCompanies,'/companies/delete')
api.add_resource (SetCreateInvoce,'/Create/set')
api.add_resource (GetCreateInvoce,'/Create/get')
api.add_resource (DeleteCreateInvoce,'/Create/delete')
