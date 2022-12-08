from app import getPairs, launchApp

list_test = [1,9,5,0,20,-4,12,16,7]
list_test_without_target = [1,7,8,14]
target_test = 12

result_test = [[-4, 16], [0, 12], [5, 7]]
result_test_empty = []

def test_get_pair_success():
    result = getPairs(list_test, target_test)
    assert result == result_test

def test_get_pair_empty():
    result = getPairs(list_test_without_target, target_test)
    assert result == result_test_empty

def test_launch_app_success():
    try:
        launchApp()
    except IOError:
        assert False, f"'Raised an exception with the file"
    except Exception as exc:
        assert False, f"'Raised an exception with the json {exc}"