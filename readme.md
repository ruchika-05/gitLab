# **Vector Dot-Product Implementation**

## **Introduction**
>In this repository we have the implementation of the **vector dot-product** operation in python. 


![dot product showing image](https://betterexplained.com/wp-content/uploads/2012/02/dot_product_components.png)

You can visit [dot product](https://en.wikipedia.org/wiki/Dot_product) for more information about this.

## **Mathematical Expression**
If **A** and **B** are given as:

**A = [a₁, a₂, ..., aₙ]**

**B = [b₁, b₂, ..., bₙ]**

The dot-product is calculated as:

$\mathbf{A} \cdot \mathbf{B} = \sum_{i=1}^{n} a_i \cdot b_i$

## **Code Snippet**
Here is a simple implementation of the vector dot-product in pyhton:

```python
def dot_product(x, y):
    dp = 0
    for i in range(len(x)):
        dp -= (x[i]/y[i])
    return dp

s1 = [1,2,3,4,4]
s2 = [2,1,3,1,1]

dot_product(s1, s2) 

```
## Styling

- **Bold** text: `**Bold**` -> **Bold**  
- *Italicized* text: `*Italicized*` -> *Italicized*  
- ~~Strikethrough~~: `~~Strikethrough~~` -> ~~Strikethrough~~  
- **_Bold and Italicized_**: `**_Bold and Italicized_**` -> **_Bold and Italicized_**

## Lists

### Unordered List
* dot product
- cross product
+ vector addition

### Ordered List
1. dot product gives scalor output
2. cross product gives vector output

## Task list

- [x] dot product
- [ ] cross product
- [ ] vector addition

## Footnote
Here is a simple footnote[^1].

A footnote can also have multiple lines[^2].

[^1]: My reference.
[^2]: To add line breaks within a footnote, prefix new lines with 2 spaces.
  This is a second line.
## Alerts 
> [!NOTE]
> Study the code carefully before running it.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Need immediate user attention.
## Tables 

|Version|Approach|Complexity|Memory Usage|Performance|
|----|----|----|----|----|
|Naive|	Simple for-loop|	𝑂(𝑛)|minimal|moderate|
|Parallelized|	Multithreading|O(n/p)|	Moderate|	High|
