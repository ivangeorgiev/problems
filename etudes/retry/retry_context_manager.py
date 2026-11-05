import time
from collections.abc import Iterable
from functools import wraps


class Retry:
    def __init__(
        self,
        timeout: float,
        supress: Exception | Iterable[Exception] | None = None,
        interval: float = 0,
    ):
        self.timeout = timeout
        self.deadline = None
        self.interval = interval
        self.attempts = 0

        if supress is None:
            self.supress = Exception
        elif isinstance(supress, Iterable):
            self.supress = tuple(supress)
        else:
            self.supress = (supress,)
        self.supress = supress

    def run(self, fn, *args, **kwargs):
        deadline = self.deadline or time.monotonic() + self.timeout
        last_exc = None

        while time.monotonic() < deadline:
            self.attempts += 1
            try:
                return fn(*args, **kwargs)
            except self.supress as exc:
                last_exc = exc
                if self.interval:
                    time.sleep(self.interval)
        raise TimeoutError(
            f"{fn.__name__} did not succeed within {self.timeout}s"
        ) from last_exc

    def __enter__(self):
        self.deadline = time.monotonic() + self.timeout
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def __call__(self, fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            return self.run(*args, **kwargs)

        return wrapper


if __name__ == "__main__":
    import random

    def f1(n, exc_type=RuntimeError):
        if random.randint(0, 100) > n:
            raise exc_type("No luck")
        time.sleep(2)

    with Retry(4, ValueError) as retry:
        retry.run(f1, 1, ValueError)
    print(f"Finished with {retry.attempts} attempts.")
