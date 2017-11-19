import falcon
import json
from sample.error.sample_error import SampleError
from sample.error.code import ErrorCode

def parseJson(req, resp, resource, params):
    body = req.stream.read().decode('utf-8')
    try:
        req.body = json.loads(body)
    except Exception as err:
        raise SampleError(status=falcon.HTTP_400, code=ErrorCode.INVALID_JSON, exception=err, vars={ "body": body })