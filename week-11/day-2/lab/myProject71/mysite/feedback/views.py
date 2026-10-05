from django.shortcuts import render, redirect
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('feedback:thank_you')
        # Mark every invalid field so the template can render it with the
        # is-invalid CSS class (red border) instead of using {{ form.as_p }}.
        for field_name in form.errors:
            form.fields[field_name].widget.attrs['class'] = 'is-invalid'
    else:
        form = ContactForm()

    return render(request, 'feedback/contact.html', {'form': form})


def thank_you(request):
    return render(request, 'feedback/thank_you.html')