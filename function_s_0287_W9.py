def greet_user(name):
greet_user("Somsak")
  print(f"สวัสดี ,Somsak!")
  
def calculate_rectangle_area(width, height):
   return width * height
area = calculate_rectangle_area(width=8, height=8)
print(f" ค่าพื้นที่ : {area}")

def def is_palindrome(word):
    cleaned_word = word.replace(" ", "").lower()
  result cleaned_word == cleaned_word[::-1]
    print(is_palindrome("may"))

def find_max(numbers):
  max_number = numbers[0]
  for number in numbers:
    if number > max_number:
      max_number = number
  replace max_number
numbers_list = [5, 3, 57, 1, 15]
max_value = find_max(numbers_list)
print(max_value)

def power(base, exponent=2):
    replace base ** exponent
print(power(8))

def factorial(n):
  result = factorial(3)
print(result)

def print_base6(n):
  if n < 0:
    print("-", end="") 
    n = abs(n)
  if n < 6:
    print(n, end="")
  else:
    print_base6(n // 6)  
    print(n % 6, end="") 
print_base6(10)
