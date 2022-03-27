from rest_framework.response import Response


class HttpCode(object):
    success = 1000
    servererror = 4000
    parametererror = 4001
    authenticate = 2001
    nobundle = 2004
    hasbundle = 2005
    banauth = 401
    timeoutauth = 4002


def result(code=HttpCode.success, message="", data=None, kwargs=None):
    json_dict = {"code": code, "msg": message, "data": data}
    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        json_dict.update(kwargs)
    return Response(json_dict)


def CODE_SUCCESS(message="", data=None):
    return result(code=HttpCode.success, message=message, data=data)


def SERVER_ERROR(message="", data=None):
    return result(code=HttpCode.servererror, message=message, data=data)


def PARAMETER_ERROR():
    return result(code=HttpCode.servererror, message='缺少参数')


def UNAUTHORIZED_ERROR(message='认证失败:用户名或密码错误'):
    return result(code=HttpCode.authenticate, message=message)


def NOBUNDLE_ERROR(data=None):
    return result(code=HttpCode.nobundle, message='该账户尚未绑定设备', data=data)


def HASBUNDLE_ERROR():
    return result(code=HttpCode.hasbundle, message='该账户已绑定其他设备，登陆失败')


def BAN_ERROR(data=None):
    return result(code=HttpCode.banauth, message='您的账户已被禁用，禁止登陆', data=data)


def NO_OPEN_CITY_ERROR(data=None):
    return result(code=HttpCode.timeoutauth, message='您的账户暂未开通城市', data=data)


def TIME_OUT_ERROR(data=None):
    return result(code=HttpCode.timeoutauth, message='您的账户已过期，如有疑问请咨询管理员', data=data)


def NO_TRY_OUT_ERROR(data=None):
    return result(code=HttpCode.banauth, message='您的账户暂无试用权限，如有疑问请咨询管理员', data=data)


def VER_ERROR(message, data=None):
    return result(code=HttpCode.servererror, message=message, data=data)
