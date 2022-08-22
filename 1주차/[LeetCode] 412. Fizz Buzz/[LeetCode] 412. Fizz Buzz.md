Given an integer n, return a string array answer (**_1-indexed_**) where:

- answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
- answer[i] == "Fizz" if i is divisible by 3.
- answer[i] == "Buzz" if i is divisible by 5.
- answer[i] == i (as a string) if none of the above conditions are true.
 

**Example 1:**
<pre>
<code>
Input: n = 3
Output: ["1","2","Fizz"]
</code>
</pre>

**Example 2:**
<pre>
<code>
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
</code>
</pre>

**Example 3:**
<pre>
<code>
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
</code>
</pre>

**Constraints:**

- 1 <= n <= 10^4