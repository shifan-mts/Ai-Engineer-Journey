---
budget: ₹0 target; prefer local models and free resources
daily_time: 3h (up to 5h on selected days)
description: Learn neural-network fundamentals with Andrej Karpathy,
  then build LLM applications and agent workflows with the freeCodeCamp
  Agentic AI course.
duration: 30
id: ai-engineering-30-day-roadmap
milestones:
- day: 7
  title: Implemented micrograd and a small language model
- day: 14
  title: Understood transformer fundamentals and built a tiny GPT
    experiment
- day: 21
  title: Built a basic agent and LangGraph workflows
- day: 30
  title: Built and deployed a small RAG-enabled AI application
start_date: 2026-11-11
title: AI Engineering --- 30-Day Build-While-Learning Roadmap
version: 1
---

# AI Engineering --- 30-Day Roadmap

**How to use this roadmap**
-   **Normal day:** approximately 3 hours.
-   **Optional intensive day:** up to 5 hours; use the extra time for
    implementation, debugging, and revision, not more passive video
    watching.
-   **Learning rule:** use the exact video start/stop points listed under each video task. Stop at the endpoint, then implement before watching further.
-   **AI rule:** use Qwen3:8B or Gemma4:12B locally for hints,
    explanations, and bounded code assistance. Do not let an agent
    implement an entire lesson for you.
-   **Budget:** target ₹0. Use local Ollama models where practical. If a
    course example requires a hosted API, first check whether the lesson
    can be adapted to a local model or a mocked response.
-   **Scope:** this is a 30-day foundation, not a promise to master deep
    learning or finish every large course project.

**Primary course references**
-   Andrej Karpathy --- Neural Networks: Zero to Hero:
    https://karpathy.ai/zero-to-hero.html
-   Karpathy course repository and exercises:
    https://github.com/karpathy/nn-zero-to-hero
-   freeCodeCamp --- Agentic AI Complete Course:
    https://youtu.be/Zy7EXDONlTY
-   Course code repository:
    https://github.com/entbappy/Complete-Agentic-AI-Course

------------------------------------------------------------------------

**Video timestamp rule**
- Start at the first timestamp and stop at the second timestamp shown in that task.
- Do not continue watching ahead before completing the practical task.
- Timestamp ranges refer to the original videos linked in each task. For the freeCodeCamp course, the selected ranges are intentionally limited excerpts; you do not need to finish the full 22-hour video in this 30-day plan.

------------------------------------------------------------------------

## Day 01 - Neural Networks and Computational Graphs

**Topics**
-   What a neural network does at a high level
-   Scalars, functions, inputs, weights, and outputs
-   Computational graphs
-   Derivatives and the intuition behind gradients

### Tasks

-   [ ] `D01-T01` Watch the introductory part of Micrograd
    -   Estimate: 45m
    -   Type: learning
    -   Reference: https://youtu.be/VMj-3S1tku0
    -   Video stop: **00:25 → 32:10** (31m 45s). Stop after the `Value` object and graph setup; then draw your own graph.
-   [ ] `D01-T02` Work through simple derivatives and the chain rule
    -   Estimate: 45m
    -   Type: learning
    -   Reference: https://www.3blue1brown.com/topics/calculus
-   [ ] `D01-T03` Draw a computational graph for a small expression and
    calculate its output
    -   Estimate: 60m
    -   Type: practical
-   [ ] `D01-T04` Write a short explanation of a neuron, weight, bias,
    and gradient
    -   Estimate: 30m
    -   Type: revision

### Resources

-   https://youtu.be/VMj-3S1tku0
-   https://github.com/karpathy/micrograd
-   https://www.3blue1brown.com/topics/calculus

### Completion Criteria

You can draw a small computational graph, calculate its forward value,
and explain what a derivative tells you.

------------------------------------------------------------------------

## Day 02 - Micrograd: Autograd and Backpropagation

**Topics**
-   The `Value` object
-   Forward computation
-   Local derivatives
-   Chain rule and backward propagation

### Tasks

-   [ ] `D02-T01` Continue the Micrograd lecture and inspect the
    reference implementation
    -   Estimate: 45m
    -   Type: learning
    -   Reference: https://youtu.be/VMj-3S1tku0
    -   Video stop: **32:10 → 1:27:05** (54m 55s). Stop after the graph-level backward pass and repeated-node bug; then implement it yourself.
-   [ ] `D02-T02` Implement a minimal `Value` class with arithmetic
    operations
    -   Estimate: 75m
    -   Type: practical
