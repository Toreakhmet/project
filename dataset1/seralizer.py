from rest_framework import serializers
from .models import *


class taraz_ser(serializers.ModelSerializer):
    class Meta:
        model=taraz
        fields=['name_sea','description','size_sez']