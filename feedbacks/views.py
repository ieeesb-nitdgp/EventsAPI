from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FeedbackSerializer
from .models import Feedback
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.core.exceptions import ValidationError

# Create your views here.

class FeedbackView(viewsets.ModelViewSet):
	serializer_class = FeedbackSerializer
	queryset = Feedback.objects.all()
	permission_classes = (AllowAny,)

	def list(self, request):
		queryset = Feedback.objects.all()
		serializer = FeedbackSerializer(queryset, many=True, context={'request': request})
		return Response(serializer.data)

	def create(self, request):
		print("Feedback")
		feedback = FeedbackSerializer(data=request.data)
		#feedback.is_valid(raise_exception=True)
		if feedback.is_valid() :
			print("validated")
			feedback.save()
		
		else:
			print(feedback.errors)
			raise ValidationError(('FORM is not validated'))
		
		
		headers = self.get_success_headers(feedback.data)
		return Response(feedback.data, headers=headers)