-   [ ] `D02-T03` Implement and test backward propagation for supported
    operations
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D02-T04` Compare your gradients with a numerical
    finite-difference check
    -   Estimate: 15m
    -   Type: practical
### Resources

-   https://youtu.be/VMj-3S1tku0
-   https://github.com/karpathy/micrograd

### Completion Criteria

Your small autograd engine calculates gradients for a simple expression,
and you can explain how the chain rule is applied.

------------------------------------------------------------------------

## Day 03 - Building a Tiny Neural Network

**Topics**
-   Neurons and layers
-   Forward pass
-   Loss
-   Gradient descent
-   Updating parameters

### Tasks

-   [ ] `D03-T01` Finish the Micrograd neural-network walkthrough
    -   Estimate: 45m
    -   Type: learning
    -   Reference: https://youtu.be/VMj-3S1tku0
    -   Video stop: **1:27:05 → 2:14:03** (46m 58s). Stop after the MLP training walkthrough; then build and train your tiny network.
-   [ ] `D03-T02` Implement a neuron, layer, and multilayer perceptron
    using your `Value` class
    -   Estimate: 75m
    -   Type: practical
-   [ ] `D03-T03` Train on the small example dataset from the lesson
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D03-T04` Record the loss before and after training and explain
    the change
    -   Estimate: 15m
    -   Type: revision

### Resources

-   https://youtu.be/VMj-3S1tku0
-   https://github.com/karpathy/micrograd

### Completion Criteria

You can run a forward pass, calculate a loss, backpropagate, update
parameters, and observe the loss decrease on the lesson's small example.

------------------------------------------------------------------------

## Day 04 - Language Modelling and Bigram Models

**Topics**
-   What a language model predicts
-   Character-level tokenisation
-   Bigram probabilities
-   Training data and sampling

### Tasks

-   [ ] `D04-T01` Watch Makemore Part 1
    -   Estimate: 60m
    -   Type: learning
    -   Reference: https://youtu.be/PaCmpygFfXo
    -   Video stop: **00:00 → 36:17** (36m 17s). This covers dataset exploration, bigram counts, sampling, and the start of efficient normalization; then implement the count-based model.
-   [ ] `D04-T02` Prepare a small text dataset and build a character
    vocabulary
    -   Estimate: 30m
    -   Type: practical
-   [ ] `D04-T03` Implement a count-based bigram model
    -   Estimate: 60m
    -   Type: practical
-   [ ] `D04-T04` Sample generated names and inspect the results
    -   Estimate: 30m
    -   Type: practical
### Resources

-   https://youtu.be/PaCmpygFfXo
-   https://github.com/karpathy/makemore

### Completion Criteria

Your bigram model can learn character transition probabilities and
generate sample names from the dataset.

------------------------------------------------------------------------

## Day 05 - Neural Bigram Model and Loss

**Topics**
-   One-hot encoding
-   Neural network view of a bigram model
-   Softmax
-   Negative log likelihood
-   Training and sampling

### Tasks

-   [ ] `D05-T01` Revisit the neural-network portion of Makemore Part 1
    -   Estimate: 45m
    -   Type: learning
    -   Reference: https://youtu.be/PaCmpygFfXo
    -   Video stop: **1:02:57 → 1:56:16** (53m 19s). Focus on the neural bigram dataset, one-hot inputs, linear layer, softmax, loss, backward pass, and sampling; then implement and train the neural bigram model.
-   [ ] `D05-T02` Implement the neural bigram model using PyTorch
    tensors
    -   Estimate: 60m
    -   Type: practical
-   [ ] `D05-T03` Calculate the loss and train the model
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D05-T04` Compare generated samples with the count-based bigram
    model
    -   Estimate: 30m
    -   Type: practical
### Resources

-   https://youtu.be/PaCmpygFfXo
-   https://pytorch.org/tutorials/beginner/basics/intro.html

### Completion Criteria

You can explain the difference between a count-based bigram model and a
neural bigram model, and can interpret the training loss.

------------------------------------------------------------------------

## Day 06 - MLP Language Model and Embeddings

**Topics**
-   Character embeddings
-   Context windows
-   Multilayer perceptrons
-   Training/validation split
-   Overfitting

### Tasks

-   [ ] `D06-T01` Watch Makemore Part 2
    -   Estimate: 60m
    -   Type: learning
    -   Reference: https://youtu.be/TCH_1BHY58I
    -   Video stop: **09:03 → 56:20** (47m 17s). Focus on dataset construction, embeddings, MLP layers, loss, training, and mini-batches; then implement the context-window MLP.
-   [ ] `D06-T02` Implement the context-window MLP from the lesson
    -   Estimate: 60m
    -   Type: practical
-   [ ] `D06-T03` Split data into training and validation sets
    -   Estimate: 30m
    -   Type: practical
-   [ ] `D06-T04` Experiment with context length or embedding size
    -   Estimate: 30m
    -   Type: practical
### Resources

-   https://youtu.be/TCH_1BHY58I
-   https://github.com/karpathy/makemore
-   https://pytorch.org/tutorials/

### Completion Criteria

Your MLP generates names, and you can explain embeddings, context
windows, and why validation data is useful.

------------------------------------------------------------------------

## Day 07 - Week One Review and First Milestone

**Topics**
-   Review computational graphs, gradients, and language modelling
-   Debugging and independent implementation

### Tasks

-   [ ] `D07-T01` Reimplement one small autograd example without copying
    the lesson
    -   Estimate: 45m
    -   Type: revision
-   [ ] `D07-T02` Run the bigram and MLP models and compare their
    outputs
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D07-T03` Fix the most important implementation gaps
    -   Estimate: 60m
    -   Type: practical
