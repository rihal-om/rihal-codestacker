# Machine Learning Challenge


### Overview
Imagine yourself as a data scientist in a busy news organization, where articles come in every minute. It's crucial to categorize, summarize, and caption these articles quickly. To keep up with the fast-paced world of news, your challenge is to automate this process by developing a system that accurately categorizes news articles into 24 distinct groups and generates captivating abstracts and captions that capture the essence of each article.

### Problem Statement
The New York Times, an excellent source of news, has provided us with a unique dataset called N24News. This dataset contains 24 categories of news, each with a headline, abstract, article body, image, and image caption. Your challenge is to develop a machine learning model that can accurately categorize news articles into their respective categories, generate insightful abstracts, and captivating captions.


### Objective:

The objective of this challenge is to create a system that can:

**Level 1: The Basics** *(40 points)*
- Develop a model that can categorize news articles into their respective categories.

**Level 2: The Intermediate** *(20 points)* 
- Generate abstracts that provide a clear and concise summary of the article.

**Level 3: The Advanced** *(20 Bonus Points)*
- Generate captions for each news article's image that accurately reflect the content.

**Level 4: The Mastery** *(20 Bonus Points)* 
- Implement a real-time UI web app for inference where it allows the user to upload an article body, image, and a title, and then return its category, a caption, and an abstract (you could use tools such as Streamlit or Gradio).

**Level 5: The Hero** *(10 Bonus Points)* 
- Detect if the news article is related to Palestine and categorize it under a new subcategory called "FreePalestine".


### Technical Guidance:
- You are free to use any tools and techniques you find appropriate, but **Python** is the preferred programming language.
- Using **cloud-based** LLMs (Large Language Models), including OpenAI's GPT models API, **is prohibited**.

### Expectations:
The following are expected to be included in the solution to this problem: 
- Data analysis and exploring the dataset.
- Data preprocessing. 
- A machine learning/ Deep learning model. 
- Evaluate the model’s performance. 
- Clear code documentation. 
- Thoroughly explain your work at each step by using the markdown cell blocks in your notebook or code comments.
- Write your thoughts for further improvements.

### Data Description:
The [N24News](https://arxiv.org/pdf/2108.13327v4.pdf) dataset contains news articles from the New York Times with 24 categories, including both text and image information. Each article sample contains one category tag, one headline, one abstract, one article body, one image, and one corresponding image caption.

### Submission:
- Please submit your solution in a well-documented Jupyter Notebook. 
- Show model evaluation results.
- Include examples of inference results showcasing how your model categorizes news articles, generates abstracts, captions, etc.
- Include clear instructions on how to run your code.
- Make sure all libraries used are included in a requirements.txt file.
- If applicable, include screenshots or recordings demonstrating your real-time UI web app functionality.

The Rihal Codestacker Challenge offers an exciting opportunity to showcase your skills in machine learning and data science.  Participating in this challenge could open doors for you to join the amazing team at Rihal. We look forward to seeing your solution! 🚀🔥

_____
 
> **To Download the dataset:** 
https://drive.google.com/file/d/1OS1fXwZ1Vsj70lEQajccyssxQRYp5X9D/view?usp=share_link

> **Important Note**: Please use the data in `nytimes_train.json` file for training and the `nytimes_test.json` file for evaluation.
 