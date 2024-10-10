def duplicata(nums):
    valores = []
    for num in nums:
        if num in valores:
            return True
        valores.append(num)
    return False

nums = [1,2,3]
print(duplicata(nums))
    