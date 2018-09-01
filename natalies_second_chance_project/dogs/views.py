from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.urls import reverse_lazy

from .models import Dog
from .forms import DogCreateForm

import stripe
import json #Not used yet (Remove later if not needed)

stripe_api_key = settings.STRIPE_SECRET_KEY

class HomePageView(TemplateView):
    template_name = 'home.html'
    
    def post(self, request, **kwargs):
        context = self.get_context_data()
        post_data = self.request.POST
        token = self.request.POST.get('stripeToken', '')

        # Check for custom donation
        if post_data.get('custom-donation-option'):
            amount = float(post_data.get('custom-donation-option')) * 100 #convert donation to cents
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
    

class DogCreateView(LoginRequiredMixin, CreateView):
    model = Dog
    form_class = DogCreateForm

class DogListView(ListView):
    model = Dog
    template_name = "dogs/dog_list.html"
    context_object_name = 'dogs'
    paginate_by = 10 

class DogDetailView(DetailView):
    model = Dog
    template_name = 'dogs/dog_detail.html'

class DogUpdateView(LoginRequiredMixin, UpdateView):
    model = Dog
    fields = '__all__'
    template_name = "dogs/dog_form.html"

class DogDeleteView(LoginRequiredMixin, DeleteView):
    model = Dog
    template_name = "dogs/dog_delete.html"

