# Laboratory 1: Python and Numerical Libraries

## Introduction
This report documents the solutions for the first laboratory session on Python and its numerical libraries, specifically focusing on basic data structures (lists, dictionaries) and the NumPy library. The assignment consists of eight exercises ranging from file parsing to matrix operations and simulations.

## Exercise 1: Gymnastic Event Scores (Pure Python)
The objective of this exercise is to process a file containing artistic gymnastics event scores. The program computes the final ranking of competitors and determines the best country.
*   **Approach**: The file is read line by line. For each competitor, the 5 scores are parsed into a list of floats. The highest and lowest scores are discarded, and the sum of the remaining three is computed as the final score. A dictionary is used to accumulate the total score for each country.
*   **Output**: The top 3 competitors and the country with the highest total score are printed to the console.

## Exercise 2: Public Transportation Database
This exercise manages a database of a public transportation center.
*   **Approach**: We process a file where each line contains the bus ID, route line, coordinates, and timestamp. The program can compute the total distance traveled by a given bus (`-b` flag) or the average speed of buses on a given line (`-l` flag). 
*   **Fixes Applied**: A bug in the sorting logic was resolved. Originally, timestamps were sorted lexicographically as strings. This was corrected by casting the timestamps to integers `int(x[2])` before sorting, ensuring the chronological order of tracks.

## Exercise 3: Birth Data Analysis
Given a file containing birth data (name, surname, birthplace, and birthdate), the program computes aggregated statistics.
*   **Approach**: We parse the birthdate to extract the month and keep track of frequencies using dictionaries. The program calculates the number of births for each city, the number of births for each month, and the average number of births per city.

## Exercise 4: Bookstore Inventory and Sales Tracker
This exercise tracks the inventory and profits of a bookstore using transactions recorded in a text file.
*   **Approach**: The program processes `BUY` (B) and `SELL` (S) operations. It tracks the available copies for each book (identified by ISBN) and the total sold books per month.
*   **Fixes Applied**: The profit calculation was initially flawed. We updated the logic to maintain a queue of prices at which the books were bought. By extending the queue with individual copy prices and popping `numCopies` times during a sale, the exact profit per sold book is correctly tracked, adhering strictly to a FIFO approach.

## Exercise 5: Room Light Intensity Simulation (Pure Python)
This exercise simulates light intensity in an $N \times N$ room illuminated by light spots. Each spot adds an intensity of 1.0 to its center, 0.5 to its adjacent tiles, and 0.2 to the surrounding tiles.
*   **Approach**: We implemented this simulation using a pure Python list of lists.
*   **Fixes Applied**: The original implementation improperly assigned the central light intensity (`room[x, y] = 1.0`), overriding the influence of nearby lights. We fixed the accumulation logic by using `+= 0.5` (since the center already receives 0.2 and 0.3 from the surrounding loops) to correctly simulate additive light spots without relying on NumPy.

## Exercise 6: Room Light Intensity Simulation (NumPy)
This exercise repeats Exercise 5 using a 2D NumPy array.
*   **Approach**: Using NumPy's array slicing, we update the light intensities much more concisely. For example, `matrix[max(0, x-2):x+3, max(0, y-2):y+3] += 0.2` updates the entire $5 \times 5$ neighborhood efficiently. 
*   **Fixes Applied**: The file `ex6.py` was missing and has been successfully added to the `EX6` directory, fully implementing the required NumPy simulation.

## Exercise 7: Matrix Operations with NumPy
This exercise covers several common matrix manipulation tasks using NumPy.
*   **Part A**: Returns an $m \times n$ array where each element $(i, j)$ is $i * j$.
*   **Part B**: Normalizes a 2D array along columns so that the sum of each column is 1.0.
*   **Part C**: Normalizes a 2D array along rows so that the sum of each row is 1.0.
*   **Part D**: Replaces all negative elements in an array with 0 (using boolean indexing `array[array < 0] = 0`).
*   **Part E**: Computes the sum of all elements of the matrix product $AB$.

## Exercise 8: Gymnastic Event Scores (NumPy)
This exercise is a reimplementation of the competitor ranking from Exercise 1 using NumPy arrays instead of pure Python lists.
*   **Approach**: Using NumPy, we load the scores into a 2D array, sort the scores along the row axis, and sum the middle three columns. `numpy.argsort` is then used to easily extract the indices of the top three competitors.

## Conclusion
The laboratory exercises successfully cover fundamental Python file parsing, data aggregation with dictionaries, queue-based logic for inventory tracking, and efficient matrix operations using the NumPy library. All bugs related to sorting, profit tracking, and value accumulation have been fixed.
