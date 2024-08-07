from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from utils.error_handler import error_handler
from .models import *
from utils.responses import SuccessResponse,FailureResponse
from django.db.models import Count
from .serializers import (
    AboutUseSerializer,
    OurServiceSerializer,
   FeatureSectionSerializer,
    OurTeamSerializer,
    PropertyInputSerializer,
    PropertyOutputSerializer,
    BlogSerializer,
    HeroSectionSerializer,
    TestimonySerializer,
    FillFormserializer,
    AgentSerializer,
    ReUsableSerializer,
    AgentMemberSerializer,
    AgentReadSerializer,
    AdminAppearanceSerializer,
    DeviceSerializer
)
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser
from drf_yasg.openapi import IN_QUERY, Parameter
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
        
class BlogApiView(APIView):
    parser_classes=[JSONParser,MultiPartParser,FormParser]
   
    @swagger_auto_schema(
            request_body=BlogSerializer
    )
    def post(self,request):
        try:
            serializer=BlogSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return SuccessResponse(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
    @swagger_auto_schema(
            manual_parameters=[
                Parameter("page", IN_QUERY, type="int", required=False),
                Parameter("limit", IN_QUERY, type="int", required=False),
            ]
    )
    def get(self,request):
        try:
            page = int(request.GET.get("page", 0))
            limit = int(request.GET.get("limit", 10))
            queryset=Blog.objects.order_by("-created_at").all()
            paginator = queryset[(page * limit) : (page * limit) + limit]
            return SuccessResponse(BlogSerializer(paginator,many=True).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
class SingleBlogApiView(APIView):
    parser_classes=[JSONParser,MultiPartParser,FormParser]

    def get(self,request,slug):
        try:
            instance=Blog.objects.get(slug=slug)
            return SuccessResponse(BlogSerializer(instance).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
    @swagger_auto_schema(
            request_body=BlogSerializer
    )
    def put(self,request,slug):
        try:
            instance=Blog.objects.get(slug=slug)
            serializer=BlogSerializer(instance=instance,data=request.data)
            serializer.is_valid(raise_exception=True)
            data=serializer.save()
            return SuccessResponse(BlogSerializer(data).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,slug):
        try:
            instance=Blog.objects.get(slug=slug)
            instance.delete()
            return SuccessResponse("Blog deleted",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

class PropertyApiView(APIView):
    parser_classes=[JSONParser,MultiPartParser,FormParser]
   
    @swagger_auto_schema(
            manual_parameters=[
                Parameter("page", IN_QUERY, type="int", required=False),
                Parameter("limit", IN_QUERY, type="int", required=False),
                Parameter("minprice",IN_QUERY,type="int",required=False),
                Parameter("maxprice",IN_QUERY,type="int",required=False)
            ]
    )
    def get(self,request):
        try:
            page = int(request.GET.get("page", 0))
            limit = int(request.GET.get("limit", 20))
            minprice=int(request.GET.get("minprice",0))
            maxprice=int(request.GET.get("maxprice",0))
            queryset=PropertyListing.objects.order_by("-created_at").all()
            if minprice!=0:
                queryset=queryset.filter(amount__gte=minprice)

            if maxprice !=0:
                queryset=queryset.filter(amount__lte=maxprice)

            paginator = queryset[(page * limit) : (page * limit) + limit]
            return SuccessResponse(PropertyOutputSerializer(paginator,many=True).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(
            request_body=PropertyInputSerializer
    )
    def post(self,request):
        try:
            serializer=PropertyInputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            images=serializer.validated_data.pop("images",None)
            data=serializer.save()
            #save image 
            if images:
                for image in images:
                    ImageAsset.objects.create(property=data,image=image)

            return SuccessResponse(PropertyOutputSerializer(data).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
class SinglePropertyApiView(APIView):
    parser_classes=[JSONParser,MultiPartParser,FormParser]

    def get(self,request,slug):
        try:
            instance=PropertyListing.objects.get(slug=slug)
            return SuccessResponse(PropertyOutputSerializer(instance).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
            request_body=PropertyInputSerializer
    )
    def put(self,request,slug):
        try:
            instance=PropertyListing.objects.get(slug=slug)
            serializer=PropertyInputSerializer(instance=instance,data=request.data)
            serializer.is_valid(raise_exception=True)
            images=serializer.validated_data.pop("images",None)
            data=serializer.save()
            #save image 
            if images:
                #delete the image associated to that instance
                ImageAsset.objects.filter(property=instance).delete()
                for image in images:
                #save new image
                    ImageAsset.objects.create(property=data,image=image)
            return SuccessResponse(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,slug):
        try:
            instance=PropertyListing.objects.get(slug=slug)
            #delete the image associated to that instance
            ImageAsset.objects.filter(property=instance).delete()
            instance.delete()
            return SuccessResponse("Property Deleted",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
class AboutApiView(APIView):
    parser_classes=[JSONParser,MultiPartParser,FormParser]

    @swagger_auto_schema(
            request_body=AboutUseSerializer
    )
    def post(self,request):
        try:
            serializer=AboutUseSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return SuccessResponse(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        try:
            queryset=AboutUs.objects.all()
            return SuccessResponse(AboutUseSerializer(queryset,many=True).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

class SingleAboutAPiView(APIView):
    parser_classes=[JSONParser,MultiPartParser,FormParser]
        
    @swagger_auto_schema(
            request_body=AboutUseSerializer
    )
    def put(self,request,pk):
        try:
            instance=AboutUs.objects.get(pk=pk)
            serializer=AboutUseSerializer(instance=instance,data=request.data)
            serializer.is_valid(raise_exception=True)
            data=serializer.save()
            return SuccessResponse(AboutUseSerializer(data).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        try:
            instance=AboutUs.objects.get(pk=pk)
            instance.delete()
            return SuccessResponse("About us deleted",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

class OurServicesApiView(APIView):
    @swagger_auto_schema(
            request_body=OurServiceSerializer
    )
    def post(self,request):
        try:
            serializer=OurServiceSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return SuccessResponse("saved",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        try:
            queryset=OurServices.objects.all()
            return SuccessResponse(OurServiceSerializer(queryset,many=True).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
class SingleOurServicesAPiView(APIView):
    @swagger_auto_schema(
            request_body=OurServiceSerializer
    )
    def put(self,request,pk):
        try:
            OurServices.objects.get(pk=pk)
            serializer=OurServiceSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return SuccessResponse("updated successful",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,pk):
        try:
            instance=OurServices.objects.get(pk=pk)
            instance.delete()
            return SuccessResponse("statement deleted",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
class TermsOfServiceApiView(APIView):

    @swagger_auto_schema(
            request_body=ReUsableSerializer
    )
    def post(self,request):
        try:
            serializer=ReUsableSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            #delete First

            TermsOfService.objects.create(**serializer.validated_data)
            return SuccessResponse(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        try:
            queryset=TermsOfService.objects.all()
            return SuccessResponse(ReUsableSerializer(queryset,many=True).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

class SingleTermsofserviceAPiView(APIView):
        
    @swagger_auto_schema(
            request_body=ReUsableSerializer
    )
    def put(self,request,pk):
        try:
            serializer=ReUsableSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            TermsOfService.objects.filter(pk=pk).update(
                **serializer.validated_data
            )
            return SuccessResponse("updated successfully",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,pk):
        try:
            instance=TermsOfService.objects.get(pk=pk)
            instance.delete()
            return SuccessResponse("Term of services deleted",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

class PrivatePolicyApiView(APIView):

    @swagger_auto_schema(
            request_body=ReUsableSerializer
    )
    def post(self,request):
        try:
            serializer=ReUsableSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            PrivatePolicy.objects.create(**serializer.validated_data)
            return SuccessResponse(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        try:
            queryset=PrivatePolicy.objects.all()
            return SuccessResponse(ReUsableSerializer(queryset,many=True).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

class SinglePrivacyAPiView(APIView):
    
    @swagger_auto_schema(
            request_body=ReUsableSerializer
    )
    def put(self,request,pk):
        try:
            serializer=ReUsableSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            PrivatePolicy.objects.filter(pk=pk).update(
                **serializer.validated_data
            )
            return SuccessResponse("updated successfully",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,pk):
        try:
            instance=PrivatePolicy.objects.get(pk=pk)
            instance.delete()
            return SuccessResponse("Privacy deleted",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

class OurTeamApiView(APIView):
    parser_classes=[JSONParser,MultiPartParser,FormParser]

    @swagger_auto_schema(
            request_body=OurTeamSerializer
    )
    def post(self,request):
        try:
            serializer=OurTeamSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return SuccessResponse(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        try:
            queryset=OurTeam.objects.all()
            return SuccessResponse(OurTeamSerializer(queryset,many=True).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

class SingleOurTeamAPiView(APIView):
    parser_classes=[JSONParser,MultiPartParser,FormParser]
    
    @swagger_auto_schema(
            request_body=OurTeamSerializer
    )
    def put(self,request,pk):
        try:
            instance=OurTeam.objects.get(pk=pk)
            serializer=OurTeamSerializer(instance=instance,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return SuccessResponse("updated successfully",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,pk):
        try:
            instance=OurTeam.objects.get(pk=pk)
            instance.delete()
            return SuccessResponse("Term of services deleted",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

class TestimonyApiView(APIView):
    parser_classes=[JSONParser,MultiPartParser,FormParser]
    @swagger_auto_schema(
            request_body=TestimonySerializer
    )
    def post(self,request):
        try:
            serializer=TestimonySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data=serializer.save()
            return SuccessResponse(TestimonySerializer(data).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request):
        try:
            queryset=Testimony.objects.all()
            return SuccessResponse(TestimonySerializer(queryset,many=True).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
            
class SingleTestimonyApiView(APIView):
    parser_classes=[JSONParser,MultiPartParser,FormParser]
     
    @swagger_auto_schema(
            request_body=TestimonySerializer
    )
    def put(self,request,pk):
        try:
            instance=Testimony.objects.get(pk=pk)
            serializer=TestimonySerializer(instance=instance,data=request.data)
            serializer.is_valid(raise_exception=True)
            data=serializer.save()
            return SuccessResponse(TestimonySerializer(data).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,pk):
        try:
            instance=Testimony.objects.get(pk=pk)
            instance.delete()
            return SuccessResponse("Testimony deleted",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
class FillFormAPiView(APIView):
    def post(self,request):
        try:
            serializer=FillFormserializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return SuccessResponse("Message sent",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
class AgentApiView(APIView):
    parser_classes=[JSONParser,MultiPartParser,FormParser]

    @swagger_auto_schema(
            request_body=AgentSerializer
    )
    def post(self,request):
        try:
            serializer=AgentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return SuccessResponse(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        try:
            queryset=Agent.objects.all()
            return SuccessResponse(AgentReadSerializer(queryset,many=True).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

class SingleAgentAPiView(APIView):
    parser_classes=[JSONParser,MultiPartParser,FormParser]
    
    @swagger_auto_schema(
            request_body=AgentSerializer
    )
    def put(self,request,pk):
        try:
            instance=Agent.objects.get(pk=pk)
            serializer=AgentSerializer(instance=instance,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return SuccessResponse("updated successfully",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,pk):
        try:
            instance=Agent.objects.get(pk=pk)
            instance.delete()
            return SuccessResponse("Agent deleted",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
class AgentMemberApiView(APIView):
    parser_classes=[JSONParser,MultiPartParser,FormParser]

    @swagger_auto_schema(
            request_body=AgentMemberSerializer
    )
    def post(self,request):
        try:
            serializer=AgentMemberSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return SuccessResponse(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        try:
            queryset=AgentMember.objects.all()
            return SuccessResponse(AgentMemberSerializer(queryset,many=True).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

class SingleAgentMemberAPiView(APIView):
    parser_classes=[JSONParser,MultiPartParser,FormParser]
    
    @swagger_auto_schema(
            request_body=AgentMemberSerializer
    )
    def put(self,request,pk):
        try:
            instance=AgentMember.objects.get(pk=pk)
            serializer=AgentMemberSerializer(instance=instance,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return SuccessResponse("updated successfully",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,pk):
        try:
            instance=AgentMember.objects.get(pk=pk)
            instance.delete()
            return SuccessResponse("Agent deleted",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

class HeroSectionApiView(APIView):
    parser_classes=[JSONParser,MultiPartParser,FormParser]

    @swagger_auto_schema(
            request_body=HeroSectionSerializer
    )
    def post(self,request):
        try:
            serializer=HeroSectionSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return SuccessResponse(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        try:
            queryset=HeroSection.objects.all()
            return SuccessResponse(HeroSectionSerializer(queryset,many=True).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

class SingleHeroSectionAPiView(APIView):
    parser_classes=[JSONParser,MultiPartParser,FormParser]
    
    @swagger_auto_schema(
            request_body=HeroSectionSerializer
    )
    def put(self,request,pk):
        try:
            instance=HeroSection.objects.get(pk=pk)
            serializer=HeroSectionSerializer(instance=instance,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return SuccessResponse("updated successfully",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,pk):
        try:
            instance=AgentMember.objects.get(pk=pk)
            instance.delete()
            return SuccessResponse("Agent deleted",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

class FeatureSectionApiView(APIView):
    parser_classes=[JSONParser,MultiPartParser,FormParser]

    @swagger_auto_schema(
            request_body=FeatureSectionSerializer
    )
    def post(self,request):
        try:
            serializer=FeatureSectionSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return SuccessResponse(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        try:
            queryset=FeatureSection.objects.all()
            return SuccessResponse(FeatureSectionSerializer(queryset,many=True).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

class SingleFeatureSectionAPiView(APIView):
    parser_classes=[JSONParser,MultiPartParser,FormParser]
    
    @swagger_auto_schema(
            request_body=FeatureSectionSerializer
    )
    def put(self,request,pk):
        try:
            instance=FeatureSection.objects.get(pk=pk)
            serializer=FeatureSectionSerializer(instance=instance,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return SuccessResponse("updated successfully",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,pk):
        try:
            instance=FeatureSection.objects.get(pk=pk)
            instance.delete()
            return SuccessResponse("Agent deleted",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

class HomeSectionApiView(APIView):
    def get(self,request):
        try:
            hero=HeroSection.objects.all()[:10]
            about=AboutUs.objects.all()[:10]
            service=OurServices.objects.all()[:10]
            featured=FeatureSection.objects.all()[:10]
            agent=Agent.objects.all()[:10]
            team=TermsOfService.objects.all()[:10]
            policy=PrivatePolicy.objects.all()[:10]

            data={
                "hero_section":HeroSectionSerializer(hero,many=True).data,
                "about_us":AboutUseSerializer(about,many=True).data,
                "service":OurServiceSerializer(service,many=True).data,
                "feature":FeatureSectionSerializer(featured,many=True).data,
                "agent":AgentReadSerializer(agent,many=True).data,
                "term_of_service":ReUsableSerializer(team,many=True).data,
                "policy":ReUsableSerializer(policy,many=True).data
            }
            return SuccessResponse(data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

class AdminAppearanceApiView(APIView):
    @swagger_auto_schema(
            request_body=AdminAppearanceSerializer
    )
    def post(self,request):
        try:
            serializer=AdminAppearanceSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            AdminAppearance.objects.all().delete()
            serializer.save()
            return SuccessResponse(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request):
        try:
            instance=AdminAppearance.objects.last()
            serializer=AdminAppearanceSerializer(instance).data
            return SuccessResponse(serializer,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
#DashBoard
class DashBoardApiView(APIView):
    def get(self,request):
        try:
            recent_post=Blog.objects.count()            
            agent=Agent.objects.count()
            view_property=PropertyListing.objects.count()
            device_counts = Device.objects.values('name').annotate(name_count=Count('name')).order_by('-name_count').all()
            visitor = MostViewPage.objects.count()
            res={
                "visitor":visitor,
                "blogPost":recent_post,
                "property":view_property,
                "agent":agent,
                "top_browser":DeviceSerializer(device_counts,many=True).data if device_counts != None else None
            }
            return SuccessResponse(res,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
#Home
        
class HomeApiView(APIView):
    def get(self,request):
        try:
            feature_property=PropertyListing.objects.order_by("-created_at").all()[:10] 
            our_service=OurServices.objects.all()[:10]
            testimony=Testimony.objects.all()[:10]
            about_us=AboutUs.objects.all()[:10]
            our_agent=Agent.objects.all()[:10]
            res={
                "feature_property":PropertyOutputSerializer(feature_property,many=True).data,
                "our_service":OurServiceSerializer(our_service,many=True).data,
                "testimony":TestimonySerializer(testimony,many=True).data,
                "about_us":AboutUseSerializer(about_us,many=True).data,
                "agent":AgentReadSerializer(our_agent,many=True).data
            }
            return SuccessResponse(res,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)