-   [ ] `D07-T04` Write a one-page explanation of what you learned
    -   Estimate: 30m
    -   Type: other
### Resources

-   https://github.com/karpathy/nn-zero-to-hero
-   https://github.com/karpathy/micrograd
-   https://github.com/karpathy/makemore

### Completion Criteria

You have a working autograd experiment and at least one working
character-level language model. You can explain the forward pass, loss,
gradients, and parameter updates.

------------------------------------------------------------------------

## Day 08 - Activations, Gradients, and Training Stability

**Topics**
-   Activation distributions
-   Gradient distributions
-   Initialization
-   Saturation and gradient flow

### Tasks

-   [ ] `D08-T01` Watch Makemore Part 3
    -   Estimate: 60m
    -   Type: learning
    -   Reference: https://youtu.be/P6sfmUTpUmc
    -   Video stop: **00:00 → 40:40** (40m 40s). Focus on initialization, saturated activations, and Kaiming initialization; then reproduce the activation experiments.
-   [ ] `D08-T02` Reproduce activation and gradient visualisations
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D08-T03` Change initialisation or activation settings and
    observe the effect
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D08-T04` Record what changed and why
    -   Estimate: 30m
    -   Type: revision

### Resources

-   https://youtu.be/P6sfmUTpUmc
-   https://github.com/karpathy/makemore

### Completion Criteria

You can inspect activation and gradient statistics and explain why
initialisation and gradient flow matter.

------------------------------------------------------------------------

## Day 09 - Batch Normalisation and Backpropagation Practice

**Topics**
-   Batch normalisation
-   Training stability
-   Manual gradient reasoning
-   Gradient checking

### Tasks

-   [ ] `D09-T01` Finish the relevant Makemore Part 3 sections
    -   Estimate: 45m
    -   Type: learning
    -   Reference: https://youtu.be/P6sfmUTpUmc
    -   Video stop: **40:40 → 1:03:07** (22m 27s) in Makemore Part 3. Stop after the BatchNorm summary, then implement and compare BatchNorm.
-   [ ] `D09-T02` Implement or reproduce BatchNorm in the MLP
    -   Estimate: 60m
    -   Type: practical
