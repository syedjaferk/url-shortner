import json
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


class GetShortenUrl(View):
    """
    View class to get the actual url given shortened url
    """
    @csrf_exempt
    def get(self, request, referenceId):
        """
        Get method to handle the redirection of the shortened url to the actual url
        """
        return JsonResponse({'result': referenceId})

class CreateShortUrl(View):
    """
    View class to generate short url given actual url.
    """
    @csrf_exempt
    def post(self, request):
        """
        Post method to handle the logic of creating shortened url
        """
        request_data = json.loads(request.body)
        url = request_data.get("url")
        return JsonResponse({'result': 'success', 'url': url})

