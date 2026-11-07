
import logging

from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.utils.html import escape

from .models import ContactInfo

logger = logging.getLogger(__name__)


def contact(request):
    contact_info = ContactInfo.objects.filter(
        is_active=True
    ).first()

    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()
        sender_email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        if not all([full_name, sender_email, subject, message]):
            messages.error(request, "Please fill in all fields.")

        else:
            try:
                validate_email(sender_email)

                if len(full_name) > 150 or len(subject) > 200:
                    raise ValueError("Input is too long.")

                admin_subject = f"New Portfolio Inquiry: {subject}"

                admin_text = f"""
You have received a new message through your portfolio.

SENDER DETAILS
Name: {full_name}
Email: {sender_email}
Subject: {subject}

MESSAGE
{message}

You can reply directly to this email to contact the sender.
"""

                safe_name = escape(full_name)
                safe_email = escape(sender_email)
                safe_subject = escape(subject)
                safe_message = escape(message).replace("\n", "<br>")

                admin_html = f"""
                <div style="background:#f4f6fb;padding:35px 15px;
                            font-family:Arial,sans-serif;">
                  <div style="max-width:620px;margin:auto;background:#ffffff;
                              border-radius:12px;overflow:hidden;
                              border:1px solid #e5e7eb;">
                    <div style="background:#101c35;padding:28px 32px;
                                color:#ffffff;">
                      <h2 style="margin:0;font-size:22px;">
                        New Portfolio Inquiry
                      </h2>
                      <p style="margin:8px 0 0;color:#cbd5e1;">
                        You have received a new message.
                      </p>
                    </div>
                    <div style="padding:30px 32px;color:#263247;">
                      <p><strong>Name:</strong> {safe_name}</p>
                      <p><strong>Email:</strong> {safe_email}</p>
                      <p><strong>Subject:</strong> {safe_subject}</p>
                      <hr style="border:0;border-top:1px solid #e5e7eb;">
                      <h3 style="font-size:16px;">Message</h3>
                      <p style="line-height:1.8;">{safe_message}</p>
                      <p style="margin-top:28px;color:#64748b;font-size:13px;">
                        Reply directly to this email to respond to the sender.
                      </p>
                    </div>
                    <div style="padding:18px 32px;background:#f8fafc;
                                color:#64748b;font-size:12px;">
                      Portfolio Contact Notification
                    </div>
                  </div>
                </div>
                """

                admin_email = EmailMultiAlternatives(
                    subject=admin_subject,
                    body=admin_text,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[settings.EMAIL_HOST_USER],
                    reply_to=[sender_email],
                )
                admin_email.attach_alternative(admin_html, "text/html")
                admin_email.send(fail_silently=False)

                # Send acknowledgement to the person who submitted the form.
                acknowledgement_subject = (
                    "We've received your message | Asfand Amjad"
                )

                acknowledgement_text = f"""
Hello {full_name},

Thank you for reaching out through my portfolio.

This is to confirm that I have successfully received your message
regarding: {subject}

I appreciate your interest. I will review your inquiry and get back
to you as soon as possible.

Best regards,
Asfand Amjad
"""

                acknowledgement_html = f"""
                <div style="background:#f4f6fb;padding:35px 15px;
                            font-family:Arial,sans-serif;">
                  <div style="max-width:620px;margin:auto;background:#ffffff;
                              border-radius:12px;overflow:hidden;
                              border:1px solid #e5e7eb;">
                    <div style="background:#101c35;padding:30px 32px;
                                color:#ffffff;">
                      <h2 style="margin:0;font-size:23px;">
                        Thank You for Reaching Out!
                      </h2>
                      <p style="margin:9px 0 0;color:#cbd5e1;">
                        Message successfully received
                      </p>
                    </div>
                    <div style="padding:32px;color:#263247;
                                line-height:1.8;">
                      <p>Hello {safe_name},</p>
                      <p>
                        Thank you for contacting me through my portfolio.
                        I appreciate you taking the time to reach out.
                      </p>
                      <div style="background:#f4f6fb;padding:16px 20px;
                                  border-radius:8px;margin:22px 0;">
                        <strong>Inquiry subject:</strong><br>
                        {safe_subject}
                      </div>
                      <p>
                        Your message has been successfully received.
                        I will review your inquiry and get back to you
                        as soon as possible.
                      </p>
                      <p>
                        Thank you for your patience.
                      </p>
                      <p style="margin-top:28px;">
                        Best regards,<br>
                        <strong>Asfand Amjad</strong><br>
                        Portfolio
                      </p>
                    </div>
                    <div style="padding:18px 32px;background:#f8fafc;
                                color:#64748b;font-size:12px;">
                      This is an automated confirmation email.
                      Please do not reply to this message.
                    </div>
                  </div>
                </div>
                """

                acknowledgement_email = EmailMultiAlternatives(
                    subject=acknowledgement_subject,
                    body=acknowledgement_text,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[sender_email],
                )
                acknowledgement_email.attach_alternative(
                    acknowledgement_html,
                    "text/html",
                )

                try:
                    acknowledgement_email.send(fail_silently=False)
                    messages.success(
                        request,
                        "Thank you! Your message has been received. "
                        "A confirmation email has been sent to your inbox."
                    )
                except Exception:
                    logger.exception("Portfolio acknowledgement email failed.")
                    messages.success(
                        request,
                        "Your message was received successfully. "
                        "However, we could not send the confirmation email."
                    )

            except ValidationError:
                messages.error(
                    request,
                    "Please enter a valid email address."
                )
            except ValueError:
                messages.error(
                    request,
                    "Please check your name and subject lengths."
                )
            except Exception:
                logger.exception("Portfolio contact email failed.")
                messages.error(
                    request,
                    "Sorry, your message could not be sent. "
                    "Please try again later."
                )

    context = {
        "contact_info": contact_info,
    }

    return render(request, "contact/contact.html", context)
