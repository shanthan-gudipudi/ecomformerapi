from rest_framework import serializers
from farmer.models import Yards,Items

class YardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yards
        fields = ('id','yardname','yardlocation','yarddiscription','yardcontact','yardaddress','yardimg','status','published','author')



class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('id','itemname','itemprice','itemdiscription','itemimg','itemstatus','itemtype','published','itemproducer')