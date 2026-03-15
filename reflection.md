# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

* The system said "go lower" when I am guessing 15 but the correct answer is 18. I would expect the system tells me go higher. 
* When you type a value out of range 0 - 100, the system would not catch you, it would tell you go lower / higher instead, which is misleading. I would expect the system catch a invalid input error. 
* The initial score started at -5. I expect it starts at zero. 
* There is no choice for difficulty levels

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

* I use AI tools as my studying pal. For ChatGPT, I usually asked it for how to tidy my plotting code or help me make my machine learning function more chunky and easy maintinable. For Claude, I usually asked it for cover letter help and resume tweak. 
* AI is correct: sometimes I need to do a train test split and I forget certain functions name in Python (as I use R for most of my time), I'll make ChatGPT help with my existing code, and if I see the result matching my expectation, I know it's correct
* AI is incorrect: sometimes when I do a plotting and asking for some adjusts, AI will just throw me a function with a fake parameter (which would cause error for my code running), then I know they are broken. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

* First I tried to reproduce the bug and understand when it happened. After making changes, I checked if the same situation still caused the problem. I tested both by running the Streamlit app manually and by writing small test cases for the functions. If the behavior matched what I expected and the bug didn’t appear anymore, I considered it fixed
* for `test_parse_guess_out_of_range()`, originally the game would still accept numbers like 150 and give a “higher/lower” hint, which was confusing. This test helped confirm that the function now correctly detects out-of-range inputs and returns an error instead
* Yes. I used Copilot to help think of test cases for the bugs I found. For example, it suggested testing the parse_guess function directly instead of only checking the behavior through the UI. That made it easier to verify that the input validation was working correctly
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