-   [ ] `D09-T03` Compare training behaviour with and without BatchNorm
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D09-T04` Review the Backprop Ninja lecture section and trace
    one gradient manually
    -   Estimate: 30m
    -   Type: revision
    -   Reference: https://youtu.be/q8SA3rM6ckI
    -   Video stop: **13:01 → 53:35** (40m 34s) in Backprop Ninja. Focus on manually deriving gradients through the loss and linear layer; trace one gradient yourself.

### Resources

-   https://youtu.be/P6sfmUTpUmc
-   https://youtu.be/q8SA3rM6ckI
-   https://pytorch.org/docs/stable/generated/torch.nn.BatchNorm1d.html

### Completion Criteria

You can explain what BatchNorm does and compare the behaviour of your
MLP with and without it.

------------------------------------------------------------------------

## Day 10 - WaveNet and Larger Contexts

**Topics**
-   Hierarchical representations
-   Larger context windows
-   Dilated/temporal patterns at a conceptual level
-   Receptive field

### Tasks

-   [ ] `D10-T01` Watch Makemore Part 5 (WaveNet)
    -   Estimate: 60m
    -   Type: learning
    -   Reference: https://youtu.be/t3YJ5hKiMQ0
    -   Video stop: **17:11 → 47:44** (30m 33s). Focus on the WaveNet overview, larger context, implementation, and training; then draw its data flow.
-   [ ] `D10-T02` Draw the data flow and receptive field for a small
    example
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D10-T03` Inspect how the model uses a larger context
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D10-T04` Summarise how the architecture differs from the
    earlier MLP
    -   Estimate: 30m
    -   Type: revision

### Resources

-   https://youtu.be/t3YJ5hKiMQ0
-   https://github.com/karpathy/makemore

### Completion Criteria

You can explain why a model may need a larger context and describe the
high-level data flow in the WaveNet lesson.

------------------------------------------------------------------------

## Day 11 - Transformer and Self-Attention Fundamentals

**Topics**
-   Tokens and token embeddings
-   Query, key, and value intuition
-   Self-attention
-   Causal masking
-   Positional information

### Tasks

-   [ ] `D11-T01` Start Let's Build GPT
    -   Estimate: 60m
    -   Type: learning
    -   Reference: https://youtu.be/kCc8FmEb1nY
    -   Video stops: **00:00 → 22:11** (22m 11s), then **42:13 → 1:11:38** (29m 25s) in Let's Build GPT. Skip the bigram-training middle section; focus on data setup and self-attention.
-   [ ] `D11-T02` Work through a tiny self-attention example with a few
    tokens
    -   Estimate: 60m
    -   Type: practical
-   [ ] `D11-T03` Implement or inspect a single-head self-attention
    layer
    -   Estimate: 30m
    -   Type: practical
-   [ ] `D11-T04` Explain why causal masking is needed for next-token
    prediction
    -   Estimate: 30m
    -   Type: revision

### Resources

-   https://youtu.be/kCc8FmEb1nY
-   https://jalammar.github.io/illustrated-transformer/
-   https://pytorch.org/docs/stable/generated/torch.nn.MultiheadAttention.html

### Completion Criteria

You can explain query, key, value, attention scores, and causal masking
at a basic implementation level.

------------------------------------------------------------------------

## Day 12 - GPT Architecture and Training

**Topics**
-   Transformer blocks
-   Multi-head attention
-   Feed-forward layers
-   Residual connections
-   Layer normalisation
-   Next-token prediction

### Tasks

-   [ ] `D12-T01` Continue Let's Build GPT
    -   Estimate: 60m
    -   Type: learning
    -   Reference: https://youtu.be/kCc8FmEb1nY
    -   Video stop: **1:11:38 → 1:56:20** (44m 42s). Focus on attention, multi-head attention, feed-forward layers, residuals, layer normalization, and the completed GPT; then run and inspect it.
-   [ ] `D12-T02` Trace the flow through one transformer block
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D12-T03` Run the small GPT implementation from the lesson
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D12-T04` Change one small configuration and observe the effect
    -   Estimate: 30m
    -   Type: practical
### Resources

-   https://youtu.be/kCc8FmEb1nY
-   https://github.com/karpathy/nn-zero-to-hero

### Completion Criteria

You can describe the major components of a GPT-style transformer and run
the lesson's small model.

------------------------------------------------------------------------

## Day 13 - Tokenisation and BPE

**Topics**
-   Text encoding
-   Token IDs
-   Byte Pair Encoding
-   Vocabulary size
-   Encoding and decoding

### Tasks

-   [ ] `D13-T01` Watch the tokenizer lecture
    -   Estimate: 60m
    -   Type: learning
    -   Reference: https://youtu.be/zduSFxRajkE
    -   Video stop: **00:00 → 57:36** (57m 36s). Focus on Unicode, BPE training, encoding, and decoding; then run the tokenizer examples.
-   [ ] `D13-T02` Run the tokenizer examples and inspect token IDs
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D13-T03` Experiment with encoding and decoding text
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D13-T04` Explain how tokenisation affects model input
    -   Estimate: 30m
    -   Type: revision

### Resources

-   https://youtu.be/zduSFxRajkE
-   https://github.com/karpathy/nn-zero-to-hero
-   https://huggingface.co/learn/llm-course/chapter6/5

### Completion Criteria

You can explain why language models use token IDs and demonstrate a
tokenizer's encode/decode behaviour.

------------------------------------------------------------------------

## Day 14 - Deep Learning Review and Milestone

**Topics**
-   Neural-network fundamentals review
-   Language modelling review
-   Transformer and tokenizer review

### Tasks

-   [ ] `D14-T01` Re-run your autograd, bigram, and MLP implementations
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D14-T02` Run the small GPT experiment and inspect generated
    output
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D14-T03` Explain a transformer block on paper or in your notes
    -   Estimate: 45m
    -   Type: revision
-   [ ] `D14-T04` List the concepts that remain unclear before moving to
    application engineering
    -   Estimate: 45m
    -   Type: revision
### Resources

-   https://karpathy.ai/zero-to-hero.html
-   https://github.com/karpathy/nn-zero-to-hero
-   https://jalammar.github.io/illustrated-transformer/

### Completion Criteria

You have working small-model experiments and can explain the basic path
from text tokens to next-token prediction. Do not delay the
application-engineering phase to perfect every mathematical detail.

------------------------------------------------------------------------

## Day 15 - Agentic AI Concepts and Async Python

**Topics**
-   LLM applications versus agents
-   Agent components and tool use
-   Async/await
-   Basic agent workflow

### Tasks

-   [ ] `D15-T01` Start the freeCodeCamp Agentic AI course and study its
    introduction
    -   Estimate: 60m
    -   Type: learning
    -   Reference: https://youtu.be/Zy7EXDONlTY
    -   Video stop: **08:33 → 41:26** (32m 53s) in the freeCodeCamp course. Focus on the evolution from LLMs to agents; pause and draw the distinction.
-   [ ] `D15-T02` Study the course's async Python section
    -   Estimate: 45m
    -   Type: learning
    -   Reference: https://youtu.be/Zy7EXDONlTY
    -   Video stop: **1:33:18 → 2:06:23** (33m 05s). This is the async Python section; stop at the Pydantic chapter and implement the async exercise.
-   [ ] `D15-T03` Implement a small async Python program
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D15-T04` Draw the components of a simple tool-using agent
    -   Estimate: 30m
    -   Type: practical

### Resources

-   https://youtu.be/Zy7EXDONlTY
-   https://docs.python.org/3/library/asyncio.html

### Completion Criteria

You can explain the difference between a normal LLM call and an agent
that can select and use tools, and can write a basic async function.

------------------------------------------------------------------------

## Day 16 - Pydantic and Structured Data

**Topics**
-   Pydantic models
-   Field types and constraints
-   Validation errors
-   Structured input and output

### Tasks

