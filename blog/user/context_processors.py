from .forms import loginForm


def login_modal_form(request):
	return {'login_modal_form': loginForm()}