import re
from collections import Counter
import random
import psycopg2

# Sample data extracted from the web page
data = """
MONDAY GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN
TUESDAY ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE
WEDNESDAY GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE
THURSDAY BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN
FRIDAY GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE
"""

# 1. Which color of shirt is the mean color?
colors = re.findall(r'\b\w+\b', data)
mean_color = max(set(colors), key=colors.count)
print("Mean color:", mean_color)

# 2. Which color is mostly worn throughout the week?
most_common_color = Counter(colors).most_common(1)[0][0]
print("Most worn color throughout the week:", most_common_color)

# 3. Which color is the median?
sorted_colors = sorted(colors)
median_index = len(sorted_colors) // 2
median_color = sorted_colors[median_index]
print("Median color:", median_color)

# 4. BONUS Get the variance of the colors
variance = len(set(colors))
print("Variance of colors:", variance)

# 5. BONUS if a colour is chosen at random, what is the probability that the color is red?
red_probability = colors.count("RED") / len(colors)
print("Probability of choosing red color at random:", red_probability)

# 6. Save the colours and their frequencies in PostgreSQL database

conn = psycopg2.connect(
    dbname="your_database",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
    )
cur = conn.cursor()
color_counts = Counter(colors)
for color, count in color_counts.items():
    cur.execute("INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s)", (color, count))
conn.commit()
conn.close()


# 7. BONUS write a recursive searching algorithm to search for a number entered by user in a list of numbers.
def recursive_search(arr, target, start=0):
    if start >= len(arr):
        return -1
    if arr[start] == target:
        return start
    return recursive_search(arr, target, start + 1)

# 8. Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.
random_number = ''.join([str(random.randint(0, 1)) for _ in range(4)])
base_10 = int(random_number, 2)
print("Random 4-digit number in base 2:", random_number)
print("Converted to base 10:", base_10)

# 9. Write a program to sum the first 50 fibonacci sequence.
def fibonacci_sum(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return sum(fib)

print("Sum of the first 50 Fibonacci sequence:", fibonacci_sum(50))
