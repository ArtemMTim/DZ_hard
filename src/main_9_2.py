def strings_a_a(strings: list[str]) -> list[str]:
    """Функция принимает список строк и возвращает список строк,
    у которых первая и последняя буквы одинаковые"""
    return [word for word in strings if word == "" or word[0] == word[-1]]


def max_multy(nums: list[int]) -> int:
    """Функция принимает список целых чисел и возвращает максимальное произведение двух из переданных чисел.
    Если в списке меньше 2 чисел, возвращает 0."""
    if len(nums) >= 2:
        return max([nums[i] * nums[j] for i in range(len(nums) - 1) for j in range(1, len(nums))])
    else:
        return 0
