import datetime
from django.utils import timezone
from django.test import TestCase
from polls.models import Poll
from django.core.urlresolvers import reverse


def create_poll(question, days):
    """
    Create a poll with a given question published the given number of
    days offest to new(negetive for poll published in the past,
    positive for polls that have yet to be published)
    """
    return Poll.objects.create(question=question,
                               pub_date=timezone.now() + datetime.timedelta(days=days))


class PollViewTest(TestCase):
    def test_index_view_with_no_polls(self):
        """
        if no polls exists an appropriate message will be displayed
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Polls are available")
        self.assertQuerysetEqual(response.context['latest_poll_list'], [])

    def test_index_view_with_a_past_poll(self):
        """
        polls with a pub_date in the past will be displayed in the index page
        """

        create_poll(question="Past Poll", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_poll_list'], ['<Poll: past poll.>']
        )

# PollMethodTest is the subclass of django.test.TestCase
class PollMethodTest(TestCase):
    # For the test case, method names should be started with test
    def test_was_published_recently_with_future_poll(self):
        """
        Was published recently should return false
        for polls whose pub_date is in the future
        """

        # Created a Poll instance whose pub_date field in 30 day in the future.
        future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
        self.assertEqual(future_poll.was_published_recently(), False)

    def test_was_published_recently_with_old_poll(self):
        """
        was_published_recently() should return false for polls whose pub_date
        is older than one day
        """

        old_poll = Poll(pub_date=timezone.now() - datetime.timedelta(days=30))
        self.assertEqual(old_poll.was_published_recently(), False)

    def test_was_published_recently_with_recent_poll(self):
        """
        was_published_recently should return true for polls whose
        pub_date is within the last day
        """
        recent_poll = Poll(pub_date=timezone.now() - datetime.timedelta(hours=1))
        self.assertEqual(recent_poll.was_published_recently(), True)

