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
        """        Get method to handle the redirection of the shortened URL to the actual URL.

        Args:
            _ (object): Placeholder for unused parameter.
            referenceId (str): The reference ID of the shortened URL.

        Returns:
            dict: A JSON response containing the original URL corresponding to the reference ID.
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
        """        Post method to handle the logic of creating shortened URL.

        This method takes the input URL from the request data, creates a ShortUrls object with the URL,
        saves it to the database, and then constructs a shortened URL using the reference ID of the saved object.

        Args:
            request (HttpRequest): The HTTP request object containing the input data.

        Returns:
            JsonResponse: A JSON response containing the result of the operation and the shortened URL.
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
