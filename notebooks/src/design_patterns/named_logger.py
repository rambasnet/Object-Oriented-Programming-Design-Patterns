# class decorators
import logging
import time
from typing import Any, Callable
from functools import wraps

class NamedLogger:
		# configure logger
		logging.basicConfig(filename="demo.log",
      					format='%(asctime)s %(message)s',
               	filemode='w')

		def __init__(self, logger_name: str) -> None:
			# Create logger
			self.logger = logging.getLogger(logger_name)
			# Setting the threshold of logger to DEBUG
			self.logger.setLevel(logging.DEBUG)
				
		def __call__(
						self,
						function: Callable[..., Any]
		) -> Callable[..., Any]:
				@wraps(function)
				def wrapped_function(*args: Any, **kwargs: Any) -> Any:
						start = time.perf_counter()
						#print(start)
						try:
								result = function(*args, **kwargs)
								#print('result', result)
								μs = (time.perf_counter() - start) * 1_000_000
								self.logger.info(
										f"{function.__name__}, { μs:.1f}μs")
								return result
						except Exception as ex:
								μs = (time.perf_counter() - start) * 1_000_000
								self.logger.error(
										f"{ex}, {function.__name__}, { μs:.1f}μs")
								raise
				return wrapped_function


@NamedLogger("log4")
def test4(median: float, sample: float) -> float:
	return sample - median

if __name__ == "__main__":
	print(test4(5.0, 10.0))
