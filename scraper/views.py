from rest_framework.decorators import api_view

from libs.custom_response import custom_response
from bs4 import BeautifulSoup
import requests

from libs.string import anime_info_changer, anime_slug_changer


# Create your views here.
@api_view(['GET'])
def get_all(request):
    page = request.query_params.get('page')
    filter_by = request.query_params.get('filter_by')
    
    url = 'https://otakudesu.watch/'
    
    if filter_by == 'on-going':
        url = f'https://otakudesu.watch/ongoing-anime/page/{page}'
    if filter_by == 'complete':
        url = f'https://otakudesu.watch/complete-anime/page/{page}'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    parent = soup.select('#venkonten > div > div.venser > div.venutama > div > div.rapi > div > ul > li > div.detpost')

    data = [{'anime_title': pr.find(class_="jdlflm").text, 'anime_episode': (pr.find(class_="epz").text).lstrip(), 'img_url': pr.find(class_="attachment-thumb size-thumb wp-post-image")['src'], 'slug': anime_slug_changer(pr.find("a")["href"]).rstrip('/')} for pr in parent]

    return custom_response(data)

@api_view(['GET'])
def get_by_slug(request, slug):
    url = f'https://otakudesu.watch/anime/{slug}/'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    parent = soup.select('#venkonten > div.venser')
    for pr in parent:
        data = {
        'anime_title': anime_info_changer((pr.select("div.infozin > div > p:nth-child(1)"))[0].find('span').text),
        'score': anime_info_changer((pr.select("div.infozin > div > p:nth-child(3)"))[0].find('span').text),
        'img_url': pr.find("img")["src"],
        'producer': anime_info_changer((pr.select("div.infozin > div > p:nth-child(4)"))[0].find('span').text),
        'status': anime_info_changer((pr.select("div.infozin > div > p:nth-child(6)"))[0].find('span').text),
        'total_episode': anime_info_changer((pr.select("div.infozin > div > p:nth-child(7)"))[0].find('span').text),
        'duration': anime_info_changer((pr.select("div.infozin > div > p:nth-child(8)"))[0].find('span').text),
        'release_date': anime_info_changer((pr.select("div.infozin > div > p:nth-child(9)"))[0].find('span').text),
        'studio': anime_info_changer((pr.select("div.infozin > div > p:nth-child(10)"))[0].find('span').text),
        'genre': anime_info_changer((pr.select("div.infozin > div > p:nth-child(11)"))[0].find('span').text),
        'episode_list': [{
            'episode_title': ep.find('a').text,
            'episode_release_date': ep.find(class_='zeebr').text,
            'episode_slug': anime_slug_changer(ep.find('a')['href'])
        } for ep in soup.select('#venkonten > div.venser > div:nth-child(8) > ul > li')]
    }

    return custom_response(data)

@api_view(['GET'])
def get_stream_by_slug(request, slug):
    url = f'https://otakudesu.watch/episode/{slug}/'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    parent = soup.select('#venkonten > div.venser > div.venutama')
    
    for pr in parent:
        data = {
        'anime_title': pr.find(class_='posttl').text,
        'stream_url': pr.find('iframe')['src'],
        'next_episode': None if not pr.find('a', {'title':'Episode Selanjutnya'}) else anime_slug_changer(pr.find('a', {'title':'Episode Selanjutnya'})['href']),
        'prev_episode': None if not pr.find('a', {'title':'Episode Sebelumnya'}) else anime_slug_changer(pr.find('a', {'title':'Episode Sebelumnya'})['href'])
    }

    return custom_response(data)