-   [ ] `D16-T01` Study the Pydantic section in the course
    -   Estimate: 60m
    -   Type: learning
    -   Reference: https://youtu.be/Zy7EXDONlTY
    -   Video stop: **2:06:23 → 3:27:08** (1h 20m 45s). This is the Pydantic section; pause at the single-agent chapter, then build and validate your own schemas.
-   [ ] `D16-T02` Create Pydantic models for an agent request and
    response
    -   Estimate: 60m
    -   Type: practical
-   [ ] `D16-T03` Test valid, missing, and invalid fields
    -   Estimate: 30m
    -   Type: practical
-   [ ] `D16-T04` Record how validation protects application boundaries
    -   Estimate: 30m
    -   Type: revision

### Resources

-   https://docs.pydantic.dev/latest/
-   https://youtu.be/Zy7EXDONlTY

### Completion Criteria

You can define and validate structured Python data and explain why model
output must be validated before your application trusts it.

------------------------------------------------------------------------

## Day 17 - LLM Integration and a Single-Agent Application

**Topics**
-   Model clients
-   System and user messages
-   Prompt structure
-   Tool calling concepts
-   Error handling

### Tasks

-   [ ] `D17-T01` Follow the course's LangChain and single-agent
    sections
    -   Estimate: 60m
    -   Type: learning
    -   Reference: https://youtu.be/Zy7EXDONlTY
    -   Video stop: **3:27:08 → 4:10:00** (42m 52s). Watch the opening of the end-to-end single-agent section, then stop and build your minimal model-backed agent.
-   [ ] `D17-T02` Configure one model provider supported by the lesson;
    prefer Ollama if compatible
    -   Estimate: 30m
    -   Type: practical
-   [ ] `D17-T03` Build a minimal single-agent interaction
    -   Estimate: 60m
    -   Type: practical
-   [ ] `D17-T04` Add basic error handling and test a failed model
    request
    -   Estimate: 30m
    -   Type: practical
### Resources

-   https://docs.langchain.com/oss/python/langchain/overview
-   https://docs.ollama.com/
-   https://youtu.be/Zy7EXDONlTY

### Completion Criteria

Your application can send a request to a model and return a response
through a small Python application. Keep provider credentials out of
source control if using a hosted provider.

------------------------------------------------------------------------

## Day 18 - Tools and Agent Execution

**Topics**
-   Tools and tool schemas
-   Tool selection
-   Tool execution
-   Tool results and errors
-   Limits on tool permissions

### Tasks

-   [ ] `D18-T01` Study the course section on agents and tools
    -   Estimate: 45m
    -   Type: learning
    -   Reference: https://youtu.be/Zy7EXDONlTY
    -   Video stop: **4:10:00 → 4:49:37** (39m 37s), continuing the end-to-end single-agent section. Focus on the remaining agent execution/tool-use example, then implement one harmless tool.
-   [ ] `D18-T02` Implement one harmless tool, such as a calculator or
    local date lookup
    -   Estimate: 60m
    -   Type: practical
-   [ ] `D18-T03` Connect the tool to the agent and inspect the
    tool-call cycle
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D18-T04` Test invalid arguments and tool failures
    -   Estimate: 30m
    -   Type: practical
### Resources

-   https://docs.langchain.com/oss/python/langchain/tools
-   https://docs.ollama.com/capabilities/tool-calling
-   https://youtu.be/Zy7EXDONlTY

### Completion Criteria

Your agent can call one explicitly permitted tool, consume its result,
and handle a tool error without crashing.

------------------------------------------------------------------------

## Day 19 - Multi-Agent Systems

**Topics**
-   Single-agent versus multi-agent designs
-   Agent responsibilities
-   Handoffs and coordination
-   Failure modes and unnecessary complexity

### Tasks

-   [ ] `D19-T01` Study the multi-agent section in the course
    -   Estimate: 60m
    -   Type: learning
    -   Reference: https://youtu.be/Zy7EXDONlTY
    -   Video stop: **4:49:37 → 5:49:37** (60m) in the multi-agent section. Watch the first hour, then design and implement a small two-agent workflow. The chapter continues to 6:30:27.
-   [ ] `D19-T02` Design two agents with distinct responsibilities
    -   Estimate: 30m
    -   Type: practical
-   [ ] `D19-T03` Implement a small two-agent workflow from the lesson
    -   Estimate: 60m
    -   Type: practical
-   [ ] `D19-T04` Compare the two-agent approach with a single-agent
    alternative
    -   Estimate: 30m
    -   Type: learning
### Resources

-   https://youtu.be/Zy7EXDONlTY
-   https://docs.langchain.com/oss/python/langchain/multi-agent

### Completion Criteria

You can explain why the example uses multiple agents and identify at
least one case where a single agent would be simpler.

------------------------------------------------------------------------

## Day 20 - LangGraph Fundamentals

**Topics**
-   Graphs, nodes, and edges
-   Shared state
-   Start and end nodes
-   State transitions

### Tasks

-   [ ] `D20-T01` Study the LangGraph introduction in the course
    -   Estimate: 60m
    -   Type: learning
    -   Reference: https://youtu.be/Zy7EXDONlTY
    -   Video stop: **6:30:27 → 7:30:27** (60m). Focus on why LangGraph is needed and its core concepts; then build a small graph. The core-components chapter continues to 7:44:43.
-   [ ] `D20-T02` Create a small state schema
    -   Estimate: 30m
    -   Type: practical
-   [ ] `D20-T03` Implement a graph with two nodes and a state
    transition
    -   Estimate: 60m
    -   Type: practical
-   [ ] `D20-T04` Trace the state before and after each node
    -   Estimate: 30m
    -   Type: practical
### Resources

-   https://docs.langchain.com/oss/python/langgraph/overview
-   https://docs.langchain.com/oss/python/langgraph/graph-api
-   https://youtu.be/Zy7EXDONlTY

### Completion Criteria

You can create and run a small LangGraph graph and explain how state
moves between nodes.

------------------------------------------------------------------------

## Day 21 - Workflow Patterns and Milestone Review

**Topics**
-   Sequential workflows
-   Parallel execution
-   Conditional edges
-   Iterative workflows

### Tasks

-   [ ] `D21-T01` Study the course's sequential and parallel workflow
    sections
    -   Estimate: 45m
    -   Type: learning
    -   Reference: https://youtu.be/Zy7EXDONlTY
    -   Video stop: **8:29:07 → 9:29:07** (60m). Focus on sequential workflows and the beginning of parallel workflows; then implement the patterns. The parallel chapter continues to 10:15:27.
-   [ ] `D21-T02` Implement a sequential workflow
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D21-T03` Implement a conditional route or simple parallel
    workflow
    -   Estimate: 60m
    -   Type: practical
