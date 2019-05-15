from typing import Collection, TypeVar
from random import choice

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with quick sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	# if len(container) <= 1:
	# 	return container
	# N = choice(container)
	# left = [i for i in container if i < N]
	# mid = [i for i in container if i == N]
	# right = [i for i in container if i > N]
	# return sort(left) + mid + sort(right)
	def quick_sort(low, high, container):
		block = container[(low+high)//2]
		i = low - 1
		j = high + 1
		while i < j:

			while container[i] < block:
				i += 1
			while container[j] > block:
				j -= 1


	return container
