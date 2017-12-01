import jwt
from sample.error.sample_error import SampleError
from sample.error.code import ErrorCode

SECRET = 'SUPER_SECRET'

def check_auth(req, resp, resource, params):
    token = req.headers.get('token')
    decoded = jwt.decode(token, SECRET, algorithms=['HS256'])
    if decoded.application_id:
        req.context.application_id = decoded.application_id
        req.context.admin = decoded.admin
    else:
      raise SampleError(error_code=ErrorCode.UNAUTHORIZED, extra_vars={'token': token})
