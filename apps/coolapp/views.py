from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
# from . import models
from .models import User, Quote

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User

def index(request):
    return render(request, 'coolapp/index.html')

def register_process(request):

	if request.method == "POST":
		result = User.objects.register(request.POST['first_name'],request.POST['last_name'],request.POST['email'],request.POST['password'], request.POST['confirm_password'])

		if result[0]==True:
			request.session['id'] = result[1].id
			print result, "*******************************************************"
			# request.session.pop('errors')
			return redirect('/quotes')
		else:

			# request.session['errors'] = result[1]
			messages.add_message(request, messages.WARNING, result[1][0])

			print result[1], "^^^^^^^^^^^^^^^^^^^^"
			return redirect('/')
	else:

		return redirect ('/')

def login_process(request):
	print "------------ POST ----------------\n", request.POST
	result = User.objects.login(request.POST['email'],request.POST['password'])

	if result[0] == True:
		request.session['id'] = result[1][0].id
		# We have result[1][0] this refers to the results of the query (user query returned) and index of zero which is what we just unwrapped.
		return redirect('/quotes')
	else:
		messages.add_message(request, messages.WARNING, result[1][0])

		# request.session['errors'] = result[1]
		return redirect('/')

def users(request):
	if not 'id' in request.session :
		return redirect('/')
	else:
		session = request.session['id']
        # quotesByUser = Quote.objects.all().order_by('-created_at')

		return render(request, "coolapp/users.html",)

def quotes(request):
	if not 'id' in request.session :
		return redirect('/')
	else:
		session = request.session['id']
        allQuotes = Quote.objects.all().order_by('-created_at')

        data = {
            'allQuotes': allQuotes,
        }

        print allQuotes.count()

        return render(request, "coolapp/quotes.html", data)

def add_quote(request):
	res = Quote.objects.create_quote(request.POST, request.session['id'])
	print "Quote ID", res[1].id, "#"*500
	return redirect ('/quotes')



def logout(request)	:
	del request.session['first_name']
	return redirect ('/')
