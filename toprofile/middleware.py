from toprofile_api.models import Device,MostViewPage
from django.utils.deprecation import MiddlewareMixin

class DeviceTrackerMiddleware(MiddlewareMixin):
        
    def process_request(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        user_agent=request.META.get('HTTP_USER_AGENT', '').lower()
        if request.path != "/":
            if "iphone" in user_agent:
                Device.objects.create(
                    name="Mobile"
                )
            if "macintosh" in user_agent:
                Device.objects.create(
                    name="Web"
                )
            if "android" in user_agent:
                Device.objects.create(
                    name="Mobile"
                )
            if "windows" in user_agent:
                Device.objects.create(
                    name="Web"
                )
        return response
    
class MostViewPageMiddleware(MiddlewareMixin):
        
    def process_request(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        #home,property,blog
        if "home" in request.path:
            MostViewPage.objects.create(
                    name="HOME"
                )
        return response