# VIT Bhopal University
## Term End Examinations – Fall Semester 2026–27
### Course Code: MAT2002 | Course Title: Discrete Mathematics and Graph Theory
**Duration:** 180 Minutes (3 Hours)  
**Maximum Marks:** 100  

---

# Paper 1: 16-10-2026 (Slot: A14 + D11 + D12 | Session: S-2)

**General Instructions:**
1. Non-Programmable calculator is permitted: **YES**
2. Reference tables are permitted: **NA**

---

### PART – A ($12 \times 5 = 60\text{ Marks}$)

#### Question 1
* **(a)** There are two restaurants next to each other. One has a signboard that says *"Good food is not cheap"* and another has a signboard that says *"Cheap food is not good."* Are the signboards saying the same thing? Prove or disprove using propositional equivalence.  
  *(6 Marks)*
* **(b)** Find the truth table of $p \to q$ and $(\sim p \lor \sim q) \to q$. Given the value of $p \to q$ is true, determine the value of $(\sim p \land \sim q) \to q$ from the truth table.  
  *(6 Marks)*

**[OR]**

* **(c)** Show the validity of the following argument using the rule of conditional proof:  
  *"If my program runs successfully then I will submit my project. I can appear in the examination if I submit my project. Either my program runs successfully or the computer crashes. Therefore, if the computer does not crash then I can appear at the examination."*  
  *(12 Marks)*

---

#### Question 2
* **(a)** Draw the Hasse diagram of the power set of $D_{36}$.  
  *(6 Marks)*
* **(b)** For any two real numbers $\theta$ and $\phi$, we define $\theta \, R \, \phi$ if and only if $\sec^2 \theta - \tan^2 \phi = 1$. Check if $R$ is an equivalence relation or not.  
  *(6 Marks)*

**[OR]**

* **(c)** Consider the following relation $R$ on $A = \{1, 2, 3, 4, 5, 6, 7, 8\}$:  
  $$R = \{(i, j) : |i - j| = 3\}$$  
  Determine whether $R$ is an equivalence relation. Check whether $R$ is a partial ordered relation or not?  
  *(12 Marks)*

---

#### Question 3
* **(a)** Construct an input/output table for the following Boolean function:  
  $$f(A, B, C) = (A + B)\overline{C}$$  
  Also find the disjunctive normal form (DNF) of the Boolean function. Hence represent the logical expressions with minterms.  
  *(6 Marks)*
