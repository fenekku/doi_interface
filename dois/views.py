from django.shortcuts import render
from crossref.restful import Works


def index(request):
    return render(request, "dois/main.html")

def get_doi(request, doi):
    works = Works()
    result = works.doi(doi)
    context = {"doi": result} if result else {}
    return render(request, "dois/main.html", context)

def fake_doi(request):
    # Just a quick way to test the main.html without having to call crossref everytime
    result = {'deposited': {'timestamp': 1495591046000, 'date-parts': [[2017, 5, 24]], 'date-time': '2017-05-24T01:57:26Z'}, 'volume': '32', 'issued': {'date-parts': [[2016, 11]]}, 'references-count': 3, 'short-container-title': ['Cad. Saúde Pública'], 'reference-count': 3, 'published-print': {'date-parts': [[2016, 11]]}, 'subject': ['Public Health, Environmental and Occupational Health'], 'content-domain': {'domain': [], 'crossmark-restriction': False}, 'ISSN': ['0102-311X'], 'member': '530', 'issue': '11', 'publisher': 'FapUNIFESP (SciELO)', 'DOI': '10.1590/0102-311x00133115', 'indexed': {'timestamp': 1509131823205, 'date-parts': [[2017, 10, 27]], 'date-time': '2017-10-27T19:17:03Z'}, 'reference': [{'key': 'ref1', 'year': '2016', 'author': 'Eickmann SH', 'volume': '32', 'article-title': 'Zika virus congenital syndrome', 'journal-title': 'Cad Saúde Pública'}, {'key': 'ref2', 'year': '2016', 'volume': '6', 'author': 'San K', 'first-page': '37', 'article-title': 'Seroprevalence of Zika virus in Cambodia a preliminary report', 'journal-title': 'Advance Laboratory Medicine International'}, {'key': 'ref3', 'doi-asserted-by': 'crossref', 'year': '2016', 'author': 'Miranda-Filho DB', 'volume': '106', 'first-page': '598', 'article-title': 'Initial description of the presumed congenital zika syndrome', 'journal-title': 'Am J Public Health', 'DOI': '10.2105/AJPH.2016.303115'}], 'is-referenced-by-count': 0, 'issn-type': [{'value': '0102-311X', 'type': 'electronic'}], 'prefix': '10.1590', 'source': 'Crossref', 'container-title': ['Cadernos de Saúde Pública'], 'relation': {'cites': []}, 'URL': 'http://dx.doi.org/10.1590/0102-311x00133115', 'title': ['Congenital Zika virus syndrome'], 'alternative-id': ['S0102-311X2016001107002'], 'type': 'journal-article', 'score': 1.0, 'link': [{'content-type': 'unspecified', 'intended-application': 'similarity-checking', 'content-version': 'vor', 'URL': 'http://www.scielo.br/pdf/csp/v32n11/1678-4464-csp-32-11-e00133116.pdf'}], 'journal-issue': {'issue': '11'}, 'original-title': [], 'subtitle': [], 'created': {'timestamp': 1481147528000, 'date-parts': [[2016, 12, 7]], 'date-time': '2016-12-07T21:52:08Z'}, 'short-title': []}
    context = {'doi': result}
    return render(request, "dois/main.html", context)
