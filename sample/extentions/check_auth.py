import jwt
from sample.error.sample_error import SampleError
from sample.error.code import ErrorCode

SECRET = b'SUPER_SECRET'

def check_auth(req, resp, resource, params):
    token = req.headers.get('token')
    decoded = jwt.decode(token.encode("utf-8") , SECRET, algorithms=['HS256']) if token else None
    if decoded and decoded.application_id:
        req.context['application_id'] = decoded.application_id
        req.context['admin'] = decoded.admin
    else:
      raise SampleError(error_code=ErrorCode.UNAUTHORIZED, extra_vars={'token': token})
