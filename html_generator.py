head = ['1.Computer', '2.Computer Program','3. Programming Language', '4.Python',  '5.Python Grammar', '6.Variables in Python','7. Strings in Python','8. Functions and Procedures', '9.Loops','10. Structured Data']
concepts = """Title: Computer
Description: Most machines are designed to do few things, but computers cannot do anything on its own, unless you write programs to instruct them to do many things. Computer is an electronic device for storing and processing data according to instructions given to it in a program.
Title: Computer Program
Description: Program is a set of instructions that programmers write to instruct computer to what to do. Some examples are Web browsers, games, apps and so on.
Title: Programming Language 
Description: Programming Language, like Python is a language that programmers use to write set of instructions that in turn instructs the computer to what to do.
Title: Python
Description: Python is an programming language. It converts the code into the language computer understands and executes.
Title: Python Grammar
Description: Python Grammar are set of rules that programmers follow while writing the code. It is the same as we have English grammar rules. In Python, we have expression, followed by operation, followed by expression. Expression can be replaced either by another expression or numbers (0,1,...). Operation is what kind of operations we want to do with those numbers. In short, we have to follow set of rules while coding so that computer can interpret and execute correctly.
Title: Variables in Python
Description: We use variables to give names to values. For example if speed_of_car is a variable with a value of 20, then the following code would print out 2000: 
 print 100 * speed_of_car
Title: Strings in Python
Description: String is a sequence of characters in a quote or quotes.  For example:
 name = 'Dave' 
 print 'Hello ' + name 
The result will be Hello Dave
Title: Functions or Procedures
Description: A function takes an input, processes it and then produces an output. We can code this by using the keyword def and then writing function name followed by the function parameters in parentheses. In the next line, we write the code that specifies what to do with the input parameters. When this procedure is called, the parameters are replaced by actual values
Title: Loops 
Description: A while loop statement in Python programming language repeatedly executes a single statement or a block of statements till test expression is true.
When the test expression becomes false, program control passes to the line immediately following the loop. The while loop might not ever run. When the condition is tested and the result is false, the loop body will be skipped and the first statement after the while loop will be executed
Title: Structured Data 
Description: We learned two ways of structuring data: Strings and Lists.
Strings are the most popular types in Python. We can create them by enclosing sequence of characters in quotes and assigning it to the variable. Python treats single quotes the same as double quotes. 
Lists: It is a most versatile data type available in Python. It can be written as a list of values separated by commas between square brackets. Important thing about a list is that value can be sequence of anything like strings, numbers and so on. Lists can even contain other lists."""




def contents(headings):
	html_head = ‘’
	for e in headings:
		html_head =  html_head + '''
		''' +  e
	html_head_1 = '''
  <div class="tableofcontents">
	''' + html_head
	html_head_2 = '''

  </div>'''
	full_head = html_head_1 + html_head_2
	return full_head

def generate_concept_html(def_title, def_description):
	html_concept_1 = '''
   <div class = “lesson4”>
	<div class = “def-title”>
	''' + def_title
	html_concept_2 = ‘’’
	</div>
       	<div class = “def-description”>
	''' + def_description
	html_concept_3 = '''
	</div>
    </div>'''
	html_all = html_concept_1 + html_concept_2 + html_concept_3
	return html_all



def generate_all_html(text):
	all_html = ''
	counter_title = 0
	counter_descrip = 0
	counter = 0
	while counter < len(text):
		counter1 = text.find('Title:',counter_title)
		if counter1 < 0:
			break
		counter2 = text.find('Description:',counter_descrip)
		title = text[counter1+7 : counter2-1]
		counter3 = text.find('Title:' , counter1+1)
		description = text[counter2+13 : counter3-1]
		html = generate_concept_html(title,description)
		all_html = all_html + html
		counter_title = counter1 + 1
		counter_descrip = counter2 + 1
		counter = counter + 1
	return all_html

print contents(head) 
print generate_all_html(concepts)



