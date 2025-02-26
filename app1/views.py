from django.shortcuts import render,redirect
from . forms import CustomUserCreationForm,CustomUserChangeForm,Passwordchangform
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from . models import CustomUser
from django.utils.encoding import force_bytes,force_str
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import update_session_auth_hash
from .tokens import account_activation_token


from django.utils.safestring import mark_safe
# Create your views here.


# def activate(request, uidb64, token):
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         user = CustomUser.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
#         user = None

#     if user and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         messages.success(request, "Thank you for email confirmation. Your account is now activated.")
#         return redirect('login_page')
#     else:
#         messages.error(request, "Invalid or expired activation link.")  # Token expired or invalid
#         return redirect('resend_acc')  # Redirect to resend page if expired
    # return redirect("home_page")

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Thank you for email confirmation. Your account is now activated.")
        return redirect('login_page')
    else:
        messages.error(request, "Invalid or expired activation link. Please request a new one.")
        return redirect('resend_acc')  # Redirect to resend page if expired






def home(request):
    data = CustomUser.objects.all()
    context ={'data':data}
    return render(request,"app1/home.html",context)


# def activateemail(request,user,to_email):
#     mail_subject ='activate you accoutn'
#     message = render_to_string("app1/activate_acc.html",{
#         'user':user.name,
#         'domain':get_current_site(request).domain,
#         'uid':urlsafe_base64_encode(force_bytes(user.pk)),
#         'token':account_activation_token.make_token(user),
#         'protocol': 'https' if request.is_secure() else 'http'
#     })
#     email = EmailMessage(mail_subject,message,to=[to_email])
#     email.content_subtype = "html" 
#     if email.send():
#         message_text = f'Dear <b>{user.name}</b>, we have sent a link to your email: <b>{to_email}</b>'
#         messages.success(request, mark_safe(message_text))
#         # messages.success(request,f'dear <b>{user.username}</b> we have a sent a link to your email{to_email}')
#     else:
#         messages.error(request,'problem sending email to you!')

# def activateemail(request, user, to_email):
#     mail_subject = 'Activate your account'
#     message = render_to_string("app1/activate_acc.html", {
#         'user': user.name,
#         'domain': get_current_site(request).domain,
#         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#         'token': account_activation_token.make_token(user),
#         'protocol': 'https' if request.is_secure() else 'http'
#     })
#     email = EmailMessage(mail_subject, message, to=[to_email])
#     email.content_subtype = "html"
#     if email.send():
#         message_text = f'Dear <b>{user.name}</b>, we have sent a link to your email: <b>{to_email}</b>'
#         messages.success(request, mark_safe(message_text))
#     else:
#         messages.error(request, 'Problem sending email to you!')

# from django.utils.timezone import now

# def activateemail(request, user, to_email):
#     """
#     Sends an account activation email with a fresh token.
#     """
    
#     mail_subject = 'Activate your account'
    
#     # Ensure user name exists
#     user_name = getattr(user, "name", "User")

#     # ✅ Force token refresh by updating `last_login` or adding a new field
#     user.last_login = now()  # Updating last_login ensures a new token is generated
#     user.save(update_fields=["last_login"])  

#     # ✅ Generate a **new** token for each activation email
#     token = account_activation_token.make_token(user)

#     # Encode user ID
#     uid = urlsafe_base64_encode(force_bytes(user.pk))

#     # Construct activation link
    
#     activation_link = f"http://{get_current_site(request).domain}/activate/{uid}/{token}"

#     # Render email message
#     message = render_to_string("app1/activate_acc.html", {
#         'user': user_name,
#         'domain': get_current_site(request).domain,
#         'uid': uid,
#         'token': token,
#         'protocol': 'https' if request.is_secure() else 'http'
#     })

#     # Create email
#     email = EmailMessage(mail_subject, message, to=[to_email])
#     email.content_subtype = "html"  # Ensure HTML email content

#     try:
#         if email.send():
#             message_text = f'Dear <b>{user_name}</b>, we have sent a link to your email: <b>{to_email}</b>'
#             messages.success(request, mark_safe(message_text))
#         else:
#             messages.error(request, 'Problem sending email. Please try again later.')
#     except Exception as e:
#         messages.error(request, f"Error sending email: {str(e)}")

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.utils.timezone import now

