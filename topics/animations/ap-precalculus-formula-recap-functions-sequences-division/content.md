---
title: "AP Precalculus: Formula Recap — Functions, Sequences, Division"
topic: animations
example: ap-precalculus-formula-recap-functions-sequences-division
status: concept-note
languages: [en, zh-TW, fr, de, ru]
created: 2026-11-23
author: Wei-Che Hung
---

# AP Precalculus: Formula Recap — Functions, Sequences, Division

![AP Precalculus: Formula Recap — Functions, Sequences, Division](media/ap-precalculus-formula-recap-functions-sequences-division.gif)

## What happens

1. What $y = f(x)$ means. The input $x_1 = 1$ goes into $f(x) = 2x + 1$ and $y_1 = 3$ comes out, giving the point $(1,\ 3)$ . The input $x_2 = 3$ gives $y_2 = 7$ and the point $(3,\ 7)$ . The line through all such points is the graph of $f$ .
2. A line $y = mx + b$ . Starting from $y = 3x + 3$ , the slope $m$ changes from $3$ to $1$ to $-1$ and the line turns around the point $(0,\ 3)$ . With $m = 3$ again, $b$ changes from $3$ to $6$ to $-2$ and the line moves up and down, staying parallel.
3. Shifting a parabola. $y = x^2$ becomes $y = (x - 3)^2$ and the curve moves right $3$ . It becomes $y = (x + 4)^2$ and the curve moves left $4$ . In each case the lowest point is where the bracket is $0$ .
4. An arithmetic sequence. The terms $1, 3, 5, 7, 9$ give $a_1 = 1$ and $d = 2$ . Putting $n = 2, 3, 5$ into $a_n = a_1 + (n - 1)d$ gives back $3$ , $5$ and $9$ . With the numbers in, $a_n = 1 + (n - 1)\cdot 2 = 2n - 1$ .
5. A geometric sequence. The terms $3, 6, 12, 24, 48$ give $a_1 = 3$ and $r = 2$ . Putting $n = 2, 3, 5$ into $a_n = a_1 \cdot r^{\,n-1}$ gives back $6$ , $12$ and $48$ , so $a_n = 3 \cdot 2^{\,n-1}$ .
6. Long division. $x^2 + 3x + 5$ is divided by $x - 1$ in four moves, done twice: divide the first terms, multiply back, subtract, bring down. The quotient is $x + 4$ and the remainder is $9$ . The graph of $f(x)$ approaches the line $y = x + 4$ far from $x = 1$ .

## Concept

A formula is a machine: numbers go in, one number comes out.

```math
y = f(x), \qquad y = mx + b, \qquad y = (x - h)^2
```

- In $y = mx + b$ , $m$ is the slope (go right $1$ , the line goes up $m$ ) and $b$ is where the line crosses the $y$ axis.
- In $y = (x - h)^2$ , the curve of $y = x^2$ moves right $h$ ; $(x + 4)^2$ is $(x - (-4))^2$ , so it moves left $4$ .

The $n$ -th term of a sequence comes from the first term and one fixed number:

```math
a_n = a_1 + (n - 1)d \qquad\qquad a_n = a_1 \cdot r^{\,n-1}
```

| Sequence | $a_1$ | Fixed number | $a_n$ |
|---|---:|---:|---|
| $1, 3, 5, 7, 9$ | $1$ | $d = 2$ (added) | $2n - 1$ |
| $3, 6, 12, 24, 48$ | $3$ | $r = 2$ (multiplied) | $3 \cdot 2^{\,n-1}$ |

Long division writes a rational function as quotient plus remainder over the divisor:

```math
\frac{x^2 + 3x + 5}{x - 1} = (x + 4) + \frac{9}{x - 1}
```

Check: $(x - 1)(x + 4) + 9 = x^2 + 3x - 4 + 9 = x^2 + 3x + 5$ . For large $|x|$ the term $\frac{9}{x - 1}$ is close to $0$ , so $f(x) \approx x + 4$ .