-   [ ] `D21-T04` Review and test your single-agent and graph
    implementations
    -   Estimate: 30m
    -   Type: revision

### Resources

-   https://docs.langchain.com/oss/python/langgraph/overview
-   https://docs.langchain.com/oss/python/langgraph/graph-api
-   https://youtu.be/Zy7EXDONlTY

### Completion Criteria

You have a working agent and at least one working LangGraph workflow.
You can explain nodes, edges, state, and conditional routing.

------------------------------------------------------------------------

## Day 22 - Build an Agentic Chatbot

**Topics**
-   Chatbot architecture
-   Message history
-   Graph state
-   Conversation turns

### Tasks

-   [ ] `D22-T01` Follow the course's Agentic Chatbot implementation
    -   Estimate: 60m
    -   Type: learning
    -   Reference: https://youtu.be/Zy7EXDONlTY
    -   Video stop: **11:35:51 → 12:35:51** (60m) in the Agentic Chatbot chapter. Stop before the persistence chapter, then build the basic chatbot flow.
-   [ ] `D22-T02` Build the basic chatbot flow
    -   Estimate: 60m
    -   Type: practical
-   [ ] `D22-T03` Test multiple turns and inspect the message state
    -   Estimate: 30m
    -   Type: practical
-   [ ] `D22-T04` Document the request-to-response flow
    -   Estimate: 30m
    -   Type: other
### Resources

-   https://youtu.be/Zy7EXDONlTY
-   https://docs.langchain.com/oss/python/langgraph/overview

### Completion Criteria

You can interact with your chatbot over multiple turns and explain how
the conversation state is represented.

------------------------------------------------------------------------

## Day 23 - Persistence and Conversation Memory

**Topics**
-   Short-term conversation state
-   Checkpointing
-   Thread identifiers
-   Persistence across requests

### Tasks

-   [ ] `D23-T01` Study the course's memory and persistence section
    -   Estimate: 45m
    -   Type: learning
    -   Reference: https://youtu.be/Zy7EXDONlTY
    -   Video stop: **12:43:49 → 13:43:49** (60m) in the persistence section. Stop before the streaming chapter; then add thread IDs and checkpointing.
-   [ ] `D23-T02` Add a thread identifier to the chatbot
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D23-T03` Configure a checkpointer supported by the lesson
    -   Estimate: 60m
    -   Type: practical
-   [ ] `D23-T04` Restart the application and verify persisted
    conversation state
    -   Estimate: 30m
    -   Type: practical
### Resources

-   https://docs.langchain.com/oss/python/langgraph/persistence
-   https://youtu.be/Zy7EXDONlTY

### Completion Criteria

A conversation can continue using its thread identifier, and you can
explain the difference between in-memory state and persisted state.

------------------------------------------------------------------------

## Day 24 - Streaming and Chat Threads

**Topics**
-   Streaming responses
-   Chat sessions and thread IDs
-   Frontend/backend streaming concepts
-   Loading and failure states

### Tasks

-   [ ] `D24-T01` Study the course's streaming and chat-thread section
    -   Estimate: 45m
    -   Type: learning
    -   Reference: https://youtu.be/Zy7EXDONlTY
    -   Video stop: **13:51:00 → 14:42:02** (51m 02s). This covers streaming, chat threading, and the start of database-backed memory; then implement streaming and separate threads.
-   [ ] `D24-T02` Add streaming to the chatbot if supported by the
    chosen model integration
    -   Estimate: 60m
    -   Type: practical
-   [ ] `D24-T03` Support more than one conversation thread
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D24-T04` Test interrupted streams and invalid thread IDs
    -   Estimate: 30m
    -   Type: practical