def activateemail(request, user, to_email):
    """
    Sends an account activation email with a fresh token.
    """
    mail_subject = 'Activate your account'
    
    # ✅ Ensure `user.name` exists, fallback to "User" if missing
    user_name = getattr(user, "name", "User")

    # ✅ Force token refresh by updating `last_login`
    user.last_login = now()  # Updating ensures a new token is generated
    user.save(update_fields=["last_login"])  

    # ✅ Generate a new token for every activation email
    token = account_activation_token.make_token(user)

    # Encode user ID
    uid = urlsafe_base64_encode(force_bytes(user.pk))

    # ✅ Determine if the request is HTTP or HTTPS
    protocol = "https" if request.is_secure() else "http"

    # ✅ Construct activation link dynamically
    activation_link = f"{protocol}://{get_current_site(request).domain}/activate/{uid}/{token}"

    # Render email message using template
    message = render_to_string("app1/activate_acc.html", {
        'user': user_name,
        'domain': get_current_site(request).domain,
        'uid': uid,
        'token': token,
        'protocol': protocol  # Pass protocol to the template if needed
    })

    # ✅ Create email
    email = EmailMessage(mail_subject, message, from_email="noreply@example.com", to=[to_email])
    email.content_subtype = "html"  # Ensure HTML email content

    try:
        if email.send():
            message_text = f'Dear <b>{user_name}</b>, we have sent a link to your email: <b>{to_email}</b>'
            messages.success(request, mark_safe(message_text))
        else:
            messages.error(request, 'Problem sending email. Please try again later.')
    except Exception as e:
        messages.error(request, f"Error sending email: {str(e)}")




def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            try:
                existing_user = CustomUser.objects.get(email=email)
                if existing_user.is_active:
                    messages.info(request, "This email is already registered and activated. Please log in.")
                    return redirect('login_page')
                else:
                    messages.info(request, "This email is already registered but not activated. Resending activation link.")
                    activateemail(request, existing_user, email)
                    return redirect('resend_acc')
            except CustomUser.DoesNotExist:
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                activateemail(request, user, email)
                return redirect("home_page")
    else:
        form = CustomUserCreationForm()

    context = {'form': form}
    return render(request, 'app1/register.html', context)

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            if not user.is_active:
                messages.error(request, "Your account is not activated yet. Please check your email for the activation link.")
                return redirect('resend_acc')
            login(request, user)
            return redirect('home_page')
        else:
            messages.error(request, "Invalid email or password")

    return render(request, 'app1/loginp.html')




def update_acc(request):

    if request.method =='POST':
        form =CustomUserChangeForm(request.POST,request.FILES,instance=request.user)
        
        if form.is_valid():
            form.save()                   
            return redirect("home_page")
    else:
        form = CustomUserChangeForm(instance=request.user)

    context ={'form':form}
    return render(request,'app1/update.html',context)

def resend_acc(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = CustomUser.objects.get(email=email)
            if user.is_active:
                messages.info(request, "Your account is already activated. You can log in.")
                return redirect('login_page')
            else:
                activateemail(request, user, email)
                messages.success(request, f"A new activation link has been sent to {email}. Please check your inbox.")
                return redirect('home_page')  # Redirect to home page after sending the email
        except CustomUser.DoesNotExist:
            messages.error(request, "This email address is not registered. Please sign up first.")
            return redirect('register')

    return render(request, 'app1/resend.html')  

def cng_pswrd(request):
    c_user = request.user  # Get the current authenticated user

    if request.method == 'POST':
        form = Passwordchangform(c_user, request.POST)  # Pass user and form data
        if form.is_valid():
            form.save()  # Save the new password
            update_session_auth_hash(request, c_user)  # Prevent logout after password change
            return redirect('home_page')  # Redirect after success
    else:
        form = Passwordchangform(c_user)  # Pass user only

    context = {'form': form}
    return render(request, 'app1/change_password.html', context)

