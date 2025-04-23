# Wiki-Surfer: Navigating the Wikipedia Graph

## Overview

Wiki-Surfer is a web-based tool that finds the shortest path between two Wikipedia pages using graph search algorithms. It treats Wikipedia as a directed graph, where each page is a node and hyperlinks are edges. Given a starting page and a target page, Wiki-Surfer visualizes the shortest sequence of links connecting them.

## Features

-   **Graph Search Algorithms:** Implements Breadth-First Search (BFS) and Bidirectional Search.
-   **Interactive Web Interface:** Built with HTML, CSS, and JavaScript for a user-friendly experience.
-   **Performance Metrics:** Displays the number of pages visited and execution time.
-   
## Algorithms

### Breadth-First Search (BFS)

-   Explores all possible links level by level from the start page.
-   **Time Complexity:** O(|V| + |E|) (worst-case)
-   **Space Complexity:** O(|V|) (worst-case)

### Bidirectional Search

-   Starts from both the start and target pages and meets in the middle.
-   Typically faster than BFS for large graphs.
-   **Time Complexity:** O(|V| + |E|) (worst case)
-   **Space Complexity:** O(|V|) (worst case)


## Technologies Used

-   Python
-   PyScript
-   HTML
-   CSS
-   JavaScript

## Setup Instructions

1.  Clone the repository:

    ```bash
    git clone [https://github.com/TJPcodes/DSAWikiSurfersFinal.git]
    cd [DSAWikiSurfersFinal]
    ```

2.  Open `index.html` in your web browser.

## Running the Project

1.  Enter a starting page and a target page in the input fields.
2.  Select the search algorithm (BFS or Bidirectional Search) from the menu.
3.  Click the search button to start the algorithm.
4.  View the results, including the number of pages visited and execution time.

## Project Structure

Wiki-Surfer/
├── index.html # Main HTML file for the web interface
├── assets/ # Contains CSS, JavaScript, and other assets
│ ├── css/ # CSS files for styling the interface
│ ├── js/ # JavaScript files for interactivity
│ └── animations/ # GIF animation
├── scripts/ # Python scripts for the search algorithms
│ ├── bfs.py # Breadth-First Search implementation
│ ├── bidirectional.py # Bidirectional Search implementation
│ └── web_interface.py # Interface between web and python
├── README.md # This file
└── ...


## Team Members

-   Nathaniel Parkes
-   Carlos Vasquez
-   Tyler Pencinger


## Acknowledgements

-   This project was inspired by the Data Structures and Algorithms course at University of Florida.
-   We would like to thank our Professor and TA for their guidance and support.
