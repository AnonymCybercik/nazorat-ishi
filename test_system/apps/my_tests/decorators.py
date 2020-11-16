from django.http import HttpResponse
from django.shortcuts import redirect,reverse,render

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
				    return view_func(request, *args, **kwargs)

				if group == 'admin':
				    return view_func(request, *args, **kwargs)

				if group == 'admin2':
				    return view_func(request, *args, **kwargs)
			else:
			    return HttpResponse('siz bu sahifa uchun ro`yxatdan o`tmagansiz')
		return wrapper_func
	return decorator

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'customer':
			return redirect('user-page')

		if group == 'admin':
			return view_func(request, *args, **kwargs)

	return wrapper_function

