
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader

from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from telephony.forms import ContactForm, AsteriskForm
from django.core.mail import send_mail

from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login

from telephony.models import Asterisk


def index(request):
    # set permission
    if 'username' in request.session:
        return HttpResponseRedirect('/telephony/home/')

    page_title = "Login Form"

    context = {
        'page_title': page_title,
    }

    return render(request, 'telephony/login.html', context)

def home(request):

    # set permission
    if 'username' not in request.session:
        return HttpResponseRedirect('/telephony/')

    page_title = "Home"

    context = {
        'page_title': page_title,
        }

    return render(request, 'telephony/home.html', context)

def contact(request):

    # set permission
    if 'username' not in request.session:
        return HttpResponseRedirect('/telephony/')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # Single Email send to user
#            send_mail(
#                cd['subject'],
#                cd['message'],
##                cd.get('email'), ['imran.meditation@gmail.com'], fail_silently=False
#                'imran.meditation@gmail.com',
#                [cd['email']]
#            )
            #End Single Email Send

            # Start HTML Email Send alternatively
            from django.core.mail import EmailMultiAlternatives

            subject, from_email, to = cd['subject'], 'imran.meditation@gmail.com', cd['email']
            text_content = ''
            html_content = cd['message']
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            # End html email send alternatively

            return HttpResponseRedirect('/telephony/thanks/')
    else:
        form = ContactForm()

    return render(request, 'telephony/contact.html', {'form': form, 'page_title':'Contact Form'})



def thanks(request):
    # set permission
    if 'username' not in request.session:
        return HttpResponseRedirect('/telephony/')

    return render(request, 'telephony/thanks.html', {'page_title':'Sending Successfully!'})






def user_login(request):
    state = ""
    username = password = ''

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
#                state = "You're successfully logged in!"
                request.session['username'] = username
                return HttpResponseRedirect('/telephony/home/')

            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render(request, 'telephony/login.html',{'state':state, 'username': username, 'page_title': 'Login Form'})


def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass

    return HttpResponseRedirect('/telephony/')


# asterisk user management

def adduser(request):
    # set permission
    if 'username' not in request.session:
        return HttpResponseRedirect('/telephony/')

    error = ''

    if request.method == 'POST':
        form = AsteriskForm(request.POST)
        if form.is_valid():
            fields = form.cleaned_data
            try:
                insert = Asterisk(
                    name = fields['name'],
                    bind = fields['bind'],
                    secret = fields['secret'],
                    user = fields['user'],
                    email = fields['email'],
                    mobile = fields['mobile'])

                insert.save()

                if fields['email']:
                    #Send email to user
                    from django.core.mail import EmailMultiAlternatives

                    subject, from_email, to = 'IP Telephony Test Email', 'imran.meditation@gmail.com', fields['email']
                    text_content = ''

                    html_content = "<img src='http://i.imgur.com/AAuTuLH.png' alt='QIPT LOGO' />"
                    html_content += "<p>Dear " + fields['name'] + "</p>"
                    html_content += "<p>Your IP Telephony account is created.</p>"
                    html_content += "<p>Further any query feel free contact with us </p>"
                    html_content += "<p> Mobile : +8801711400092 <br /> Email address : tarik@quantummethod.org.bd </p>"
                    html_content += "<br /><br /><br />"
                    html_content += "<p>---<br />Thank You<br /><b>Tarik Mahmud</b></p>"

                    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                    #End Send email to user

                return HttpResponseRedirect('/telephony/users/')

            except:
                error = "Duplicate Entry"

    else:
        form = AsteriskForm()

    return render(request, 'telephony/adduser.html', {'form': form, 'page_title':'Add User', 'error':error})





def edituser(request, uid):
    # set permission
    if 'username' not in request.session:
        return HttpResponseRedirect('/telephony/')

    user = get_object_or_404(Asterisk, id = uid)
    error = ''

    if request.POST:
        try:
            edit = Asterisk.objects.get(id=uid) # object to update
            edit.name = request.POST['name'] # update name
            edit.bind = request.POST['bind']
            edit.secret = request.POST['secret']
            edit.user = request.POST['user']
            edit.email = request.POST['email']
            edit.mobile = request.POST['mobile']
            edit.save() # save object
        except: error = 'Duplicate Value'

        return HttpResponseRedirect('/telephony/users/')


    return render(request, 'telephony/edituser.html', {'user':user,'page_title':'Edit User', 'error':error})


def deleteuser(request, uid):
    # set permission
    if 'username' not in request.session:
        return HttpResponseRedirect('/telephony/')


    emp = Asterisk.objects.get(id=uid)
    emp.delete()

    return HttpResponseRedirect('/telephony/users/')


def alluser(request):
    # set permission
    if 'username' not in request.session:
        return HttpResponseRedirect('/telephony/')

#    users = Asterisk
    users = poll = Asterisk.objects.all()

    return render(request, 'telephony/alluser.html', {'users': users,'page_title':'All User'})

def applyzone(request):
    # set permission
    if 'username' not in request.session:
        return HttpResponseRedirect('/telephony/')

    users = poll = Asterisk.objects.all()

    zone = open('/etc/asterisk/sip.conf', 'w')

    for user in users:
        try:
            zone.write('['+ user.name + ']\nbind = ' + user.bind + '\nsecret = ' + user.secret + '\nuser = ' + user.user + '\n\n')
        except:
            print('The file is not writable')



    return HttpResponseRedirect('/telephony/users/')


def sip(request):
    # set permission
    if 'username' not in request.session:
        return HttpResponseRedirect('/telephony/')

    zone = open('/etc/asterisk/sip.conf', 'r')


    return render(request, 'telephony/sip.html', {'page_title':'SIP FILE', 'zone':zone})

#To send email individual user
def sendemail(request):

    # set permission
    if 'username' not in request.session:
        return HttpResponseRedirect('/telephony/')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # Single Email send to user
            #            send_mail(
            #                cd['subject'],
            #                cd['message'],
            ##                cd.get('email'), ['imran.meditation@gmail.com'], fail_silently=False
            #                'imran.meditation@gmail.com',
            #                [cd['email']]
            #            )
            #End Single Email Send

            # Start HTML Email Send alternatively
            from django.core.mail import EmailMultiAlternatives

            subject, from_email, to = cd['subject'], 'imran.meditation@gmail.com', cd['email']
            text_content = ''
            html_content = cd['message']
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            # End html email send alternatively

            return HttpResponseRedirect('/telephony/thanks/')
    else:
        form = ContactForm()

    return render(request, 'telephony/sendemail.html', {'form': form, 'page_title':'Email Sending Form'})


# documentation page, user guide
def doc(request):

    return render(request, 'telephony/documentation.html', {'page_title':'Documentation'})


def search(request):

    # set permission
    if 'username' not in request.session:
        return HttpResponseRedirect('/telephony/')

    user = None
    error = ''




    if request.POST:
        if 'search_item' in request.POST:

            item = request.POST['search_item']
    #        query = 'SELECT * FROM asterisk WHERE name = %s' % item
    #        user = Asterisk.objects.raw(query)
            from django.db.models import Q
    #        user = Asterisk.objects.filter(name = request.POST['search_item'])
            try:
                user = get_object_or_404(Asterisk, Q(name = item) | Q(email = item) | Q(mobile = item))
            except: error = "Please enter your search item again."


    return render(request, 'telephony/search.html', {'page_title':'Search Area', 'user':user, 'error':error})


