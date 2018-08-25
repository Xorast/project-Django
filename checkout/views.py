# from django.contrib.auth.decorators     import login_required
# from django.shortcuts                   import render, redirect, get_object_or_404
# from django.contrib                     import messages
# from django.http                        import HttpResponse, HttpResponseForbidden
# from django.conf                        import settings
# from django.utils                       import timezone
# from activities.models                  import Event, EventRegistration
# from .models                            import RegistrationOrder
# from .forms                             import MakePaymentForm
# from .utils                             import charge_card

# import stripe


# @login_required
# def register_confirm_request(request, event_type, event_subtype, event_id):
    
#     event   = get_object_or_404(Event, pk=event_id)
#     ER      = EventRegistration(participant=request.user,event=event)
    
#     if event.number_available > 0 :
    
#         try:
#             # Constraint on the model : user / event combination must be unique
#             # If the user is already registered : will throw an error
#             ER.save()
    
#             event.number_available += -1
#             event.save()
            
#         except:
#             error = "E01"
#             return render(request, "activities/event_registration_request_failed.html", {"error":error})
    
#     else:
#         error = "E02"
#         return render(request, "activities/event_registration_request_failed.html", {"error":error})
        
#     return render(request, "activities/event_registration_request_successful.html")
    


# @login_required
# def checkout(request):
    
#     if request.method == "POST":
            
#         id      = request.POST["event_id"]
#         event   = get_object_or_404(Event, pk=id)

#         payment_form    = MakePaymentForm()
            
#         return render(request, "checkout/checkout.html", {'event': event, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE_KEY })
        
#     else:
        
#         return HttpResponseForbidden() 



# @login_required
# def payment(request):
    
#     if request.method == "POST":
        
#         user                 = request.user
#         id                   = request.POST["event_id"]
#         event                = get_object_or_404(Event, pk=id)
#         total                = event.rate * 1 #include User Profile rate_coefficient
        
#         payment_form         = MakePaymentForm(request.POST)
        
#         if payment_form.is_valid():
            
#             stripe_token        = payment_form.cleaned_data['stripe_id']
            
#             try:
                
#                 customer        = charge_card(stripe_token, total)
                
#             except stripe.error.CardError:
                
#                 # Check this page
#                 messages.error(request, "Your card was declined!")
#                 return render(request, "checkout/checkout.html")
                

#             if customer.paid:
                
#                 ER      = EventRegistration(participant=user,event=event)
#                 ER.save()
                
#                 event.number_available += -1
#                 event.save()
                
#                 registration_order   = RegistrationOrder(user=user, event=event, date=timezone.now(), paid_fare= total) 
#                 registration_order.save()
                
#                 # Rework this : the message is not displayed on the rendered page.
#                 # messages.error(request, "You have successfully paid")
        
#                 return render(request, "activities/event_registration_request_successful.html", {'event': event })
        
#         else:
            
#             # Debug ==> Rework real case
#             return HttpResponse("Try again ! =)")
            
        
        
#     else:
        
#         return HttpResponseForbidden()
    
    