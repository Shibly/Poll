from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from polls.models import Choice, Poll, ContactForm
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """
        Returns the last five published polls
        """
        return Poll.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Poll
    # Tells django to use a specific template name instead of the auto generated default template name
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'


def about(request):
    return render(request, 'polls/about.html')


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            recipient = ['shibly.phy@gmail.com']
            if cc_myself:
                recipient.append(sender)
            from django.core.mail import send_mail

            send_mail(subject, message, sender, recipient)
            return HttpResponseRedirect('/thanks/') # Redirect after post
    else:

        # Dynamic initial values.
        form = ContactForm(initial={'sender': 'shibly.phy@gmail.com'})
    return render(request, 'polls/contact.html', {'form': form})

