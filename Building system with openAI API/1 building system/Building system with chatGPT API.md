
<hr>


Large Language Model 
-----
model made by using supervised learning (x -> y) to repeatedly predict the next word.
For example , say 

$\underbrace{(\textcolor{cyan}{\text{I love eating}})}_\text{prompt}$ _ _ _ _ _ _ _ _ _ _ _ _ <br>
$\text{bagels with cream cheese}$ , <br>
$\text{my mother's butter chicken}$ , <br>
$\text{out with my friends}$

<hr>

 #### Base LLM 
Predicts next word based on a text training data
	
E.g Once upon a time, there was a unicorn ----> that lived in a magical forest with all other unicorns
		
e.g what is the capital of France ? 
	gives the answer from model on various web searches 
	
<hr>

#### Instruction tuned LLM
train these base LLM on a lot of data 
and 
+ further fine tune the model to follow an specific output instruction
+ obtain ratings from human whether helpful or not 
+ tune LLM to increase probability that it generates more highly rated outputs using RLHF(reinforcement learning using human feedback)

----

### System, User and Assistant Messages 

System → sets tone/behaviours of assistant 

assistant → LLM response 

user → prompts 

   
