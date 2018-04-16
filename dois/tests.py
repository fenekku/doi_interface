from django.test import TestCase


class ViewTests(TestCase):

    def test_valid_doi(self):
        response = self.client.get(reverse('doi_enpoint'), data={'doi':'10.1590/0102-311x00133115'})

        assert response['DOI'] == '10.1590/0102-311x00133115'
        assert response['score'] == 1.0

    def test_invalid_doi(self):
        response = self.client.get(reverse('doi_enpoint'), data={'doi':''})

        assert response == {}
        # assert response['DOI'] == '10.1590/0102-311x00133115'
        # assert response['score'] == 1.0
