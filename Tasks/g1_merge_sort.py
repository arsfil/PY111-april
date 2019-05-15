from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with merge sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	def merge(left, right):
		left = right = 0
		list = []
		left_len, right_len = len(left), len(right)
		for i in range(left_len + right_len):
			if
	if len(container) <= 1:
		return container
	Halve = len(container)//2
	left = sort(container[:Halve])
	right = sort(container[Halve:])
	return container(left, right)
