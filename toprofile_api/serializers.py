from .models import *
from rest_framework import serializers


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields="__all__"
        extra_kwargs={
            "slug":{
                "read_only":True
            }
        }

class PropertyInputSerializer(serializers.ModelSerializer):
    images=serializers.ListField(
        child=serializers.ImageField(),
        default=[],
        write_only=True,
    )
    class Meta:
        model=PropertyListing
        exclude=[
            "slug"
        ]

class PropertyOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model=PropertyListing
        fields="__all__"
        
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

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=HeroSection
        fields="__all__"

class FeatureSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=FeatureSection
        fields="__all__"

class AboutUseSerializer(serializers.ModelSerializer):
    class Meta:
        model=AboutUs
        fields="__all__"

class OurServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=OurServices
        fields="__all__"

class  OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=OurTeam
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
    
class  AgentReadSerializer(serializers.ModelSerializer):
    agent=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Agent
        fields="__all__"
    
    def get_agent(self,obj):
        return AgentMemberSerializer(obj.agent.all(),many=True).data

class  AgentMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=AgentMember
        fields="__all__"

class ReUsableSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    content=serializers.CharField(required=True)

class AdminAppearanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdminAppearance
        fields="__all__"


class DeviceSerializer(serializers.Serializer):
    name=serializers.CharField()
    name_count=serializers.IntegerField()