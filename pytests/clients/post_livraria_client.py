from playwright.sync_api import sync_playwright


class PostLivrariaClient:
    
    @staticmethod
    def post_livros(payload):
        with sync_playwright() as p:
            context = p.request.new_context()
            response = context.post("http://132.145.174.237:3000/livros", data=payload)
            return {
                "code": response.status,
                "body": response.text(),
                "headers": response.headers,
            }
