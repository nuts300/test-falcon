import jwt
from sample.error.sample_error import SampleError
from sample.error.code import ErrorCode
from bson.json_util import dumps

SECRET = 'SUPER_SECRET'

def check_auth(req, resp, resource, params):
    token = req.headers['TOKEN']
    if not token:
        raise SampleError(error_code=ErrorCode.UNAUTHORIZED, extra_vars={'token': token})
    try:
        decoded = jwt.decode(token, SECRET, algorithms=['HS256'])
        req.context['application_id'] = decoded['application_id']
        req.context['admin'] = decoded['admin']
    except:
        raise SampleError(error_code=ErrorCode.UNAUTHORIZED, extra_vars={'token': token})
