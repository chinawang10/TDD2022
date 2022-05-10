from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page #(2)

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')
    #def test_root_url_resolve_to_home_page_view(self):
     #  found = resolve('/') #(1)
      # self.assertEqual(found.func, home_page) #(1)
       
    #def test_home_page_returns_correct_html(self):
     #   response = self.client.get('/') #1
        
      #  html = response.content.decode('utf8') # 2
       # self.assertTrue(html.startswith('<html>')) 
        #self.assertIn('<title>To-Do lists</title>',html) 
        #self.assertTrue(html.strip().endswith('</html>'))
        
       # self.assertTemplateUsed(response, 'home.html')

