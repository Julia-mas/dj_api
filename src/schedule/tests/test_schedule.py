import json

from django.test import TestCase
from rest_framework import status

from rest_framework.test import APIRequestFactory, APIClient

from ..models import Schedule

from ..views import ScheduleView


class ApiPageTest(TestCase):
    def test_schedule_loads(self):
        """The schedule api page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/api/schedule/')
        self.assertEqual(response.status_code, 200)


class ViewSetTest(TestCase):

    def test_view_set(self):
        """The ScheduleView works properly"""
        request = APIRequestFactory().get("")
        schedule_list = ScheduleView.as_view({'get': 'retrieve'})
        task = Schedule.objects.create(task_name="Task_Test")
        response = schedule_list(request, pk=task.pk)
        self.assertEqual(response.status_code, 200)

    def test_schedule_create(self):
        data = json.dumps({
            "task_name": "Task 1",
            "description": "Test Task 1"
        })
        client = APIClient()
        response = client.post('/api/schedule/schedule_list/', data=data, content_type='application/json')
        # Check if you get a 201 back:
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Check to see if Schedule was created
        self.assertEqual(response.data['task_name'], 'Task 1')
