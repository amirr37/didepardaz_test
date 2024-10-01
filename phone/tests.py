from django.test import TestCase
from django.urls import reverse
from phone.models import Country, Brand, Phone
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User


class PhoneViewsTest(TestCase):

    def setUp(self):
        self.country = Country.objects.create(name='Korea')
        self.brand = Brand.objects.create(title='Samsung', country=self.country)
        self.phone = Phone.objects.create(
            model='Galaxy S21', brand=self.brand, price=1000, color='Black', screen_size=6.2,
            origin_country=self.country
        )
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_index_view(self):
        response = self.client.get(reverse('phone:index-page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'phone/index.html')

    def test_create_phone_view_get(self):
        # User needs to log in to access this view
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('phone:create-phone'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'phone/create_phone.html')

    def test_update_phone_view_get(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('phone:update-phone', args=[self.phone.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'phone/update_phone.html')

    def test_delete_phone_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('phone:delete-phone', args=[self.phone.id]))
        self.assertRedirects(response, reverse('phone:index-page'))
        phone = Phone.objects.get(id=self.phone.id)
        self.assertFalse(phone.is_active)

    def test_update_phone_view_post(self):
        self.client.login(username='testuser', password='12345')

        updated_data = {
            'model': 'Galaxy S21 Ultra',
            'brand': self.phone.brand.id,
            'screen_size': 6.7,
            'origin_country': self.phone.origin_country.id,
            'in_stock': True
        }

        response = self.client.post(reverse('phone:update-phone', args=[self.phone.id]), data=updated_data)

        self.assertRedirects(response, reverse('phone:index-page'))
        updated_phone = Phone.objects.get(id=self.phone.id)
        self.assertEqual(updated_phone.model, 'Galaxy S21 Ultra')
        self.assertEqual(updated_phone.price, 1200)
        self.assertEqual(updated_phone.color, 'White')
        self.assertEqual(updated_phone.screen_size, 6.70)


class PhoneAPITest(APITestCase):

    def setUp(self):
        # Create test data for Country, Brand, and Phone
        self.country_korea = Country.objects.create(name='Korea')
        self.country_usa = Country.objects.create(name='USA')
        self.brand_samsung = Brand.objects.create(title='Samsung', country=self.country_korea)
        self.brand_apple = Brand.objects.create(title='Apple', country=self.country_usa)
        self.phone_samsung = Phone.objects.create(
            model='Galaxy S21', brand=self.brand_samsung, price=1000, color='Black', screen_size=6.2,
            origin_country=self.country_korea
        )
        self.phone_apple = Phone.objects.create(
            model='iPhone 12', brand=self.brand_apple, price=1200, color='White', screen_size=6.1,
            origin_country=self.country_usa
        )
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    # Test KoreanBrandsAPIView
    def test_korean_brands(self):
        url = reverse('phone:report-korean-brands')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['brands'][0]['title'], 'Samsung')

    # Test PhoneOriginIsBrandCountryView
    def test_phone_origin_is_brand_country(self):
        url = reverse('phone:report-origin-brand-country')
        response = self.client.get(url)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['phones']), 2)  # we have 2 phones in phones of this response
        self.assertEqual(response.data['phones'][0]['model'], 'Galaxy S21')
        self.assertEqual(response.data['phones'][1]['model'], 'iPhone 12')

