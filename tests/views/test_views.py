from unittest import TestCase
from app import app


class TestHome(TestCase):

## Home Test

    def test_home(self):
        with app.test_client() as c:
            resp = c.get('/')
            self.assertEqual(resp.status_code, 200)

# Dashboard Test

    def test_dashboard(self):
        with app.test_client() as c:
            response = c.get('/dashboard', content_type='html/text')
            self.assertEqual(response.status_code, 200)


# Login page loads correctly

    def test_login_page_loads(self):
        with app.test_client() as c:
            response = c.get('/login', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(b'Please Log in' in response.data)


# Ensure that title & default user shows on main page

    def test_title_shows_up(self):
        with app.test_client() as c:
            response = c.get('/dashboard')
            self.assertTrue(b'CHARACTERISE YOUR DATASET' in response.data)
            self.assertEqual(response.status_code, 200)

# Ensure that suggested algorithm table shows on add_request page

    def test_table_shows_up(self):
        with app.test_client() as c:
            response = c.get('/add_algorithm', follow_redirects=True)
            self.assertTrue(b'Algorithm Name' in response.data)
            self.assertTrue(b'Users already suggested' in response.data)
            self.assertEqual(response.status_code, 200)