from rest_framework import status
from rest_framework.test import APITestCase


class TicketTests(APITestCase):
    def test_get_tickets(self):
        response = self.client.get('/tickets/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_get_ticket(self):
        ticket_mock = {'description': 'Description test',
                       'subject': 'Subject test'}
        expected_ticket = self.client.post('/tickets/', ticket_mock, format='json')
        response = self.client.get('/tickets/{0}'.format(expected_ticket.data.get('id')))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_ticket.data)

    def test_get_ticket_not_found(self):
        response = self.client.get('/tickets/1')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_ticket(self):
        ticket_mock = {'description': 'Description test',
                       'subject': 'Subject test'}
        response = self.client.post('/tickets/', ticket_mock, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
        self.assertIn('created_at', response.data)
        self.assertGreater(response.data.items(), ticket_mock.items())

    def test_create_ticket_bad_request(self):
        ticket_mock = {'description': 'Description test'}
        response = self.client.post('/tickets/', ticket_mock, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('subject', response.data)

    def test_update_ticket(self):
        ticket_mock = {'description': 'Description test',
                       'subject': 'Subject test'}
        edited_ticket_mock = {'description': 'Edited description test',
                              'subject': 'Edited subject test'}
        ticket = self.client.post('/tickets/', ticket_mock, format='json')
        response = self.client.put('/tickets/{0}'.format(ticket.data.get('id')), edited_ticket_mock, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(response.data.items(), edited_ticket_mock.items())

    def test_update_ticket_bad_request(self):
        ticket_mock = {'description': 'Description test',
                       'subject': 'Subject test'}
        edited_ticket_mock = {'description': 'Edited description test'}
        ticket = self.client.post('/tickets/', ticket_mock, format='json')
        response = self.client.put('/tickets/{0}'.format(ticket.data.get('id')), edited_ticket_mock, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('subject', response.data)

    def test_update_ticket_not_found(self):
        edited_ticket_mock = {'description': 'Edited description test',
                              'subject': 'Edited subject test'}
        response = self.client.put('/tickets/1', edited_ticket_mock, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_ticket(self):
        ticket_mock = {'description': 'Description test',
                       'subject': 'Subject test'}
        ticket = self.client.post('/tickets/', ticket_mock, format='json')
        response = self.client.delete('/tickets/{0}'.format(ticket.data.get('id')))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_ticket_not_found(self):
        response = self.client.delete('/tickets/1')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
