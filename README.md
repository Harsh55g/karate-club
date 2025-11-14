DSC212 - Modularity on the Karate Club Graph

This project implements the recursive spectral modularity partitioning algorithm to find communities within the classic Zachary Karate Club graph. This implementation is based on the research assignment for the DSC212: Graph Theory module.

Student: Harsh Suthar
Roll No: IMS24101

About This Project

The main goal is to use graph mathematics to see if we can automatically find the "social fault lines" in the Karate Club network that led to its real-world split into two factions. We do this by implementing a community detection algorithm from scratch.

Core Logic

Modularity Matrix (B): We calculate the $n \times n$ modularity matrix $B = A - \frac{kk^T}{2m}$, where $A$ is the adjacency matrix, $k$ is the degree vector, and $m$ is the total number of edges. This matrix compares the actual number of edges to the expected number in a random graph.

Spectral Bipartition: To split a community, we find the leading eigenvector ($u_1$) of its restricted modularity matrix ($B^{(C)}$).

Splitting: We partition the nodes into two new groups based on the sign of the entries in $u_1$ (positive or negative).

Stopping Condition: We only split a community if the corresponding leading eigenvalue ($\lambda_1$) is positive. If $\lambda_1 \le 0$, splitting would not improve the network's overall modularity, so we stop.

Recursion: We apply this process recursively to the new, smaller communities until no more positive eigenvalues are found.

Files

DSC212_Assignment_HarshSuthar.ipynb: The main Jupyter Notebook containing all the Python code, analysis, and visualizations.

How to Run

Prerequisites: You need a Python environment with Jupyter Notebook (or Jupyter Lab, VS Code, etc.) and the following libraries installed:

numpy

networkx

matplotlib

seaborn (used for plot styling)

You can install them using pip:

pip install numpy networkx matplotlib seaborn


Open the Notebook: Launch your Jupyter environment.

jupyter notebook


or

jupyter lab


Run the Code: Open the DSC212_Assignment_HarshSuthar.ipynb file. You can run all cells from top to bottom ("Run" > "Run All Cells") to see the full analysis, all the graph visualizations at each step, and the final metric evolution plots.

Summary of Tasks Completed

Task 1: Implemented the recursive spectral modularity partitioning.

Task 2: Visualized the graph after each split, with communities colored.

Task 3: Computed degree_centrality, betweenness_centrality, closeness_centrality, and clustering coefficient at each step.

Task 4: Plotted the evolution of these metrics for every node across all iterations.

Task 5: Wrote a discussion on the results, noting how the centrality of key nodes (like 0 and 33) changes as the partition progresses.
