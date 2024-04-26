import json
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from shortner.models import ShortUrls


class GetShortenUrl(View):
    """
    View class to get the actual url given shortened url
    """
    @csrf_exempt
    def get(self, _, referenceId):
        """
        Get method to handle the redirection of the shortened url to the actual url
        """
        filtered_objects = ShortUrls.objects.filter(referenceId=referenceId)
        if filtered_objects.count() > 0:
            url_object = filtered_objects[0]
            return JsonResponse({'url': url_object.url})
        else:
            return JsonResponse({'message': 'Given url not found'})

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
        filtered_objects = ShortUrls.objects.filter(url=url)
        if filtered_objects.count() == 0:
            short_url_obj = ShortUrls(url=url)
            short_url_obj.save()
        else:
            short_url_obj = filtered_objects[0]
        short_url = request.build_absolute_uri('/') + short_url_obj.referenceId
        return JsonResponse({'result': 'success', 'url': short_url})
