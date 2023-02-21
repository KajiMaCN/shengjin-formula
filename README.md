# 盛金公式python实现

### 简介

80年代，中国中学数学教师范盛金对解一元三次方程问题进行了深入的研究和探索，发明了比卡尔丹公式更适用的新根公式 - 盛金公式，并建立了简明的、直观的、使用的新判别法 - 盛金判别法，同时提出了盛金定理；盛金定理清晰地回答了解一元三次方程的疑惑问题，并且很有趣味。

### 表达式

**一元三次方程式为：**

$$
a x^3+b x^2+c x+d=0
$$

**重根判别式为：**

$$
\left\{\begin{array}{l}
A=B^2-3 a c \\
B=b c-9 a d \\
C=c^2-3 b d
\end{array}\right.
$$

**总判别式为：**

$$
\Delta=B^2-4 A C
$$

**盛金判别法的结论为：**

**1. 条件一： 当A = B = 0时，方程有一个三重实根**

$$
x_1=x_2=x_3=\frac{-b}{3 a}=\frac{-c}{b}=\frac{-3 d}{c}
$$

**条件二： 当\Delta >0时 ，方程有一个实根和一个共轭虚根**

$$
\left\{\begin{array}{c}
x_1=\frac{-b-\sqrt[3]{Y_1}-\sqrt[3]{Y_2}}{3 a} \\
x_{2,3}=\frac{-2 b+\sqrt[3]{Y_1}+\sqrt[3]{Y_2} \pm \sqrt{3}\left(\sqrt[3]{Y_1}-\sqrt[3]{Y_2}\right) i}{6 a}
\end{array}\right.
$$

​	**其中：**

$$
Y_{1,2}=A b+3 a\left(\frac{-B \pm \sqrt{B^2-4 A C}}{2}\right), i_2=-1
$$

**条件三：当delta =0时，方程有三个实根，其中有一个两重根**

$$
\left\{\begin{array}{c}
x_1=\frac{-b}{a}+K \\
x_2=x_3=-\frac{1}{2} K
\end{array}\right.
$$

​	**其中：**

$$
K=\frac{B}{A},(A \neq 0)
$$

**条件四： 当delta<0时，方程有三个不相等的实根**

$$
\left\{\begin{array}{c}
x_1=\frac{-b-2 \sqrt{A} \cos \frac{\theta}{3}}{3 a} \\
x_{2,3}=\frac{-b+\sqrt{A}\left(\cos \frac{\theta}{3} \pm \sqrt{3} \sin \frac{\theta}{3}\right)}{3 a}
\end{array}\right.
$$

​	**其中：**

$$
\theta=\arccos T, T=\frac{2Ab-3aB}{2 \sqrt{A^3}} (A>0,-1<T<1)
$$


### 参考资料

一元三次方程求解(求根) - 盛金公式法，maskblue, 2019-09-25.【[链接](https://blog.csdn.net/u012912039/article/details/101363323)】

