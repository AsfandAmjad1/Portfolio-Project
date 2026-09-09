from django.shortcuts import render
from .models import ContactInfo


def contact(request):
    contact_info = ContactInfo.objects.filter(
        is_active=True
    ).first()

    context = {
        "contact_info": contact_info,
    }

    return render(request, "contact/contact.html", context)