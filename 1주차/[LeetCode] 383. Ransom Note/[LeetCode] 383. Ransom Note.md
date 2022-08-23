Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

   
Each letter in magazine can only be used once in ransomNote.   


**Example 1:**
<pre>
<code>
Input: ransomNote = "a", magazine = "b"
Output: false
</code>
</pre>



**Example 2:**
<pre>
<code>
Input: ransomNote = "aa", magazine = "ab"
Output: false
</code>
</pre>


**Example 3:**
<pre>
<code>
Input: ransomNote = "aa", magazine = "aab"
Output: true
</code>
</pre>

**Constraints:**

- 1 <= ransomNote.length, magazine.length <= 105
- ransomNote and magazine consist of lowercase English letters.