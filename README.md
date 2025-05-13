# Doubly Linked List

## Application Description

This project implements a **Doubly Linked List** data structure. It allows storing elements in memory and performing operations such as adding, deleting, searching, and reversing elements. It supports the following operations:

- Appending elements to the end of the list (`append`)
- Inserting elements at a specific position (`insert`)
- Deleting elements by index (`delete`)
- Searching for elements by value (`find_first_element`, `find_last_element`)
- Cloning the list (`clone`)
- Reversing the list (`reverse`)
- Clearing all elements (`clear`)
- Extending the list with another list (`extend`)

## Variant Number and Description

Variant number: **3**

Variant description:
- Initial implementation: Array based list
- Refactor implementation: Doubly linked list

## Instructions to Build the Project and Run Tests

1. Clone the repository:
   ```bash
   git clone https://github.com/alomj/MTRPZ_Lab2
2. To run the tests, use unittest:
   ```bash
   python -m unittest discover

## Commit Link with Failing Tests on CI
### [Failed Commit](https://github.com/alomj/MTRPZ_Lab2/commit/45c445c21d9e17d11a4cbd30fe37a32ce51cb6e6)

## Conclusions

Unit tests were indeed helpful during the development process, as they automated the validation of the core operations of the doubly linked list. This significantly eased the detection of bugs, especially when adding new features or modifying code. Without tests, manual verification of each part of the program would have taken more time and resources.