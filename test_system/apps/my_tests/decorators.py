from django.http import HttpResponse
from django.shortcuts import redirect,reverse

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				if group == 'student':
				    return redirect(reverse('my_tests:user_profile',args = (request.user.id,)))

				if group == 'admin':
				    return redirect(reverse('my_tests:admin',args = (request.user.id,)))

				if group == 'admin1':
				    return redirect(reverse('admin_my_tests:home',args = (request.user.id,)))
			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapper_func
	return decorator


def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'student':
			return redirect('my_tests:user_profile',args = (request.user.id,))

		if group == 'admin':
			return view_func(request, *args, **kwargs)

	return wrapper_function