from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Question
from users.models import CustomUser
from .serializers import QuestionSerializer, AnswerSerializer, CustomUserSerializer
from django.shortcuts import get_object_or_404


# View for handling questions
class QuestionView(APIView):
    def get(self, request):
        # Retrieve all questions from the database
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        # Return the serialized data as a JSON response
        return Response(serializer.data)


# View for handling answers
class AnswerView(APIView):
    def post(self, request):
        # Deserialize the incoming data
        serializer = AnswerSerializer(data=request.data)
        # Check if the deserialized data is valid
        if serializer.is_valid():
            # Retrieve the question using the question_id from the validated data
            question = get_object_or_404(Question, pk=serializer.validated_data['question_id'])
            # Get the selected option from the validated data
            selected_option = serializer.validated_data['selected_option']
            # Get the user from the request
            user = request.user

            # Check if the selected option is correct
            if selected_option == question.answer:
                # Increment the user's score
                user.ball += 1
            # Save the updated user data
            user.save()

            # Return a success response
            return Response({'message': 'Answer submitted successfully'}, status=status.HTTP_200_OK)
        # Return an error response if the data is not valid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Function-based view to get the user's score
@api_view(['GET'])
def user_ball_view(request):
    # Get the user from the request
    user = request.user
    serializer = CustomUserSerializer(user)
    # Return the user's score as a JSON response
    return Response({'ball': serializer.data['ball']})

