from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
# from . import models
from .models import User, Quote, Favorite

# Render home page
def index(request):
    return render(request, 'coolapp/index.html')

# Sign up user
def register_process(request):

	if request.method == "POST":
		result = User.objects.register(request.POST['first_name'],request.POST['last_name'],request.POST['email'],request.POST['password'], request.POST['confirm_password'])

		if result[0]==True:
			request.session['id'] = result[1].id
			print result, "*******************************************************"
			request.session.pop('errors')
			return redirect('/quotes')
		else:

			request.session['errors'] = result[1]
			messages.add_message(request, messages.WARNING, result[1][0])

			print result[1], "^^^^^^^^^^^^^^^^^^^^"
			return redirect('/')
	else:

		return redirect ('/')

# Log user in
def login_process(request):
	# print "------------ POST ----------------\n", request.POST
	result = User.objects.login(request.POST['email'],request.POST['password'])
	if result[0] == True:
		request.session['id'] = result[1][0].id
		# We have result[1][0] this refers to the results of the query (user query returned) and index of zero which is what we just unwrapped.
		return redirect('/quotes')
	else:
		messages.add_message(request, messages.WARNING, result[1][0])
		request.session['errors'] = result[1]
		return redirect('/')

# Grab specific user in the site
def user(request, id):
	if not 'id' in request.session :
		return redirect('/')
	else:
		session = request.session['id']
        loggedInUser = User.objects.filter(id=session)
        user = User.objects.filter(id=session)
        userName = user[0].first_name

        allQuotes = Quote.objects.filter(user__id=id).order_by('-created_at')
        quoteCount = allQuotes.count()

        data = {
            'allQuotes': allQuotes,
            'userName': userName,
            'quoteCount': quoteCount,
            'loggedInUser': loggedInUser[0].first_name,
            'quotePosterUserName': allQuotes[0].user.first_name,
            'sessionID': session
        }

	return render(request, "coolapp/user.html", data)

# Fetch all quotes
def quotes(request):
	if not 'id' in request.session :
		return redirect('/')
	else:
		session = request.session['id']
        loggedInUserObject = User.objects.filter(id=session)
        allQuotes = Quote.objects.all().exclude(favoritequote__user__id=session).order_by('-created_at')
        quotePosterUserObject = User.objects.filter(id=session)
        quotePosterUserName = quotePosterUserObject[0].first_name
        favQuote = Favorite.objects.all().filter(user__id=session).order_by('-created_at')
        # print favQuote, "*"*300


        data = {
            'allQuotes': allQuotes,
            'quotePosterUserName': quotePosterUserName,
            'quotePosterUserID': session,
            'loggedInUser': loggedInUserObject[0].first_name,
            'favQuotes': favQuote,
            'session': session,
        }

        # print allQuotes.count()
        return render(request, "coolapp/quotes.html", data)

# Add a new quote
def add_quote(request):
    res = Quote.objects.create_quote(request.POST, request.session['id'])
    if res[0] == True:
        return redirect('/quotes')
    else:
        request.session['errors'] = res[1]
        messages.add_message(request, messages.WARNING, res[1][0])
        return redirect ('/quotes')

# Delete quote
def del_quote(request, id):
    session = request.session['id']
    res = Quote.objects.filter(id = id).delete()
    return redirect ('/quotes')


# Add a quote to your favorites
def add_fav(request, id):
	Favorite.objects.add_fav(id, request.session['id'])
	return redirect('/quotes')

# Remove a quote from your favorites
def remove_fav(request, id):
	res = Favorite.objects.filter(quote_id=id).delete()
        print res, "^"*300
	return redirect ('/quotes')

# Show all users of the site
def show_all_users(request):
    res = User.objects.all()
    data = {
        'allUsers': res
        }

    print res, "*"*300

    return render(request, 'coolapp/show_all_users.html', data)

# Clear session and log out
def logout(request)	:
	del request.session['id']
	return redirect ('/')
