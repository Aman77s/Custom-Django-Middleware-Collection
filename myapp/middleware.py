from django.shortcuts import render
from django.conf import settings
import time
from django.utils.timezone import now
from .models import LoggingRecord


class MaintanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
        
    def __call__(self, request):
        
        
        if getattr(settings, "MAINTENANCE_MODE", False):
            
            return render(request, 'maintance.html')
        
        response = self.get_response(request)  # <--- this part
        return response
    
    
class RequestTime:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        start = time.time()
        
        response = self.get_response(request)
        duration = time.time() - start 
        print(f"Totatl time is {duration:.4f} seconds")
        
        return response
    
    
class LoggingRecords:
    def __init__(self,get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        response = self.get_response(request)
        
        LoggingRecord.objects.create(
                ip = request.META.get("REMOTE_ADDR"),
                path=request.path,
                method=request.method,
                timestamp=now()
        )
        
        return response
                 
                 