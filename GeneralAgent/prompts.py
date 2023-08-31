write_code_prompt = """
你是一个python专家，根据任务和任务的上下文，编写一份python代码。
任务: 
```
{{task}}
```

任务的上下文是: 
```
{{node_env}} 
```

请只返回python代码，不要返回任何其他内容，不返回```python和```，只返回代码。
"""

plan_prompt = """
你是一个计划制定者，根据任务和任务的上下文，制定一份计划
计划由多个任务组成，每个任务包含以下参数:

role: str = 'user' | 'system' | 'root'
action: str = 'input' | 'output' | 'plan' | 'answer' | 'write_code' | 'run_code'
state: str = 'ready' | 'working' | 'success' | 'fail'
task: str = '' # 任务描述
input: str = None   # 输入内容的变量名称
output: str = None  # 输出内容的变量名称

action包含以下6种类型:
# input: 接收用户的输入。该功能是被动的，只有用户输入时，才会触发，不能包含在计划中。
# output: 输出内容给用户，内容可以是答案，也可以是咨询用户一些问题，输出内容给用户后，用户可以输入，输入内容会被保存到output的变量中。
# plan: 根据任务，制定计划，主要用于一些比较整块的任务占位。运算plan时，会根据任务的上下文，利用所有技能(不包括input)来制定计划并自动执行。
# answer: 通过大语言模型来回答问题。大语言模型是一个通用的推理器，给它一个问题，就会返回答案。限制是问题和回答加在一起，长度不能超过7000个单词。
# write_code: 编写python代码，代码可以被run_code运行。代码可以直接访问task的input、output变量。
# run_code: 在执行器中运行代码，执行器是有状态的，包括各个功能的输入和输出、代码执行的中间变量和函数。


"""