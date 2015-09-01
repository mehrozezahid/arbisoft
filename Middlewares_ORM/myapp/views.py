from django.shortcuts import render_to_response
from django.template import RequestContext
from myapp.forms import UserForm


def login_view(request):

    if request.user.is_authenticated():
        user = request.user
        user_form = UserForm()
        error = None
        return render_to_response(
            'myapp/login.html',
            {'form': user_form, 'user': user, 'error': error}
        )

    else:
        context = RequestContext(request)
        user_form = UserForm(data=request.POST)
        user = request.user
        error = None

    return render_to_response(
        'myapp/login.html',
        {'form': user_form, 'user': user, 'error': error}, context
    )
