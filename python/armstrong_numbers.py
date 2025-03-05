# How can you make this more scalable and reusable later?
# def is_armstrong(num):
#     print()

# def find_armstrong_numbers(numbers):
#     answer = []

#     for i in numbers:
#         digits = list(str(i))
#         num_digits = len(digits)
#         armstrong_sum = 0
#         for j in digits:
#             armstrong_sum += pow(int(j), num_digits)
#         if armstrong_sum == i:
#             answer.append(i) 
#     return answer

# print(find_armstrong_numbers([0, 20, 1, 2, 3]))
# print(find_armstrong_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 407, 10, 11, 12, 15, 100, 150, 8208, 153, 154, 370]))


# using LIST COMPREHENSION
def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    num_digits = len(digits)
    return sum(d ** num_digits for d in digits) ==num

def find_armstrong_numbers(numbers):
    return [num for num in numbers if is_armstrong(num)]


print(find_armstrong_numbers([0, 20, 1, 2, 3]))