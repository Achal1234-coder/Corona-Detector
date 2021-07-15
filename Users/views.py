from django.db.models.query_utils import PathInfo
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import UserSignUpForm, UserLogInForm, UserSymptomForm
from django.contrib.auth import authenticate, logout, login
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from django.contrib.auth.decorators import login_required
from .models import UserSymptomFormModel



def home_view(request):

    if request.user.is_authenticated:
        redirect('Users:LogOut')
    form1 = UserSignUpForm(request.POST or None)
    form2 = UserLogInForm(request.POST or None)


    if request.method == "POST":
        if form1.is_valid():
            form1.save()
            username = request.POST.get('username')
            password = request.POST.get('password2')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                userform = UserSymptomForm()
                return render(request, "Users/user.html", {"form": form2, "userform": userform})
            else:
                return HttpResponse("<h1>You are not authorized User to see this Page</h1>")


        elif form2.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                userform = UserSymptomForm()
                return render(request, "Users/user.html", {"form": form2, "userform": userform})
            else:
                return HttpResponse("<h1>You are not authorized User to see this Page</h1>")


    return render(request, "Users/Log-in.html", {'form1': form1, 'form2': form2})


def log_out_view(request):
    logout(request)
    return redirect('Users:home')

login_required(login_url='Users:home')
def detect(request):

    form = UserSymptomForm(request.POST or None)
    if form.is_valid():
        form.save()

        dataset = pd.read_csv('Covid-data-set.csv')
        x = dataset.iloc[:, :7].values.astype(float)
        y = dataset.iloc[:, 7].values.astype(float)
        test = []

        cough = request.POST.get('cough')
        cold = request.POST.get('cold')
        fever = request.POST.get('fever')
        breath_less_ness = request.POST.get('breath_less_ness')
        pain = request.POST.get('pain')
        loss_of_test_or_smell = request.POST.get('loss_of_test_or_smell')
        sore_throat = request.POST.get('sore_throat')


        test.append(float(cough))
        test.append(float(cold))
        test.append(float(fever))
        test.append(float(breath_less_ness))
        test.append(float(pain))
        test.append(float(loss_of_test_or_smell))
        test.append(float(sore_throat))



        y = y.reshape(-1, 1)

        decision_tree = DecisionTreeClassifier()

        decision_tree.fit(x, y)

        y_pred = decision_tree.predict([test])

        if int(y_pred) == 0:
            result = 'Very High Probability'
        elif int(y_pred) == 1:
            result = 'High Probability'
        elif int(y_pred) == 2:
            result = 'Medium'
        elif int(y_pred) == 3:
            result = 'Low Probability'

        return render(request, "Users/result.html", {'result': result})
