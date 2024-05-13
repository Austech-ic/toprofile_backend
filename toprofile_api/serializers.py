from .models import *
from rest_framework import serializers


class ListingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ListingCategory
        fields="__all__"

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields="__all__"

class PropertyInputSerializer(serializers.ModelSerializer):
    images=serializers.ListField(
        child=serializers.ImageField(),
        default=[],
        write_only=True,
    )
    class Meta:
        model=PropertyListing
        fields="__all__"

class PropertyOutputSerializer(serializers.ModelSerializer):
    monthly_payment=serializers.SerializerMethodField()
    price_per_sqr=serializers.SerializerMethodField()
    class Meta:
        model=PropertyListing
        fields="__all__"

    def get_price_per_sqr(self,obj):
        return (obj.land_space * obj.price)
    
    def get_monthly_payment(self,obj):
        return int(obj.price) // (12*obj.duration)
    
    def to_representation(self, instance):
        representation= super().to_representation(instance)
        images=ImageAsset.objects.select_related("property")\
            .filter(property=instance)
        representation["images"]=ImageAssetSerializer(images,many=True).data
        return representation

class ImageAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model=ImageAsset
        fields=[
            "id",
            "image"
        ]


# class PrivatePolicySerializer(serializers.ModelSerializer):
#     class Meta:
#         model=PrivatePolicy
#         fields="__all__"

# class TermsOfServiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=TermsOfService
#         fields="__all__"

class AboutUseSerializer(serializers.ModelSerializer):
    class Meta:
        model=AboutUs
        fields="__all__"

class OurServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=OurServices
        fields="__all__"

#statement,termsofservices,privatepolicy
class ReUsableSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=500)
    content=serializers.CharField()

class  OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=OurTeam
        fields="__all__"

class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model=HomePage
        fields="__all__"

class TestimonySerializer(serializers.ModelSerializer):
    class Meta:
        model=Testimony
        fields="__all__"


class FillFormserializer(serializers.ModelSerializer):
    class Meta:
        model=FillContactForm
        fields="__all__"


class  AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Agent
        fields="__all__"