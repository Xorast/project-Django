from django.test import TestCase

# Create your tests here.
class TestViewsViews(TestCase):
    
    def test_index_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "views/index.html")
        
    def test_about_page(self):
        page = self.client.get("/about")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "views/about.html")