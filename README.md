
# LeetCode Style Practice


### Tips for Identifying Problem Type:  

To quickly identify the required approach for solving a coding problem, follow this structured **thought process**:  

---

### **1. Understand the Problem Type**
- **Graph**: Mentions nodes, edges, shortest path → **BFS/DFS, Dijkstra, Union-Find**  
- **Tree**: Involves hierarchical relationships → **Recursion, DFS, BFS, DP on Trees**  
- **Dynamic Programming (DP)**:  
  - **Optimal substructure** (solution builds on smaller subproblems)  
  - **Overlapping subproblems** (same subproblems repeat)  
  - Keywords: "ways to do X," "minimum/maximum," "count paths," "partition"  

- **Greedy**:  
  - Looks for an **immediate best choice** at each step  
  - Keywords: "maximize," "minimum cost," "smallest/largest"  

- **Recursion / Backtracking**:  
  - Involves **trying multiple possibilities** (e.g., permutations, subsets)  
  - Keywords: "generate all possible," "find all solutions"  

- **Sliding Window / Two Pointers**:  
  - Subarray problems, optimizing over contiguous elements  
  - Keywords: "longest," "shortest," "smallest subarray," "fixed/variable window"  

- **Sorting + Binary Search**:  
  - Involves searching efficiently over a sorted dataset  
  - Keywords: "find in sorted," "upper/lower bound," "minimum X for condition Y"  

- **Bit Manipulation**:  
  - Works directly on bits (XOR, AND, OR)  
  - Keywords: "bitwise," "parity," "toggle," "power of two"  

---

### **2. Identify Constraints**
- **Small `n` (~20–30)?** → **Backtracking / Recursion (Exponential OK)**  
- **Large `n` (≥10⁶)?** → **O(log n) or O(n) required (Binary Search, DP, or Greedy)**  

---

### **3. Look for Patterns in Examples**
- **Does the problem break into subproblems?** → **DP**  
- **Can you make local greedy choices?** → **Greedy**  
- **Does it ask for a shortest path?** → **Graph BFS/Dijkstra**  
- **Does it involve arranging elements?** → **Sorting / Two Pointers**  

---

### **4. Recognize Recurrence & State**
- If a problem depends on previous results, define **states** → **Use DP**  
- If choices at each step don’t affect future choices → **Use Greedy**  

By practicing problem classification and recognizing patterns, you can **instantly** identify the best approach! 🚀




## Dynamic Programming Approach

Dynamic Programming (DP) solves problems by breaking them into **overlapping subproblems**, storing their solutions to avoid redundant computations. The core steps are:

1. **Break** the problem into **subproblems**.
2. **Store** previously computed results (**memoization** or **tabulation**).
3. **Build** the final solution **bottom-up** using a recurrence relation.
