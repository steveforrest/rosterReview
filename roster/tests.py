from django.test import TestCase

# Create your tests here.

class TestListRosters(TestCase):
    def test_testhomepage(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

class TestPostRoster(TestCase):
    def test_testpostroster(self):
        response = self.client.get('/post-roster/')
        self.assertEqual(response.status_code, 200)


class TestRosterDetail(TestCase):
    def setUpRoster(self):
        RosterList.objects.create(
            id = 1,
            name = 'Test Roster',
            points = 2000,
            faction = 1,
            createdBy = 'Test Author',
            createdOn = 'Feb. 18, 2022, 4:56 p.m',
            comments = 'Test comment',
            Likes = 7,
            Dislikes = 4,
            status = 1,
        )

    def test_testrosterdetail(self):
        response = self.client.get('<int:id>/details/')
        self.assertEqual(response.status_code, 200)


