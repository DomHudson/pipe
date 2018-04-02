import pytest
import pipe


def test_results_returned():
    """ Ensure results are actually returned.

    :raises AssertionError
    :return void
    """
    assert len(list(pipe.Pipe().run(range(5), lambda x: x))) == 5


def test_order_retained():
    """ Ensure results are remain in the correct order.

    :raises AssertionError
    :return void
    """
    assert list(pipe.Pipe().run(range(5), lambda x: x)) == list(range(5))


def test_exceptions():
    """ Ensure exceptions are raised in the main thread if 
    a job raises one.

    :raises AssertionError
    :return void
    """
    def work(item):
        raise Exception

    with pytest.raises(Exception):
        list(pipe.Pipe().run(range(5), work))


def test_exception_handler():
    """ Ensure exceptions are provided to the handler if one
    exists

    :raises AssertionError
    :return void
    """
    def work(item):
        raise Exception

    def handler(e):
        pass

    assert not bool(list(pipe.Pipe(
        exception_handler = handler
    ).run(range(5), work)))


def test_post_results():
    """ Ensure exceptions are provided to the handler if one
    exists

    :raises AssertionError
    :return void
    """
    def work(item):
        return item

    def processor(item):
        return item ** 2

    results = list(pipe.Pipe(
        post_processor = processor
    ).run(range(5), work)) == [0, 1, 4, 9, 16, 25]