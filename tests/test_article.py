from tests import client


def test_create_and_get_article():
    response = client.post(
        "/authors/",
        json={"id": 1, "first_name": "foo", "last_name": "bar"},
    )

    response = client.post(
        "/articles/",
        json={"id": 1, "title": "foo", "text": "bar", "image": "img", "is_publish": False, "author_id": 1},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "foo"
    assert data["is_publish"] == False
    assert "id" in data
    article_id = data["id"]

    response = client.get(f"/articles/{article_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "foo"
    assert data["is_publish"] == False


def test_create_and_update_article():
    response = client.post(
        "/authors/",
        json={"id": 1, "first_name": "foo", "last_name": "bar"},
    )

    response = client.post(
        "/articles/",
        json={"id": 1, "title": "foo", "text": "bar", "image": "img", "is_publish": False, "author_id": 1},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "foo"
    assert data["is_publish"] == False
    assert "id" in data
    article_id = data["id"]

    response = client.patch(
        "/articles/",
        json={"id": article_id, "title": "foo_update", "text": "bar", "image": "img", "is_publish": True, "author_id": 1},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "foo_update"
    assert data["is_publish"] == True


def test_create_and_delete_article():
    article_id = 1
    response = client.post(
        "/authors/",
        json={"id": 1, "first_name": "foo", "last_name": "bar"},
    )

    response = client.post(
        "/articles/",
        json={"id": 1, "title": "foo", "text": "bar", "image": "img", "is_publish": False, "author_id": 1},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "foo"
    assert data["is_publish"] == False
    assert "id" in data
    article_id = data["id"]

    response = client.delete(
        f"/articles/{article_id}",
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data == True