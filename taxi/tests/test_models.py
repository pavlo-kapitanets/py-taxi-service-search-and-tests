from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Manufacturer, Car


class ModelTests(TestCase):
    def test_manufacturer_str(self):
        manufacturer = Manufacturer.objects.create(name="BMW",
                                                   country="Germany")

        self.assertEqual(str(manufacturer),
                         f"{manufacturer.name} {manufacturer.country}")

    def test_driver_str(self):
        driver = get_user_model().objects.create_user(username="Test",
                                                      first_name="Test name",
                                                      last_name="Test surname")

        self.assertEqual(str(driver),
                         f"{driver.username} "
                         f"({driver.first_name} "
                         f"{driver.last_name})")

    def test_car_str(self):
        manufacturer = Manufacturer.objects.create(name="TestName",
                                                   country="TestCountry")

        car = Car.objects.create(model="Test",
                                 manufacturer=manufacturer)

        self.assertEqual(str(car),
                         car.model)

    def test_create_driver_with_license_number(self):
        username = "Test"
        password = "test1234"
        license_number = "DHF12345"

        driver = get_user_model().objects.create_user(
            username=username,
            password=password,
            license_number=license_number)

        self.assertEqual(driver.username, username)
        self.assertTrue(driver.check_password(password))
        self.assertEqual(driver.license_number, license_number)