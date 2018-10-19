from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView

from dogs.models import Dog

#Set Api Key for handling payments
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY



class HomePageView(TemplateView):
    template_name = 'index.html'

    def post(self, request, **kwargs):
        context = self.get_context_data()
        post_data = self.request.POST
        token = self.request.POST.get('stripeToken', '')
        
        # Check for custom donation
        if post_data.get('custom-donation-option'):
            amount = float(post_data.get('custom-donation-option')
                           ) * 100  # convert donation to cents
        else:
            # Defaults to $5.00 if the donation amount never changed
            amount = post_data.get('donation-option', 500)

        try:
            # Create the stripe charge
            charge = stripe.Charge.create(
                amount=int(amount),  # convert to integer of cents in USD
                currency='usd',
                description='Donation',
                source=token
            )
            context["amount"] = int(amount) / 100  # back to float for context
            context["payment"] = 'success'
            context["payment_header"] = 'Success!'
            context["payment_message"] = "Congratulate yourself on being awesome!<br>We appreciate your generosity."

        except stripe.error.CardError:
            context["payment"] = 'declined'
            context["payment_header"] = 'Payment Method Declined.'
            context["payment_message"] = "There was an error in processing your card"

        except stripe.error.InvalidRequestError:
            """
            If a user refreshes the page after payment confirmation the stripeToken
            will be invalid and give an Invalid Request Error, this handles that exception
            gracefully without causing any issue for the user
            """
            pass

        # Any general errors not on stripe's end
        except:
            context["payment"] = 'error'
            context["payment_header"] = 'Error.'
            context["payment_message"] = "There was an error in processing your donation."

        return render(request, 'index.html', context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        context['dogs'] = Dog.objects.all().order_by('-pk')[:6]
        return context


class EventPageView(TemplateView):
    template_name = 'events.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['maps_key'] = settings.GOOGLE_MAPS_KEY
        return context

def test_user_login(request):
    """ Allows anonymous user login to demo site
    NOT TO BE USED IN PRODUCTION
    """
    user = authenticate(request, username='test', password='test1234!')
    if user is not None:
        #login the test user (pre-made in the admin)
        login(request, user)
        messages.success(request, 'Logged in as Test User')
    else:
        messages.error(request, 'Could not successfully log in')
    return redirect(reverse('home'))

