"""
Tests for the user-facing web routes in web_routes.py
"""

def test_show_books_page_loads_successfully(client):
     """
     GIVEN a Flask application configured for testing
     WHEN the '/show-books' page is requested (GET)
     THEN check the response is valid and contains the expected content
     """
     # ACT
     response = client.get("/show-books")

     # ASSERT
     assert response.status_code == 200

     # Assert that the content of the response contains key text from the template
     # use `b` prefix on check string as `response.data` is a bytestring
     assert b"Available Books" in response.data
     assert b"Loading book count..." in response.data
     assert b"Loading books..." in response.data
     assert b"Loading pagination..." in response.data
