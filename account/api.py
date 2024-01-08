from django.http import JsonResponse
from rest_framework.decorators import api_view,authentication_classes,permission_classes

from .form import SignUpForm

@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def signup(request):
    data = request.data
    message = 'success'
    print(request.data)
    form = SignUpForm({
        'name':data.get('name'),
        'email':data.get('email'),
        'password1':data.get('password1'),
        'password2':data.get('password2'),
    })
    
    if form.is_valid():
        form.save()
    else:
        message = 'error '
    
    return JsonResponse({'message':message})

@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id':request.user.id,
        'name':request.user.name,
        'email':request.user.email,
    })