from playwright.sync_api import sync_playwright
from pytests.support.api_utils import ApiUtils
from pytests.support.hooks import *


class PostLivrariaClient:
    
    @staticmethod
    def post_livros(payload):
        with sync_playwright() as p:
            context = p.request.new_context()
            response = context.post("http://132.145.174.237:3000/livros", data=payload)
            LOG.log_info("POST")
            LOG.log_info("URL: http://132.145.174.237:3000/livros")
            return {
                "code": response.status,
                "body": response.text(),
                "headers": response.headers,
            }

    @staticmethod
    def validate_response(response, code):
        ApiUtils.request_parse_log(response)
        ApiUtils.validate_status_code(response, code)
        