from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Hero
from .serializers import HeroSerializer


class HeroListCreateAPIViewTest(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('heroes')

    def test_get_heroes(self):
        hero_1 = Hero(name='Superman', alias='Kook')
        hero_2 = Hero(name='Ironman', alias='Haha')
        hero_1.save()
        hero_2.save()

        response = self.client.get(self.url)
        response_json = response.json()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response_json), 2)

        data = response_json[1]
        self.assertEquals(data['name'], hero_1.name)
        self.assertEquals(data['alias'], hero_1.alias)

    def test_post_hero(self):
        self.assertEquals(Hero.objects.count(), 0)
        data = {'name': 'Batman', 'alias': 'Gary'}

        response = self.client.post(self.url, data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Hero.objects.count(), 1)

        hero = Hero.objects.first()
        self.assertEquals(hero.name, data['name'])
        self.assertEquals(hero.alias, data['alias'])


class HeroDetailsAPIViewTest(APITestCase):
    def setUp(self) -> None:
        self.hero = Hero(name='Doreamon', alias='Mon')
        self.hero.save()
        self.url = reverse('hero-details', kwargs={'pk': self.hero.id})

    def test_get_hero_details(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertEquals(data['name'], str(self.hero.name))
        self.assertEquals(data['alias'], str(self.hero.alias))

    def test_update_hero(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        data = response.json()
        data['name'] = 'Doreami'
        data['alias'] = 'Mimi'
        response = self.client.put(self.url, data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.hero.refresh_from_db()
        self.assertEquals(self.hero.name, data['name'])
        self.assertEquals(self.hero.alias, data['alias'])

    def test_delete_hero(self):
        self.assertEquals(Hero.objects.count(), 1)

        response = self.client.delete(self.url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(Hero.objects.count(), 0)
