import stripe
from django.http import HttpResponse

def stripe_webhook(request):
    payload = request.body
    # Logic to catch 'customer.subscription.created'
    # Automatically upgrade the user's role in Django
    return HttpResponse(status=200)