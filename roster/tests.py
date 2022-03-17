from django.test import TestCase
from django.shortcuts import get_object_or_404
from roster.models import RosterList
from django.contrib.auth.models import User


# Create your tests here.
class TestListRosters(TestCase):
    def test_testhomepage(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)


class TestPostRoster(TestCase):
    def test_testpostroster(self):
        response = self.client.get('/post-roster/')
        self.assertEqual(response.status_code, 302)


class TestRosterDetail(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='mark',
            email='mark@email.com',
            password='testpass1',
            )
        self.user2 = User.objects.create_user(
            username="harry",
            email='harry@email.com',
            password='testpass2',
            )
        RosterList.objects.create(
            id=1,
            name='Test Roster',
            points=2000,
            faction=1,
            created_by=self.user1,
            created_on='Feb. 18, 2022, 4:56 p.m',
            status=1,
        )
        roster_list = get_object_or_404(RosterList, pk=1)
        roster_list.list_comments.set([1, 2])
        roster_list.likes.set([1])
        roster_list.dislikes.set([2])

    def test_testrosterdetail(self):
        response = self.client.get('/roster/1/')
        self.assertEqual(response.status_code, 200)
