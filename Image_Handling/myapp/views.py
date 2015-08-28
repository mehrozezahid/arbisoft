from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from myapp.forms import UserSignUp, UserLogin, UploadPictureForm
from models import UserProfile


def sign_up(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserSignUp(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True

        else:
            print user_form.errors

    else:
        user_form = UserSignUp()

    return render_to_response(
        'myapp/signup.html',
        {'user_form': user_form, 'registered': registered}, context
    )


def login_view(request):

    if request.user.is_authenticated():
        user = request.user
        user_form = UserLogin()
        error = None
        return render_to_response(
            'myapp/login.html',
            {'form': user_form, 'user': user, 'error': error}
        )

    else:
        context = RequestContext(request)
        user_form = UserLogin(data=request.POST)
        error = None

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

            else:
                error = "Username or password is incorrect"

        else:
            user = UserLogin()


    return render_to_response(
        'myapp/login.html',
        {'form': user_form, 'user': user, 'error': error}, context
    )


@login_required(login_url='/myapp/login')
def upload_picture(request):
    context = RequestContext(request)
    user = request.user

    if request.method == 'POST':
        pic_form = UploadPictureForm(request.POST, request.FILES)

        if pic_form.is_valid():
            path = pic_form.save_image(request.user, request.FILES['picture'])
            UserProfile.objects.create(user=user, picture=path)
            # try:
            #     m = UserProfile.objects.get(user=user)
            #     m.picture.delete()
            #     m.picture = request.FILES['picture']
            #     m.save()
            #
            # except ObjectDoesNotExist:
            #     UserProfile.objects.create(user=user, picture=request.FILES['picture'])

            HttpResponseRedirect('myapp/profile')

    else:
        pic_form = UploadPictureForm()

    return render_to_response('myapp/uploadpicture.html', {'pic_form': pic_form, 'user': user}, context)


@login_required(login_url='/myapp/login')
def profile(request):
    context = RequestContext(request)
    user = request.user

    # try:
    #     obj = UserProfile.objects.get(user=user)
    #
    # except ObjectDoesNotExist:
    #     obj = None

    pic_path = UploadPictureForm.get_image(user)

    return render_to_response(
        'myapp/profile.html',
        {'pic': pic_path, 'user': user}, context
    )