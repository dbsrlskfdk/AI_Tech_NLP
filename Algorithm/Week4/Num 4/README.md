# 방정식 풀이
[문제 링크](https://www.acmicpc.net/problem/6594)
## 문제 설명

<p>변수가 한 개인 일차 방정식이 주어졌을 때, 해를 구하는 프로그램을 작성하시오.</p>


## 입력

<p>입력을 여러 개의 방정식으로 이루어져 있다. 방정식은 한 줄에 하나씩 주어진다.</p>

<p>방정식은 모두 100글자 이내이며, 아래와 같은 문법을 따른다. (EBNF 문법)</p>

<pre>
Equation   := Expression &#39;=&#39; Expression
Expression := Term { (&#39;+&#39; | &#39;-&#39;) Term }
Term       := Factor { &#39;*&#39; Factor }
Factor     := Number | &#39;x&#39; | &#39;(&#39; Expression &#39;)&#39;
Number     := Digit | Digit Number
Digit      := &#39;0&#39; | &#39;1&#39; | ... | &#39;9&#39;</pre>

<p>위의 문법에 따르면, x*x = 25와 같은 일차방정식이 아닌 식을 만들 수 있다. 하지만, 항상 x에 대해서 일차인 식만 주어진다. 또,&nbsp;방정식의 부분식도 항상 일차이다. 즉, x*x-x*x+x = 0과 같은 식은 주어지지 않는다. (x*x는 일차식이 아니다)</p>

<p>입력으로 주어지는 숫자는 모두 음이 아닌 정수이다. 또, x는 실수이다.</p>


## 출력
<p>각 테스트 케이스에 대해서, &quot;Equation #i&quot; (i는 테스트 케이스 번호)를 출력한 다음, 아래 세 가지 중 하나를 출력한다.</p>

<p>방정식이 해가 없다면, &quot;No solution.&quot;을 출력한다.<br />
방정식의 해가 무수히 많다면, &quot;Infinitely many solutions.&quot;을 출력한다.<br />
방정식의 해가 하나라면, &quot;x = solution&quot;을 출력하며, solution은 소수점 여섯째 자리까지 출력한다.</p>

<p>각 테스트 케이스 사이에는 빈 줄을 하나 출력한다.</p>

