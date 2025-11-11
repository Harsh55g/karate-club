# DSC212: Graph Theory  
### Research Assignment — *Modularity on the Karate Club Graph*  

**Name:** Nikhil Verma  
**Roll Number:**IMS24158 

---

## 📘 Project Overview
This repository contains my submission for the **Research Assignment** of the course **DSC212: Graph Theory**, focusing on **Modularity and Community Detection** using **Spectral Methods**.

The assignment applies **recursive spectral modularity partitioning** on the classic **Zachary’s Karate Club network**, one of the most well-known datasets in social network analysis.

---

## 🧠 Objective
To implement a **spectral modularity-based community detection algorithm** that:
1. Detects multiple communities in the Karate Club graph using recursive bisection.  
2. Visualizes the graph after each split with community coloring.  
3. Computes and tracks network metrics:
   - Degree Centrality  
   - Betweenness Centrality  
   - Closeness Centrality  
   - Clustering Coefficient  
4. Analyzes how these metrics evolve as the community structure becomes more refined.  

---

## ⚙️ Implementation Summary
- **Graph Dataset:** Zachary’s Karate Club Graph (NetworkX built-in)
- **Algorithm:**
  - Compute modularity matrix  
  - Extract the **leading eigenvector** of `B = A - (k kᵀ)/(2m)`
  - Partition nodes by the sign of the eigenvector components  
  - Recurse on subcommunities as long as the **largest eigenvalue (λ₁) > 0**  
- **Libraries Used:**  
  `numpy`, `networkx`, `matplotlib`, `seaborn`, `pandas`

---

## 📊 Key Results
- **Final modularity:** `Q = 0.1643`  
- The algorithm successfully identifies community divisions that reflect the real-world split between **Mr. Hi’s** group and the **Officer’s** group.  
- **Nodes 0 and 33** consistently remain most central — acting as structural bridges between communities.  
- **Metric evolution plots** and **heatmaps** visualize how network structure changes with each split.

---

## 📈 Visual Outputs
The Jupyter Notebook (`karate_club_assignment.ipynb`) includes:
- Graph visualizations for each iteration  
- Modularity value displayed in plot titles  
- Line plots of centrality metrics evolution  
- Heatmaps summarizing all metrics across nodes and iterations  

---

## 🧩 Discussion Summary
- **Degree & Betweenness Centrality:** Highest for nodes 0 and 33 — they function as network bridges.  
- **Closeness Centrality:** Decreases slightly as communities become more modular (greater separation).  
- **Clustering Coefficient:** Remains high within tight-knit subgroups, reflecting stable intra-community cohesion.  
- The recursive spectral modularity method captures statistically meaningful divisions even when total modularity stops increasing — consistent with **Newman (2006)**.

---

## 📚 Reference
> M. E. J. Newman (2006). *Modularity and community structure in networks*.  


---

## 🧾 File Structure
├── karate_club_assignment.ipynb # Main Jupyter Notebook

├── README.md # Project documentation (this file)

---

## 🏁 Conclusion
This project demonstrates how **spectral graph theory** and **modularity optimization** can uncover latent social structures from network connectivity alone.  
Even with modest modularity (Q = 0.1643), the algorithm effectively identifies meaningful communities and highlights central figures — showing the power of spectral methods in network science.

---

**Submitted by:**  
*Nikhil Verma*  
2nd Year BS–MS Student, IISER Thiruvananthapuram  