## Summary

A formula takes numbers in and gives one number out. In $y = mx + b$ the slope $m$ sets how steep the line is and $b$ sets where it crosses the $y$ axis; $(x - 3)^2$ moves $y = x^2$ right $3$ and $(x + 4)^2$ moves it left $4$ . The sequence $1, 3, 5, 7, 9$ has $a_n = 2n - 1$ and the sequence $3, 6, 12, 24, 48$ has $a_n = 3 \cdot 2^{\,n-1}$ . Long division gives $\frac{x^2 + 3x + 5}{x - 1} = (x + 4) + \frac{9}{x - 1}$ , so far from $x = 1$ the graph follows the line $y = x + 4$ .

### 繁體中文

公式就像一台機器：放入數字，得到一個數字。在 $y = mx + b$ 中，斜率 $m$ 決定直線有多陡， $b$ 決定直線與 $y$ 軸的交點； $(x - 3)^2$ 把 $y = x^2$ 向右移 $3$ ， $(x + 4)^2$ 把它向左移 $4$ 。數列 $1, 3, 5, 7, 9$ 的通項是 $a_n = 2n - 1$ ，數列 $3, 6, 12, 24, 48$ 的通項是 $a_n = 3 \cdot 2^{\,n-1}$ 。長除法得到 $\frac{x^2 + 3x + 5}{x - 1} = (x + 4) + \frac{9}{x - 1}$ ，所以離 $x = 1$ 越遠，圖形越接近直線 $y = x + 4$ 。

### Français

Une formule prend des nombres en entrée et donne un seul nombre en sortie. Dans $y = mx + b$ , la pente $m$ fixe l'inclinaison de la droite et $b$ l'endroit où elle coupe l'axe des $y$ ; $(x - 3)^2$ déplace $y = x^2$ de $3$ vers la droite et $(x + 4)^2$ de $4$ vers la gauche. La suite $1, 3, 5, 7, 9$ a pour terme général $a_n = 2n - 1$ et la suite $3, 6, 12, 24, 48$ a pour terme général $a_n = 3 \cdot 2^{\,n-1}$ . La division longue donne $\frac{x^2 + 3x + 5}{x - 1} = (x + 4) + \frac{9}{x - 1}$ , donc loin de $x = 1$ la courbe suit la droite $y = x + 4$ .

### Deutsch

Eine Formel nimmt Zahlen auf und gibt genau eine Zahl aus. In $y = mx + b$ legt die Steigung $m$ fest, wie steil die Gerade ist, und $b$ , wo sie die $y$ -Achse schneidet; $(x - 3)^2$ verschiebt $y = x^2$ um $3$ nach rechts und $(x + 4)^2$ um $4$ nach links. Die Folge $1, 3, 5, 7, 9$ hat $a_n = 2n - 1$ , die Folge $3, 6, 12, 24, 48$ hat $a_n = 3 \cdot 2^{\,n-1}$ . Die Polynomdivision ergibt $\frac{x^2 + 3x + 5}{x - 1} = (x + 4) + \frac{9}{x - 1}$ , weit weg von $x = 1$ folgt der Graph also der Geraden $y = x + 4$ .

### Русский

Формула получает числа на входе и выдаёт одно число на выходе. В $y = mx + b$ угловой коэффициент $m$ задаёт крутизну прямой, а $b$ — точку пересечения с осью $y$ ; $(x - 3)^2$ сдвигает $y = x^2$ на $3$ вправо, а $(x + 4)^2$ — на $4$ влево. У последовательности $1, 3, 5, 7, 9$ общий член $a_n = 2n - 1$ , у последовательности $3, 6, 12, 24, 48$ — $a_n = 3 \cdot 2^{\,n-1}$ . Деление многочленов уголком даёт $\frac{x^2 + 3x + 5}{x - 1} = (x + 4) + \frac{9}{x - 1}$ , поэтому вдали от $x = 1$ график идёт вдоль прямой $y = x + 4$ .
