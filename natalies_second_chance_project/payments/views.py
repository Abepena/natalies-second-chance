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
        for key, value in post_data.items():
            print (f"{key}: {value}")
        if post_data.get('custom-donation-option'):
            amount = float(post_data.get('custom-donation-option')) *100 #convert donation to cents
        else:
            amount = post_data.get('donation-option', 500)
        try:
            # Create the stripe charge
            charge = stripe.Charge.create(
                amount=int(amount),
                currency='usd',
                description='Donation',
                source=token
                
            )
            context["valid_payment"] = 'success'

        except (stripe.error.CardError, stripe.error.InvalidRequestError) as e:
            context["valid_payment"] = 'error'

        return super().render_to_response(context)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

class ChargeView(TemplateView):
    template_name = 'payments/charge.html'
  
  
    # if request.method == "POST":
    #     token = request.POST.get('stripeToken', '')
    #     charge = stripe.Charge.create(
    #         amount =  request.POST.get('amount', 0), # maybe hardcode if it does work
    #         currency = 'usd',
    #         description = 'Donation',
    #         source = token
    #     )
    #     return render(request, 'payments/charge.html')
        