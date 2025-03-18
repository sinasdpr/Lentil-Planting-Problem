**Problem Statement (Combinatorial Mathematics - Lentil Planting Problem)**  

Grandmother wants to plant lentils. She has **n** lentil seeds and a row of **k** planting spots, which are labeled from **1** to **k** from left to right. Each spot can hold at most one seed.  

Lentils should be planted with proper spacing. If two adjacent spots both contain a lentil seed, their growth will be hindered. Grandmother wants to distribute the **n** seeds in such a way that the number of adjacent pairs of spots containing seeds is minimized.  

Formally, we need to minimize the number of indices **i** (where **1 ≤ i ≤ k - 1**) such that both positions **i** and **i + 1** contain a lentil seed.  

**Input:**  
The first line contains two integers **k** (the number of planting spots) and **n** (the number of lentil seeds).  
- **2 ≤ k ≤ 100**  
- **1 ≤ n ≤ k**  

**Output:**  
Print a single integer — the minimum number of adjacent pairs where both spots contain lentil seeds.  

**Example 1:**  
_Input:_  
```
2 5
```  
_Output:_  
```
0
```  
**Explanation:**  
Grandmother can plant lentils in positions **1** and **4**, ensuring no two lentils are adjacent.  

**Example 2:**  
_Input:_  
```
4 5
```  
_Output:_  
```
2
```  
**Explanation:**  
One optimal way is to plant lentils in positions **1, 2, 3,** and **5**. The adjacent pairs **(1,2)** and **(2,3)** both contain lentils, so the answer is **2**.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Sina SaeediPour
