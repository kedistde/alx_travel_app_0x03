# listings/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@shared_task
def send_booking_confirmation_email(booking_id, user_email, user_name, listing_title, check_in, check_out):
    """
    Send booking confirmation email asynchronously
    """
    subject = f'Booking Confirmation - {listing_title}'
    
    # Create HTML email content
    context = {
        'user_name': user_name,
        'listing_title': listing_title,
        'check_in': check_in,
        'check_out': check_out,
        'booking_id': booking_id
    }
    
    html_message = render_to_string('listings/email/booking_confirmation.html', context)
    plain_message = strip_tags(html_message)
    
    try:
        send_mail(
            subject=subject,
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user_email],
            html_message=html_message,
            fail_silently=False,
        )
        return f"Email sent successfully to {user_email}"
    except Exception as e:
        return f"Failed to send email: {str(e)}"
