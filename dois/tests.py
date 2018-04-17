from django.test import TestCase
from django.urls import reverse


class ViewTests(TestCase):

    def test_fake_doi(self):
        # This just tests the context by using the canned DOI to not have to fetch again from server
        response = self.client.get(reverse('fake_doi_endpoint'))

        doi = response.context["doi"]
        assert doi['DOI'] == '10.1590/0102-311x00133115'
        assert doi['score'] == 1.0
        self.assertTemplateUsed(response, 'dois/main.html')

    def test_valid_doi(self):
        # This is NOT a unit test but rather a smoke test
        # Ideally we would annotate this to make it part of a separate test suite
        response = self.client.get(
            reverse('doi_endpoint', args=['10.1590/0102-311x00133115'])
        )

        doi = response.context["doi"]
        assert doi['DOI'] == '10.1590/0102-311x00133115'
        assert doi['score'] == 1.0
        self.assertTemplateUsed(response, 'dois/main.html')

    def test_invalid_doi(self):
        response = self.client.get(
            reverse('doi_endpoint', args=['not-a-real-doi'])
        )

        doi = response.context.get("doi", {})
        assert doi == {}

    def test_past_dois(self):
        # Test first visit with valid DOI
        # Note that using mocking would be ideal
        response = self.client.get(
            reverse('doi_endpoint', args=['10.1590/0102-311x00133115'])
        )
        assert response.context.get("past_dois", []) == []
        assert self.client.session.get("present_doi") == '10.1590/0102-311x00133115'

        # Test second visit with valid DOI
        response = self.client.get(
            reverse('doi_endpoint', args=['10.1016/s0305-9006(99)00007-0'])
        )

        assert response.context["past_dois"] == ['10.1590/0102-311x00133115']
        assert self.client.session.get("present_doi") == '10.1016/s0305-9006(99)00007-0'

        # Test third visit with invalid DOI
        response = self.client.get(
            reverse('doi_endpoint', args=['10.1016/s0305-9006(99)-invalid-doi'])
        )

        assert response.context["past_dois"] == ['10.1590/0102-311x00133115', '10.1016/s0305-9006(99)00007-0']
        assert self.client.session.get("present_doi") == '10.1016/s0305-9006(99)-invalid-doi'
