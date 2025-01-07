from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def drink_list(request):
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many = True)
        return JsonResponse({'drinks': serializer.data}) #, safe = False , if necessary
    
    if request.method == 'POST':
        serializer = DrinkSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])

def drink_detail(request, id):
    try:
        drink = Drink.objects.get(pk = id)
    except Drink.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        drink.delete()
        return JsonResponse(status = status.HTTP_204_NO_CONTENT)
    
    # I chose JsonResponse bcos of standard but u can also use return response.
    #Response will return data in html and json formart