### Resources

-   https://docs.langchain.com/oss/python/langgraph/streaming
-   https://docs.langchain.com/oss/python/langgraph/persistence
-   https://youtu.be/Zy7EXDONlTY

### Completion Criteria

The chatbot can stream a response and keep separate conversation threads
without mixing their histories.

------------------------------------------------------------------------

## Day 25 - Database Persistence and Observability

**Topics**
-   Database-backed state
-   Persistence configuration
-   Logging
-   Tracing and observability concepts

### Tasks

-   [ ] `D25-T01` Study the database/persistence and monitoring sections
    in the course
    -   Estimate: 45m
    -   Type: learning
    -   Reference: https://youtu.be/Zy7EXDONlTY
    -   Video stop: **14:42:02 → 15:40:24** (58m 22s). Focus on permanent database persistence and LangSmith monitoring; then connect storage and add logs.
-   [ ] `D25-T02` Connect a supported persistent checkpointer or storage
    backend
    -   Estimate: 60m
    -   Type: practical
-   [ ] `D25-T03` Add basic logs for requests, tool calls, and errors
    without logging secrets
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D25-T04` Inspect one failed or slow interaction
    -   Estimate: 30m
    -   Type: practical
### Resources

-   https://docs.langchain.com/oss/python/langgraph/persistence
-   https://docs.langchain.com/langsmith/observability
-   https://youtu.be/Zy7EXDONlTY

### Completion Criteria

Conversation state survives application restarts using the selected
storage approach, and important failures can be investigated through
logs.

------------------------------------------------------------------------

## Day 26 - RAG Fundamentals

**Topics**
-   Why retrieval-augmented generation is useful
-   Document loading
-   Chunking
-   Embeddings
-   Similarity search
-   Grounded answers

### Tasks

-   [ ] `D26-T01` Study the RAG section in the course
    -   Estimate: 45m
    -   Type: learning
    -   Reference: https://youtu.be/Zy7EXDONlTY
    -   Video stop: **16:54:17 → 17:50:27** (56m 10s). This is the RAG section; stop at the human-in-the-loop chapter, then implement document ingestion and retrieval.
-   [ ] `D26-T02` Load a small text or PDF document and split it into
    chunks
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D26-T03` Generate embeddings using a locally available
    embedding model or a free compatible option
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D26-T04` Retrieve relevant chunks for a question and inspect
    the results
    -   Estimate: 45m
    -   Type: practical
### Resources

-   https://docs.langchain.com/oss/python/langchain/rag
-   https://huggingface.co/learn/llm-course/chapter5/6
-   https://docs.ollama.com/capabilities/embeddings
-   https://youtu.be/Zy7EXDONlTY

### Completion Criteria

You can ingest a small document, retrieve relevant chunks for a
question, and explain the roles of chunking, embeddings, and retrieval.

------------------------------------------------------------------------

## Day 27 - Tool Calling and Human-in-the-Loop

**Topics**
-   Tool calling in an agent workflow
-   Human approval
-   Interrupts and resume
-   Safe handling of side effects

### Tasks

-   [ ] `D27-T01` Study the tool-calling and human-in-the-loop sections
    in the course
    -   Estimate: 60m
    -   Type: learning
    -   Reference: https://youtu.be/Zy7EXDONlTY
    -   Video stop: **15:40:24 → 16:40:24** (60m) for tool integration. The chapter ends at 16:54:17; then implement one safe tool.
-   [ ] `D27-T02` Add one read-only tool to the chatbot
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D27-T03` Add a human approval step before a simulated action
    -   Estimate: 45m
    -   Type: practical
    -   Video stop: **17:50:27 → 18:48:09** (57m 42s). Watch the Human-in-the-Loop section, then implement approval, rejection, and resume.
-   [ ] `D27-T04` Test approval, rejection, and interrupted execution
    -   Estimate: 30m
    -   Type: practical
### Resources

-   https://docs.langchain.com/oss/python/langgraph/interrupts
-   https://docs.langchain.com/oss/python/langchain/tools
-   https://youtu.be/Zy7EXDONlTY

### Completion Criteria

The workflow can pause for human approval and resume or reject the
proposed action. Do not give the agent unrestricted shell or filesystem
access.

------------------------------------------------------------------------

## Day 28 - Evaluation, Security, and Deployment Preparation

**Topics**
-   Evaluating answer quality
-   Small evaluation datasets
-   Groundedness and retrieval relevance
-   Secrets management
-   Docker and deployment basics

### Tasks

-   [ ] `D28-T01` Create a small set of questions with expected source
    documents or answer points
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D28-T02` Test retrieval relevance and whether answers are
    supported by retrieved text
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D28-T03` Review input validation, prompt injection risks, and
    secret handling
    -   Estimate: 45m
    -   Type: learning
