from django.utils.deprecation import MiddlewareMixin

class PublicAPICacheHeadersMiddleware(MiddlewareMixin):
    """
    Add Cache-Control headers for public API endpoints
    so Cloudflare can cache them.
    """
    def process_response(self, request, response):
        path = request.path
        if path.startswith("/api/"):
            response["Cache-Control"] = "public, max-age=300, s-maxage=300"
            response.cookies.clear()  # Remove session cookies so CF will cache
        elif path.startswith("/media/"):
            response["Cache-Control"] = "public, max-age=86400, s-maxage=86400"  # 1 day
        return response