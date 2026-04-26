Deep learning > Machine Learning > Artificial Intelligence 

## Artificial intelligence:

**Artificial intelligence:**

​	A technique which enables machines to mimic human behavior.

**Machine Learning:**

​	Subset of AI techniques which use statistical methods to enable machines to imporove with experience.

**Deep Learning:**

​	Subset of ML which make the computation of multi-layer neural network feasible.

​	ML techniques that teaches computers to process data in way that is inspired by the human brain.

![AI](https://github.com/hojat-gazestani/Notes/blob/MachineLearning/machine-learning/pic/01-Artificial-intelligence.png)






**A human brain:**

​	Contains millions of interconnected neurons  that work together to learn and process information.
![Human](https://github.com/hojat-gazestani/Notes/blob/main/machine-learning/pic/02-human-brain.png)

**Neural Network:**

​	At the heart of Deep Learning are Artificial Neural Networks. Which are <u>algorithms</u> inspired by the structure and function of the <u>brain</u>.

![NN](https://github.com/hojat-gazestani/Notes/blob/main/machine-learning/pic/03-neural-network.png)

**Artificial neural networks:**

​	are made of <u>many layer</u> of artificial neuron that work together inside the <u>computer</u>.

**Automates feature extraction:**

​	removing some of the <u>dependency</u> on human <u>experts</u>.

**Layers of Neurons:**

​	Deep learning models consist of layers of interconnected nodes or neurons, and deep refers to the number of layers through which the dat is transformed.

**Learning from Unstracutred Data:**

​	Deep learning excels at learning from unstractured data like images, text, or sound. 

​	<u>Example:</u>

​		Recognizing faces in images using Convolutional Neural Networks(CNNs)

**Large Data Requirements:**

​	Generally requires large amount of labeled data for training.



## Neural Network:

​	A neural network is a machine learning program, or model, that makes decisions in a manner similar to the human brain, by using proccesses that mimic the way biological neurons work together to identify phenomena.	

**Structure**:

​	Comprised of layers of interconnected nodes, or neurons, including input layers, hidden layers (one or more) and an output layer.

**Neuron Functionality:**

​	Each neuron performs a simple calculation (like weighted sum followed by a non-linear function) on its inputs.

**Learning Process:**

​	Neural netowrks learn to perform tasks by considering examples, generally without task-specific programming. For example, they might learn to identify images that contain cats by analyzing examples of cat images and non-cat images.

**Weights and Biases:**

​	Connections between neurons have <u>weights</u> that adjust as learning <u>proceeds</u>. The network also uses <u>biases</u>, an extra input to nodes (neurons) in each layer to help them make better decisions.



## LLM

​	Large Language Models (LLMs) are sophisticated AI systems designed for proccessing, understanding, and generating human language.

**Scale and Complexity:**

​	LLMs are composed of millions or <u>billions</u> of <u>parametes</u>, making them highly complex, Example: GPT-4, with its vast number of parameters, can generate human-like text.

**Learning method:**

​	Most LLMs use a form of deep learning called transformers, which are effective at proccessing sequences of data. Example: GPT-4's transformer architecture enables it to understand and predict language sequences efficiently.

**Continual Learning:**

​	Many LLMs are designed to continually learn and improve over time with more data and user interaction. Example: GPT-4's performance can imporve as it is exposed to more diverse and extensive user interaction.

**Customization:**

​	Some LLMs offer customization options for specific industries need or user performance. Example: GPT-4 can be fine-tuned for specialized tasks like legal analysis or medical advice, although with limitations.



## Into to Meta Llama 3.2/3.3

Https://llama.com

Llama 1B -> Billions of Parameters

**Parameters:**

​	In a neural network are the internal <u>variable</u> that the model learns during <u>training</u>. Includes <u>weights</u>, <u>biases</u>, that determine how the model processes and generates <u>information</u>. models with more parameters also require more <u>computational</u> resources and memory.



<u>Accuracy:</u> Properly tuned parameters enable the model to make precise predictions, improving oerall performance.

<u>Learning Complex Patterns:</u> More parameters allow the model to capture intricate data patterns, enhancing its ability to solve complex tasks.

<u>Generalization:</u> Well-adjusted parameters help the model generalize well to new, unseen data, ensuring reliability in real-world applications.



**Understanding by example:**

<u>Parameter 1:</u> Tea Type (Black, Green, Herbal)

<u>Parameter 2:</u> Water Temperature (70C, 85C, 100C)

<u>Parameter 3:</u> Brewing Time (2 mins, 3 mins, 4 mins)

**Real World Example:**

<u>Parameter 1:</u> Edge detection sensitivity (How sensitive the model is to edges in the image).

<u>Parameter 2:</u> Color saturation (How much the model focuses on the colors in the image, like the fur color of cats or dogs)

<u>Parameter 3:</u> Shape recognition (How the model detects features like ears, noses, and body shape)



## Models benchmark

![benchmark](https://github.com/hojat-gazestani/Notes/blob/main/machine-learning/pic/04-llama.png)



## Transformer

What is Transformer Model?
 It is a device that transfers electric energy from one cyrcle to another cyrcle.

​	Transformers are a type of neural network architecture that hve revolutionized the field of natural language processing (NLP). Here are some key points about transformer models:

1. Architecture: Transformers use a unique architecture primarily based on <u>self-attention</u> mechanisms, allowing them to <u>weigh</u> the importance of different parts of the <u>input</u> data.
![Transformer](https://github.com/hojat-gazestani/Notes/blob/main/machine-learning/pic/05-transformers.png)

2. Parallel Proccessing: Unlike previous sequence-based models like RNNs and LSTMs, transformers process entire sequences of data in parallel, significantly speeding up training and inference times.
3. Attention Mechanism: The core of the transformer is the <u>attention mechanism</u>, which allows the model to focus on different parts of the input sequence when producing output, enhancing it ability to understand context and relationships in the data.
4. ![Attention](https://github.com/hojat-gazestani/Notes/blob/main/machine-learning/pic/06-attention.png)

Context:

*Sentence 1: The **bank** of the river.

*Sentence 2: Money in the **bank**



4. No Recurrence: Transformers do not require  recurrent layer. This absence of recurrence means they can handle longer sequences of data in moer effectively than RNNs and LSTMs.
5. Scalability: The parallel nature of transformers makes them highly scalable with increased data and computaional resources, leading to improvements in performance.
6. Layer Structure: A typcal transformer model consists of an encoder and a decoder, each comprising multiple layers of self-attention and feed-forward neural networks.
![Layer](https://github.com/hojat-gazestani/Notes/blob/main/machine-learning/pic/07-layer.png)

7. Application in NLP: Transformers have become the backbone of many state-of-the-art NLP models, used in tasks like machine translation, text generation, summarization, and question-answering.
8. BERT and GPT: Notable implementaions of transformer models include BERT (Bidirectional Encoder Representation from Transformers) for understanding context in language, and GPT (Generative Pre-Transformer) for generating human-like text.
9. Beyound NLP: While initially designed for NLP tasks, the transformer architecture has also been adapted for use in other areas, such as computer vision and audio proccessing.



## Embedding

An embedding is a way of <u>converting</u> the <u>features</u> of an object, like a <u>word</u>, into <u>vectore</u> of real numbers.![Screenshot 1404-10-28 at 12.15.46 AM](/Users/hojat/Pictures/ScreenShot/Screenshot 1404-10-28 at 12.15.46 AM.png)

**Transforming Data:** Embeddings turn complex data (like words or pictures) into vector or a list of numbers that a computer can understand and work with.

**Finding Similarities:** They help find similarities between items. For example, in word embeddings, similar words are represented by numbers that are close together.

**Making Data Smaller:** They help make big, complicated data simpler and smaller, so it's easier for computers to handle.

**Used Everywhere:** Embeddings are used in many areas, like helping computers understand language or recommend things you might like.

**Different Types:** Word2Vec (Google) / GloVe (Global Vectors for Word Representation) / BERT (Bidirectional Encoder Representaions from Transformers.)

**Learning From Data:** Computers can learn to create these embeddings by looking at lots examples, which helps them understand and predict new, unseen data.

**Improving Understanding:** Some advanced embedding can even understand the context, meaning they can tell the difference in meaning when a word is used in different ways.



## Quantization

Quantization is a process of reducing the precision of numbers used to represent a model's parameter.

Quantization in AI reduces number precision to make models smaller and faster, with minimal impact on accuracy.

Example: Comressing High Quality image to Smaller size.![Screenshot 1404-10-28 at 12.32.50 AM](/Users/hojat/Pictures/ScreenShot/Screenshot 1404-10-28 at 12.32.50 AM.png)



**Reduces model size:** Makes AI models smaller, so they take up less memory.

**Speeds up processing:** Simplifies calculations, making models faster to run.

**Saves energy:** Uses less computing power, which is greater for devices like phones or edge devices.



TradeOffs

**Slight accuracy loss:** Reducing precision may cause minor error, but modern techniques often minimize this.

**More complex training:** Some models need special adjustments to work well with quantization.



## Quantize length

Context lenght refers to the maximum amount of text (tokens) that the model can remember and process.



Click on **model card on Github**

![Screenshot 1404-10-28 at 12.41.18 AM](/Users/hojat/Pictures/ScreenShot/Screenshot 1404-10-28 at 12.41.18 AM.png)



Context length

![Screenshot 1404-10-28 at 12.42.14 AM](/Users/hojat/Pictures/ScreenShot/Screenshot 1404-10-28 at 12.42.14 AM.png)



explain

![Screenshot 1404-10-28 at 12.42.47 AM](/Users/hojat/Pictures/ScreenShot/Screenshot 1404-10-28 at 12.42.47 AM.png)









### Why it's important?

**Short Context Length:** Works well for simple or short tasks (e.g. completing a sentence)

**Longer Context Length:** Needed for complex tasks. (e.g. summarizing a long article or holding a detailed conversation )



### Understand by example:

Imagine you are telling a story to a friend, but they can only remmeber the last 5 sentences you said:

1. You start with "Once upon a time, there was a brave knight"
2. You keep adding details, but once you reach the 6th sentence, your friend forgets the first one. 

Similarly, an AI with a context length of  5 tokens can only "focus" on the last 5 tokens of text at time.



### How it works:

**AI Reads the input:** The model processes and *remembers* the input text generate relevent response.

**Limit on Memory**: it can only be*remember* up to a certain number of words or tokens (a unit of text like words or parts of words)

**Older Context Gets Forgotten**: When the input exceeds the context length, older parts are forgotten, and only the most recent input is used.