-   [ ] `D28-T04` Prepare a Dockerfile or deployment configuration for
    the application
    -   Estimate: 45m
    -   Type: practical
    -   Video stop: **18:48:09 → 19:30:00** (41m 51s). Watch the opening of the CI/CD deployment section, then prepare your own deployment configuration. The chapter continues beyond this stop point.

### Resources

-   https://docs.langchain.com/langsmith/evaluation
-   https://owasp.org/www-project-top-10-for-large-language-model-applications/
-   https://docs.docker.com/get-started/
-   https://youtu.be/Zy7EXDONlTY

### Completion Criteria

You have a small repeatable evaluation set, have checked basic security
risks, and can run the application in a container or a documented local
environment.

------------------------------------------------------------------------

## Day 29 - Integrate and Deploy the RAG Chatbot

**Topics**
-   Integrating retrieval with the chatbot
-   End-to-end testing
-   Deployment
-   Configuration and environment variables

### Tasks

-   [ ] `D29-T01` Connect document retrieval to the chatbot workflow
    -   Estimate: 60m
    -   Type: practical
    -   Optional project reference: **20:06:27 → 21:00:00** (53m 33s) from the build-your-own-ChatGPT project. Watch only if you need a reference for integrating the chatbot; spend the rest of the session building your own RAG flow.
-   [ ] `D29-T02` Test questions that are answerable and unanswerable
    from the documents
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D29-T03` Containerize and run the application locally
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D29-T04` Write setup instructions and record deployment
    blockers or costs
    -   Estimate: 30m
    -   Type: other
### Resources

-   https://docs.langchain.com/oss/python/langchain/rag
-   https://docs.docker.com/get-started/
-   https://docs.ollama.com/
-   https://youtu.be/Zy7EXDONlTY

### Completion Criteria

Your chatbot can answer questions using retrieved document chunks,
handle unsupported questions safely, and run in a reproducible
environment. Public deployment is optional if free hosting or model
access is unavailable.

------------------------------------------------------------------------

## Day 30 - Final Review and Next Project Decision

**Topics**
-   Review deep-learning fundamentals
-   Review agent and RAG architecture
-   Independent implementation
-   Project retrospective

### Tasks

-   [ ] `D30-T01` Rebuild one small LangGraph workflow without following
    the tutorial
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D30-T02` Demonstrate the complete document-question-answering
    flow
    -   Estimate: 45m
    -   Type: practical
-   [ ] `D30-T03` Explain the architecture, model calls, retrieval,
    persistence, and failure handling
    -   Estimate: 45m
    -   Type: revision
-   [ ] `D30-T04` Document what you can do independently and what needs
    more practice
    -   Estimate: 30m
    -   Type: other
-   [ ] `D30-T05` Choose the next independent project milestone:
    CodeLens AI, BappyGPT extension, or TripMate AI
    -   Estimate: 15m
    -   Type: other
### Resources

-   https://karpathy.ai/zero-to-hero.html
-   https://github.com/karpathy/nn-zero-to-hero
-   https://youtu.be/Zy7EXDONlTY
-   https://docs.langchain.com/oss/python/langgraph/overview

### Completion Criteria

You can demonstrate a working small RAG-enabled chatbot, explain its
main components, identify its limitations, and choose a realistic next
project milestone.

------------------------------------------------------------------------

**Final 30-Day Completion Checklist**
-   [ ] Implemented a small autograd engine
-   [ ] Built a neural network using the Micrograd concepts
-   [ ] Built a character-level bigram model
-   [ ] Built a character-level MLP
-   [ ] Experimented with activations, gradients, and BatchNorm
-   [ ] Explained the high-level WaveNet architecture
-   [ ] Implemented or inspected a small GPT
-   [ ] Experimented with tokenisation and BPE
-   [ ] Built a basic LLM-powered application
-   [ ] Implemented a tool-using agent
-   [ ] Built a small LangGraph workflow
-   [ ] Implemented conditional routing
-   [ ] Built a multi-turn chatbot
-   [ ] Added conversation persistence
-   [ ] Experimented with streaming
-   [ ] Implemented document chunking and embeddings
-   [ ] Built basic RAG retrieval
-   [ ] Added a human approval step
-   [ ] Created a small evaluation dataset
-   [ ] Tested and documented the application

**Important scope notes**
-   Video ranges are based on the published chapter markers and video durations available when this roadmap was updated. YouTube playback may vary by a few seconds; use the chapter title as the anchor if a marker shifts.
-   Days 7 and 14 are deliberate no-new-video review days. Revisit only the earlier timestamp ranges for topics you cannot yet explain.
-   The freeCodeCamp course may use provider-specific APIs or package
    versions. Follow the lesson to understand the concept, but check
    current official documentation when an API has changed.
-   If a hosted API requires payment or a credit card, do not proceed
    automatically. Try Ollama/local inference or mock the model call
    while learning the surrounding workflow.
-   A local 4 GB VRAM GPU may require smaller models, shorter context,
    CPU offloading, or reduced batch sizes. Keep experiments small.
-   If a day takes longer, move the remaining task forward. Preserve
    understanding and working code rather than forcing the calendar.
