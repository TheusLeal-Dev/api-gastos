from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from .models import Gasto
from .serializers import GastoSerializer

@api_view(['GET', 'POST'])
def gastos_list_create(request):
    if request.method == 'GET':
        gastos = Gasto.objects.all()
        serializer = GastoSerializer(gastos, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = GastoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def gastos_detail(request, pk):
    try:
        gasto = Gasto.objects.get(pk=pk)
    except Gasto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(GastoSerializer(gasto).data)

    if request.method == 'PUT':
        serializer = GastoSerializer(gasto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        gasto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def gastos_total(request):
    total = Gasto.objects.aggregate(total=Sum('valor'))['total'] or 0
    return Response({'total': total})