* **(b)** Express the following function into its Sum of Products (SOP) / PDNF without using a truth table:  
  * **(i)** $((x y)' z)' ((x' + z)(y' + z'))'$  
  * **(ii)** $x + y z + x y z$  
  *(6 Marks)*

**[OR]**

* **(c)** Determine whether the posets represented by the following Hasse diagrams are lattices:  
  * **Diagram 1:** A linear chain of 4 elements: $v_4 \prec v_3 \prec v_2 \prec v_1$.  
  * **Diagram 2:** Poset with elements $\{v_1, v_2, v_3, v_4, v_5, v_6\}$ where $v_6$ is the bottom element, $v_1$ is the top element; $v_5$ connects to $v_6, v_2, v_4$; $v_4$ connects to $v_6, v_5, v_3, v_1$; $v_2, v_3$ connect to $v_1$.  
  * **Diagram 3:** Bow-tie / X-shape poset with two bottom minimal elements $v_4, v_5$ both connected to a common intermediate element $v_3$, which then branches to two maximal elements $v_1, v_2$.  
  *(12 Marks)*

---

#### Question 4
* **(a)** Apply Kruskal's algorithm to find the shortest distance between the vertices $e$ and $f$ in the weighted graph with vertices $\{e, a, b, c, d, f\}$ and edge weights:  
  * $(e, a) = 18$
  * $(e, c) = 15$
  * $(a, c) = 6$
  * $(a, b) = 9$
  * $(c, b) = 14$
  * $(c, d) = 7$
  * $(b, d) = 10$
  * $(b, f) = 28$
  * $(d, f) = 36$  
  *(6 Marks)*
* **(b)** Represent the following pseudograph using an incidence matrix:  
  * Vertices: $\{v_1, v_2, v_3, v_4, v_5\}$  
  * Edge descriptions:
    * Loop $e_1$ on $v_1$
    * Parallel edges $e_2, e_3$ between $v_1$ and $v_2$
    * Edge $e_4$ between $v_2$ and $v_3$
    * Edge $e_5$ between $v_3$ and $v_5$
    * Edge $e_6$ between $v_2$ and $v_5$
    * Edge $e_7$ between $v_2$ and $v_4$
    * Loop $e_8$ (or $e_9$) on $v_4$  
  *(6 Marks)*

**[OR]**

* **(c)** Determine whether the given pair of 8-vertex graphs is isomorphic. Exhibit an isomorphism or provide a rigorous argument that none exists.  
  *(12 Marks)*

---

#### Question 5
* **(a)** Apply Prim's algorithm to the following weighted graph $G$ to get a minimal spanning tree:  
  * Perimeter vertices form a hexagon: $A-B-C-D-E-F-A$ with center vertex $G$.  
  * Outer cycle edge weights:  
    $(A, B) = 3, \; (B, C) = 9, \; (C, D) = 10, \; (D, E) = 10, \; (E, F) = 7, \; (F, A) = 6$  
  * Radial edges connecting to center vertex $G$:  
    $(G, A) = 4, \; (G, B) = 4, \; (G, C) = 7, \; (G, D) = 5, \; (G, E) = 11, \; (G, F) = 8$  
  *(12 Marks)*

**[OR]**

* **(b)** Does there exist a tree for the following degree sequences?  
  * **(i)** $1, 1, 1, 1, 2, 2, 2, 3, 3$  
  * **(ii)** $4, 4, 3, 2, 1, 1, 1, 1, 1$  
  If yes, then draw the tree; else explain why such a tree cannot exist.  
  *(12 Marks)*

---

### PART – B ($8 \times 5 = 40\text{ Marks}$)

#### Question 6
Show that $(p \land q) \land (p \to r) \land (q \to r) \to r$ is a tautology without using truth tables.  
*(8 Marks)*

#### Question 7
Let $A = \{1, 2, 3\}$ and $R = \{(1, 1), (1, 2), (2, 2), (3, 3)\}$. Determine whether $R$ is:  
1. Reflexive  
2. Symmetric  
3. Transitive  
*(8 Marks)*

#### Question 8
Consider the Hasse diagram of $D_{30}$, under partial order of divisibility. Show it forms a lattice.  
* **(a)** Is the lattice distributive?  
* **(b)** Is it complemented?  
*(8 Marks)*

#### Question 9
Find a Hamilton circuit or path for the given graph, if it exists:  
* Graph with 11 vertices $\{a, b, c, d, e, f, g, h, i, j, k\}$ arranged symmetrically with connected bow-shaped upper and lower cycles through intermediate vertex $f$.  
*(8 Marks)*

#### Question 10
Find the eccentricity of all vertices, radius, diameter and centre of the following tree. It is given that the distance between any two adjacent vertices is $1\text{ unit}$:  
* Vertices $\{v_1, v_3\}$ are leaves connected to vertex $v_2$.  
* Vertices $\{v_4, v_6\}$ are leaves connected to vertex $v_5$.  
* Vertex $v_7$ is a leaf connected to $v_5$.  
* Vertices $v_2$ and $v_5$ are connected by edge $(v_2, v_5)$.  
*(8 Marks)*

---
---

# Paper 2: 17-10-2026 (Slot: A21 + A22 + A23 | Session: S-2)

**General Instructions:**
1. Non-Programmable calculator is permitted: **YES**
2. Reference tables are permitted: **NO**

---

### PART – A ($5 \times 12 = 60\text{ Marks}$)

#### Question 1
* **(a)** Show that the premises:  
  * *"It is not sunny this afternoon and it is colder than yesterday,"*  
  * *"We will go swimming only if it is sunny,"*  
  * *"If we do not go swimming, then we will take a canoe trip,"* and  
  * *"If we take a canoe trip, then we will be home by sunset"*  
  lead to the conclusion *"We will be home by sunset."*  
  *(6 Marks)*
* **(b)** Express the negations of each of the following statements so that all negation symbols immediately precede predicates:  
  * **(i)** $\exists x \exists y (Q(x, y) \leftrightarrow Q(y, x))$  
  * **(ii)** $\forall x \exists y P(x, y) \lor \forall x \exists y Q(x, y)$  
  *(6 Marks)*

**[OR]**

* **(c)** Determine whether the following statements are equivalent, using biconditional statements:  
  * **(i)** $p \leftrightarrow q \equiv (p \land q) \lor (\sim p \land \sim q)$  
  * **(ii)** $(p \to q) \to r \equiv (p \land \sim q) \to r$  
  *(12 Marks)*

---

#### Question 2
* **(a)** The relation $R$ on the set $S$ of all real numbers is defined as: $a \, R \, b$ if and only if $1 + a b \ge 0$. Show that this relation is reflexive and symmetric but not transitive.  
  *(6 Marks)*
* **(b)** Let $R$ be the relation represented by the matrix:  
  $$M_R = \begin{bmatrix} 
  0 & 1 & 0 \\ 
  0 & 0 & 1 \\ 
  1 & 1 & 0 
  \end{bmatrix}$$  
  Find the matrices that represent the relation $R^{-1}$ and $\bar{R}$.  
  *(6 Marks)*

**[OR]**

* **(c)** Let $D_{120}$ be the set of divisors of $120$, and let the relation '$\le$' defined by division $a \mid b$ be a partial ordering on $D_{120}$:  
  * **(i)** Draw the Hasse Diagram of $D_{120}$.  
  * **(ii)** Determine the GLB of $B$, where $B = \{4, 6, 10\}$.  
  * **(iii)** Determine the LUB of $B$, where $B = \{4, 6, 10\}$.  
  * **(iv)** Determine the GLB of $B$, where $B = \{12, 20, 30\}$.  
  * **(v)** Determine the LUB of $B$, where $B = \{12, 20, 30\}$.  
  *(12 Marks)*

---

#### Question 3
* **(a)** Determine all the sublattices of $D_{30}$ that contain at least four elements.  
  *(6 Marks)*
* **(b)** Let $A = \{1, 2, 3, 4\}$ and $R = \{(1, 1), (2, 2), (3, 3), (4, 4), (1, 2), (1, 4), (2, 4), (3, 4)\}$:  
  1. Determine whether $R$ is a partial order relation.  
  2. Find the relation matrix.  
  *(6 Marks)*

**[OR]**

* **(c)** Find the DNF and CNF of the following Boolean function:  
  $$((p \land q) \lor (\neg p \land \neg r)) \to (\neg q \to r)$$  
  and hence draw the logic circuits of its DNF and CNF.  
  *(12 Marks)*

---

#### Question 4
* **(a)** Prove that the graphs $G$ and $H$ shown below are isomorphic:  
  * Graph $G$: Vertices $\{u_1, u_2, u_3, u_4, u_5, u_6\}$  
  * Graph $H$: Vertices $\{v_1, v_2, v_3, v_4, v_5, v_6\}$  
  *(6 Marks)*
* **(b)** Draw the following graphs:  
  * **(i)** Two 3-regular graphs with six vertices.  
  * **(ii)** Two 3-regular graphs with eight vertices.  
  *(6 Marks)*

**[OR]**

* **(c)** The weighted graph in the figure shows some major roads in New Jersey, where the weight of each edge represents the distance between the corresponding cities:  
  * Vertices: $\text{Newark}, \text{Woodbridge}, \text{Trenton}, \text{Asbury Park}, \text{Camden}, \text{Atlantic City}, \text{Cape May}$  
  * Edge weights:  
    * $(\text{Newark}, \text{Woodbridge}) = 20$  
    * $(\text{Woodbridge}, \text{Trenton}) = 42$  
    * $(\text{Woodbridge}, \text{Asbury Park}) = 35$  
    * $(\text{Trenton}, \text{Camden}) = 30$  
    * $(\text{Trenton}, \text{Asbury Park}) = 60$  
    * $(\text{Camden}, \text{Asbury Park}) = 40$  
    * $(\text{Camden}, \text{Atlantic City}) = 55$  
    * $(\text{Camden}, \text{Cape May}) = 85$  
    * $(\text{Asbury Park}, \text{Atlantic City}) = 75$  
    * $(\text{Atlantic City}, \text{Cape May}) = 45$  
  Find the shortest route in distance between:  
  1. Newark and Camden  
  2. Newark and Cape May, using these roads.  
  *(12 Marks)*

---

#### Question 5
* **(a)** Find the eccentricity of all vertices, radius, diameter, and centre of the tree graph $G$ with 17 vertices $\{v_1, v_2, \dots, v_{17}\}$. It is given that the distance between any two adjacent vertices is $1\text{ unit}$.  
  *(6 Marks)*
* **(b)** Consider the following graphs:  
  * **(i)** $K_3, \; K_5$  
  * **(ii)** $K_{3,3}, \; K_{3,5}$  
  Colour all the graphs with proper colouring and write the chromatic number of all the graphs.  
  *(6 Marks)*

**[OR]**

* **(c)** Find a minimum spanning tree for the connected weighted graph shown in the figure using Prim's Algorithm:  
  * Hexagon cycle $A-B-C-D-E-F-A$ with center vertex $G$:  
    * $(A, B) = 3, \; (B, C) = 9, \; (C, D) = 10, \; (D, E) = 10, \; (E, F) = 7, \; (F, A) = 6$  
    * $(G, A) = 4, \; (G, B) = 4, \; (G, C) = 7, \; (G, D) = 5, \; (G, E) = 11, \; (G, F) = 8$  
  *(12 Marks)*

---

### PART – B ($5 \times 8 = 40\text{ Marks}$)

#### Question 6
Prove that the rule of hypothetical syllogism is valid using a truth table.  
*(8 Marks)*

#### Question 7
Let $A = \{2, 3, 4, 6, 12, 36, 48\}$ be a non-empty set and $R$ be the partial order relation of divisibility defined on $A$. Draw a directed graph and equivalent Hasse diagram of $R$.  
*(8 Marks)*

#### Question 8
Let $A = \mathbb{Z}^+$, and define a relation $R$ by $a \, R \, b \iff \gcd(a, 6) = \gcd(b, 6)$. Determine whether $R$ is an equivalence relation.  
*(8 Marks)*

#### Question 9
Draw the following graphs:  
* **(i)** A graph with five vertices whose every edge is a bridge.  
* **(ii)** A graph with six vertices that has exactly two cut points.  
*(8 Marks)*

#### Question 10
Consider the graph $G$ shown below:  
* Edge $(a, b)$ connected to cycle $b-c-e-d-b$, and edge $(e, f)$ attached to $e$:  
  * **(i)** Which edges must be included in every spanning tree?  
  * **(ii)** How many spanning trees does the graph have? Draw all the spanning trees.  
*(8 Marks)*

---
---

# Paper 3: 18-10-2026 (Slot: F11 + F12 + F14 | Session: S-2)

**General Instructions:**
1. Non-Programmable calculator is permitted: **YES**
2. Reference tables are permitted: **NA**

---

### PART – A ($12 \times 5 = 60\text{ Marks}$)

#### Question 1
* **(a)** Prove, without using a truth table, that the following statement is a tautology:  
  $$[((p \lor q) \to r) \land \neg p] \to (q \to r)$$  
  *(12 Marks)*

**[OR]**

* **(b)** Write the converse, contrapositive and negation of each of the following conditional statements:  
  * **(i)** If Neha wins, then Shelly loses.  
  * **(ii)** If 9 is odd then the square of 9 is odd.  
  * **(iii)** If all cats meow, then some dogs bark.  
  * **(iv)** If John wins, then Mary loses and the school closes.  
  *(12 Marks)*

---

#### Question 2
* **(a)** Let $R$ and $S$ be relations from Set $A$ to Set $B$. Derive the following identities:  
  $$(R \cup S)^{-1} = R^{-1} \cup S^{-1} \quad \text{and} \quad (R \cap S)^{-1} = R^{-1} \cap S^{-1}$$  
  *(6 Marks)*
* **(b)** Let $A, B, C \subseteq U$, where $U$ is the universal set. Simplify the following identity, naming the set laws used:  
  $$(\overline{A \cup B}) \cup (\bar{A} \cap \bar{B} \cap C) = U$$  
  *(All complements are taken relative to $U$.)*  
  *(6 Marks)*

**[OR]**

* **(c)** Let $A = \{1, 2, 3, 4, 5, 6\}$ and define a relation $R$ on $A$ by:  
  $$R = \{(i, j) \in A \times A : |i - j| = 2\}$$  
  Determine whether $R$ is reflexive, symmetric, antisymmetric and transitive; justify your answers. Hence determine whether $R$ is an equivalence relation or a partial order relation.  
  *(12 Marks)*

---

#### Question 3
* **(a)** In Boolean algebra, prove or disprove the following assertion:  
  $$a \land b = a \land c \quad \text{and} \quad a \lor b = a \lor c \implies b = c$$  
  *(6 Marks)*
* **(b)** Express the following Boolean function in canonical disjunctive normal form, as a sum of minterms:  
  $$f(x, y, z) = (x + y)(x + z) + y + z'$$  
  *(6 Marks)*

**[OR]**

* **(c)** Let $B$ be the set of all positive divisors of $30$. For $a, b \in B$, define:  
  $$a \land b = \gcd(a, b), \quad a \lor b = \operatorname{lcm}(a, b), \quad a' = \frac{30}{a}$$  
  Prove that these operations make $B$ a Boolean algebra, with least element $1$ and greatest element $30$.  
  *(12 Marks)*

---

#### Question 4
* **(a)** Find the number of edges in the complete graph $K_{10}$ and the complete bipartite graph $K_{5,7}$. Justify both answers.  
  *(6 Marks)*
* **(b)** Draw the undirected graph represented by the following incidence matrix. Determine whether the graph is simple and justify your answer:  
  $$A = \begin{bmatrix}
  1 & 0 & 0 & 0 & 0 & 0 \\
  1 & 1 & 1 & 0 & 0 & 0 \\
  0 & 1 & 0 & 1 & 1 & 1 \\
  0 & 0 & 0 & 0 & 1 & 1 \\
  0 & 0 & 1 & 1 & 0 & 0
  \end{bmatrix}$$  
  *(6 Marks)*

**[OR]**

* **(c)** Define an Euler path and an Euler circuit in an undirected graph. State and prove that a finite connected undirected graph with at least one edge has an Euler circuit if and only if every vertex has even degree.  
  *(12 Marks)*

---

#### Question 5
* **(a)** A full binary tree $T$ has $n$ vertices, where $n \ge 3$. Derive a formula for the number of pendant vertices in $T$.  
  *(6 Marks)*
* **(b)** A tree $T$ has $n$ vertices. Determine the number of edges in $T$, and hence calculate the sum of the degrees of all its vertices.  
  *(6 Marks)*

**[OR]**

* **(c)** Explain Kruskal's algorithm for finding a minimum spanning tree. Define the relevant terms and determine the total weight of a minimum spanning tree for the given graph:  
  * Vertices: $\{a, b, c, d, e, f\}$  
  * Edge weights:  
    * $(a, b) = 5$  
    * $(a, c) = 5.6$  
    * $(a, d) = 3$  
    * $(b, c) = 10.2$  
    * $(b, d) = 3$  
    * $(b, e) = 4.8$  
    * $(c, d) = 2$  
    * $(c, f) = 2.5$  
    * $(c, e) = 6.0$  
    * $(d, e) = 4.5$  
    * $(d, f) = 7.0$  
    * $(e, f) = 6.1$  
  *(12 Marks)*

---

### PART – B ($8 \times 5 = 40\text{ Marks}$)

#### Question 6
Construct truth tables for $p \to q$ and $(\neg p \lor \neg q) \to q$. Using the truth table, determine the truth value of $(\neg p \lor \neg q) \to q$, if $p \to q$ is false.  
*(8 Marks)*

#### Question 7
For each of the following, specify a nonempty set $A$ and a relation $R$ on $A$ having the stated properties. Justify every claimed property and give a counterexample to the property that fails:  
* **(i)** Reflexive and transitive, but not symmetric.  
* **(ii)** Symmetric and transitive, but not reflexive.  
* **(iii)** Reflexive and symmetric, but not transitive.  
*(8 Marks)*

#### Question 8
Determine whether each of the posets represented by the following Hasse diagrams is a lattice. Justify:  
* **(a)** A 4-element chain: $a \prec b \prec c \prec d$.  
* **(b)** Poset on 7 elements $\{a, b, c, d, e, f, g\}$:  
  * Element $a$ is the bottom minimum element.  
  * $b, c$ cover $a$.  
  * $d$ covers $b, c$.  
  * $e, f$ cover $d$.  
  * $g$ is the top maximum element and covers $e, f$.  
*(8 Marks)*

#### Question 9
Draw the digraph of the adjacency matrix:  
$$X(G) = \begin{bmatrix}
0 & 1 & 0 & 1 & 0 \\
0 & 0 & 2 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
1 & 0 & 1 & 0 & 1 \\
0 & 0 & 1 & 1 & 0
\end{bmatrix}$$  
*(8 Marks)*

#### Question 10
Find the chromatic number and construct a proper colouring of each graph:  
* **Graph 1:** Symmetrical 6-vertex hexagon with central cross-connections / diagonals.  
* **Graph 2:** 9-vertex multipartite structure with vertices $\{a, b, c, d, e, f, g, h, i\}$.  
*(8 Marks)*