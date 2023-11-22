from django.shortcuts import render
from kafka_consumer.models import Zone
import json
# Create your views here.
from django.http import JsonResponse


def get_list(request):
    objects = Zone.objects.all()
    mas = []
    for obj in objects:
        mas.append(
            {
                "id": obj.id_zone,
                "in": obj.in_zone,
                "out": obj.out_zone
            }
        )
    return JsonResponse({"zones": mas})
