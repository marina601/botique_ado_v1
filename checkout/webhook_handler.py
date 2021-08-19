from django.http import HttpResponse


class StripeWH_Handler:
    """
    Handle Stripe Webhooks
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandle webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Payment failed Webhook received: {event["type"]}',
            status=200
        )
