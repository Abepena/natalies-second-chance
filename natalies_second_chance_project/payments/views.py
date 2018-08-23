from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings

import stripe
import json
import logging

logger = logging.getLogger(__name__)

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY

class HomePageView(TemplateView):
    template_name = 'index.html'

    def post(self, request, **kwargs):
        context = self.get_context_data()
        post_data = self.request.POST
        token = self.request.POST.get('stripeToken', '')

        # Check for custom donation
        if post_data.get('custom-donation-option'):
            amount = float(post_data.get('custom-donation-option')) *100 #convert donation to cents
        else:
            amount = post_data.get('donation-option', 500) #Defaults to $5.00 if the donation amount never changed
        
        try:
            # Create the stripe charge
            charge = stripe.Charge.create(
                amount=int(amount), #convert to integer of cents in USD
                currency='usd',
                description='Donation',
                source=token
                
            )
            context["amount"] = int(amount) / 100 # back to float for context
            context["payment"] = 'success'
            context["payment_header"] = 'Success!'
            context["payment_message"] = "Congratulate yourself on being awesome!<br>We appreciate your generosity."



        except stripe.error.CardError:
            context["payment"] = 'declined'
            context["payment_header"] = 'Payment Method Declined.'
            context["payment_message"] = "There was an error in proccessing your card"
            
        
        except stripe.error.InvalidRequestError:
            """
            If a user refreshes the page after payment confirmation the stripeToken
            will be invalid and give an Invalid Request Error, this handles that exception
            gracefully without causing any issue for the user
            """
            pass
        
        #Any general errors not on stripe's end
        except:
            context["payment"] = 'error'
            context["payment_header"] = 'Error.'
            context["payment_message"] = "There was an error in processing your donation."

               
        return render(request, 'index.html', context)
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

  
  
    # if request.method == "POST":
    #     token = request.POST.get('stripeToken', '')
    #     charge = stripe.Charge.create(
    #         amount =  request.POST.get('amount', 0), # maybe hardcode if it does work
    #         currency = 'usd',
    #         description = 'Donation',
    #         source = token
    #     )
    #     return render(request, 'payments/charge.html')
        