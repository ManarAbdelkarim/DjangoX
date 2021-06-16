from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Anime
from django.test import TestCase, override_settings
@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')

# Create your tests here.

class AnimeTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
             username="maro",
             email="maro@gmail.com", 
             password="1234"
        )

        self.anime = Anime.objects.create(
            title="Attack on Titans", author=self.user, description="the greatest anime of all time", image = None,
        )
    
    def test_string_representation(self):
        self.assertEqual(str(self.anime), "Attack on Titans")

    def test_anime_content(self):
        self.assertEqual(f"{self.anime.title}", "Attack on Titans")
        self.assertEqual(f"{self.anime.author}", "maro@gmail.com")
        self.assertEqual(f"{self.anime.description}","the greatest anime of all time")



    def test_anime_list_view(self):
        response = self.client.get(reverse("anime_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Attack on Titans")
        self.assertTemplateUsed(response, "anime/anime_list.html")

    def test_anime_detail_view(self):
        response = self.client.get(reverse("anime_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, "anime/anime_detail.html")

    def test_anime_create_view(self):
        response = self.client.post(
            reverse("anime_create"),
            {
                "title": "code geass",
                "author": self.user.id,
                "description": "an awesome anime series",
            }, follow=True
        )

        # self.assertRedirects(response, reverse("anime_detail", args="2"))
        # self.assertEqual(response.status_code, 200)
        # self.assertContains(response, "code geass")


    # def test_anime_update_view_redirect(self):
    #     response = self.client.post(
    #         reverse("anime_update", args="1"),
    #         {"name": "black clover"}
    #     )

    #     self.assertRedirects(response, reverse("anime_detail", args="1"))

    def test_anime_delete_view(self):
        response = self.client.get(reverse("anime_delete", args="1"))
        self.assertEqual(response.status_code, 200)