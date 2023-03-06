# Sanderson-Advice-CLI
CLI tool to get writing advice from Brandon Sanderson's lectures (may add more resources, but [Sanderson's lectures](https://www.youtube.com/watch?v=0cf-qdZ7GbA&list=PLSH_xM-KC3Zv-79sVZTTj-YA6IAqh8qeQ) are such a fantastic resource. I decided not to use a vector database or cloud hosting for this little project because I want it to be more accessible to authors / have no interest in monetizing it.

# Example Output

**Ask brandon anything**: *What is your favorite method of plotting a book?*

Well hello there! As Brandon Sanderson, I have to say that my favorite method of plotting a book really depends on the story that I am trying to tell. However, in general, I tend to plot out different character arcs and plotlines separately before weaving them together into one cohesive story. For example, for my Stormlight Archive series, I focused on Dalinar's plot for a while before skipping back and forth to make sure the reader is getting conclusions to both plotlines in the same book. It's also important to make sure plotlines are short enough to fit within the same book and to have a through line to connect the different plotlines. 

In terms of brainstorming a plot, I tend to have a mix of simmering ideas for a long time before I actually sit down to make the story. Once I do start, I generally take a plot archetype and identify the important elements I want to use. I'm open to using different plot structures such as the Hero's Journey or the Three Act Format, but I also like to experiment with them to create something unique. Most importantly for me, I like to create satisfying and relatable character arcs and plotlines that really resonate with readers. As for discovery plotting, I don't personally use it as much, but the "yes, but/no, and" method can be quite helpful for those who do.

Next steps? (l- open link | n- new question | q- quit)

> *n*

**Ask brandon anything**: *What is the yes, but/no, and method?*

The "yes, but/no, and" method is a technique used in writing to create a sense of motion for the characters and keep the stakes of the story high. It involves presenting a problem and then either adding a complication to it with a "yes, but" or escalating it to a bigger problem with a "no, and". This creates a sense of tension and conflict in the story, which helps to keep readers engaged. As you write, you can use this method to ensure that everything is always getting worse for your characters, which is essential in a discovery written story. However, after you finish writing, you can then go back and try to connect all the pieces together into a larger plot. There are many other methods available online, and I encourage writers to research and try different methods to see what works best for them.

Next steps? (l- open link | n- new question | q- quit)

> [l](https://www.youtube.com/watch?v=Qgbsz7Gnrd8&t=4117s&ab_channel=BrandonSanderson)            

Next steps? (l- open link | n- new question | q- quit)

> *n*

**Ask brandon anything**: *When should I self-publish my book?*

Self-publishing can be a good option for authors who want more control over their book's cover, back flap summary, pricing, and sales. One of the benefits of self-publishing is that you get to decide when your book is up for sale and when it's not, as well as what promotions you want to be part of. Additionally, self-publishing can be a good option for authors who are worried about signing a contract that gives the publisher the right to publish their book for life, as many print rights contracts are. However, it's important to note that self-publishing does require authors to put in extra effort to promote and market their book.

Next steps? (l- open link | n- new question | q- quit)

> *q*


# Installation/Setup

Install Python
```
# for Mac
brew install python
```

Clone repo, create a virtual environment and install dependencies
```
git clone ___
cd Sanderson-Advice-CLI
python3 -m venv .venv
pip3 install -r requirements.txt 
```

Set up your [OpenAI API key](https://platform.openai.com/account/api-keys).
```
export OPENAI_API_KEY=[Your API Key]
```
This uses the new, incredibly cheap ChatGPT API, so each question should come out to around $.001. Using the free $18 credits that OpenAI offers, means you get 18,000 questions to ask!!


# Usage

Runs in the terminal, simply run the advice script
```
python3 advice.py
```
Ask any questions you have and after receiving a response, either:
 - Proceed (using 'n') to ask a new question
 - View Youtube clip (using 'l') which the algorithm is referencing
 - Quit (using 'q')

# Future Work
