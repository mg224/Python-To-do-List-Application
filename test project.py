from project import add, edit, delete


def main():
    test_add()
    test_delete()
    test_edit


def test_add(monkeypatch):
    #use monkeypatch to test dynamic object
    monkeypatch.setattr("builtins.input", lambda _: "clean room")
    task_list, total_tasks = add([], 0)
    assert task_list == [{"#": 1, "Task": "clean room"}] and total_tasks == 1


def test_delete(monkeypatch):
    #use monkeypatch to test dynamic object
    monkeypatch.setattr("builtins.input", lambda _: "1")
    data = delete([{"#": 1, "Task": "clean room"}])
    assert data == []
    

def test_edit(monkeypatch):
    #use monkeypatch to test dynamic object
    inputs = iter(["1", "finish homework"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    data = edit([{"#": 1, "Task": "clean room"}])
    assert data == [{"#": 1, "Task": "finish homework"}]

if __name__ == "__main__":
    main()
