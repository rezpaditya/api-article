from tests import client


def test_create_and_get_author():
    response = client.post(
        "/authors/",
        json={"id": 1, "first_name": "foo", "last_name": "bar"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["first_name"] == "foo"
    assert data["last_name"] == "bar"
    assert "id" in data
    author_id = data["id"]

    response = client.get(f"/authors/{author_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["first_name"] == "foo"
    assert data["last_name"] == "bar"
    assert data["id"] == author_id


def test_create_and_update_author():
    response = client.post(
        "/authors/",
        json={"id": 1, "first_name": "foo", "last_name": "bar"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["first_name"] == "foo"
    assert data["last_name"] == "bar"

    response = client.patch(
        "/authors/",
        json={"id": 1, "first_name": "foo_updated", "last_name": "bar_updated"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["first_name"] == "foo_updated"
    assert data["last_name"] == "bar_updated"


def test_create_and_delete_author():
    author_id = 1
    response = client.post(
        "/authors/",
        json={"id": author_id, "first_name": "foo", "last_name": "bar"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["first_name"] == "foo"
    assert data["last_name"] == "bar"

    response = client.delete(
        f"/authors/{author_id}",
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data == True