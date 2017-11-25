import json
import falcon
from sample.error.sample_error import SampleError
from sample.error.code import ErrorCode

def parse_json(req, resp, resource, params):
    try:
        body = req.stream.read().decode('utf-8')
        req.context = {"body": json.loads(body)}
    except Exception:
        raise SampleError(error_code=ErrorCode.INVALID_JSON, extra_vars={"body": body})
