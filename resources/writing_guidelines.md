# Writing Guidelines for Generated Blogs

## Audience

* Primary audience: developers, builders, college students, early-career engineers, and tech-curious readers.
* Assume basic programming knowledge, but do not assume familiarity with advanced concepts.
* Explain unfamiliar technical terms in simple language when they first appear.
* Prefer practical explanations that help readers understand how and why something works.

## Tone and Style

* Write in a clear, direct, practical, and professional style.
* Keep the tone friendly and approachable without using excessive slang.
* Use active voice whenever possible.
* Prefer simple language over unnecessarily complex vocabulary.
* Use analogies when they make a technical concept easier to understand, but avoid forcing metaphors into every explanation.
* Do not use self-references such as:

  * "In this blog post, I will..."
  * "We are going to learn..."
  * "I will explain..."
* Present the information directly.
* Avoid exaggerated claims such as "revolutionary", "game-changing", or "the ultimate guide" unless they are objectively justified.

## Structure and Length

* Target length: 900–1,600 words.
* The introduction should usually contain 2–4 short paragraphs.
* The introduction should:

  * Establish the problem, question, or opportunity.
  * Explain why the topic matters.
  * Give the reader a clear idea of what the article covers.
* Use 3–6 main sections when appropriate.
* Do not force a fixed number of sections if the topic naturally requires fewer or more.
* Each main section should develop one clear idea.
* Use additional subsections only when they improve readability.

## Headings

* Use `#` only for the blog title.
* Use `##` for main sections.
* Use `###` for meaningful subsections when necessary.
* Keep headings concise, preferably six words or fewer.
* Headings should describe the content clearly.
* Use sentence case.

Good:

```text
## How MCP tools work
```

Avoid:

```text
## An In-Depth Overview of Everything You Need to Know About MCP Tools
```

Avoid generic headings such as `## Overview` when a more descriptive heading is possible.

## Paragraphs and Sentences

* Keep paragraphs short and focused.
* Prefer 2–5 sentences per paragraph.
* Avoid walls of text.
* Vary sentence length naturally.
* Break complex explanations into multiple paragraphs.
* Each paragraph should generally communicate one main idea.

## Technical Explanations

When introducing an unfamiliar technical concept:

1. Define it in simple language.
2. Explain why it exists or what problem it solves.
3. Give a concrete example when useful.
4. Explain how it works at a practical level.
5. Mention important limitations or trade-offs when relevant.

For frameworks, methods, or technical principles:

* Give only the historical background necessary for understanding.
* Focus primarily on practical application.
* Prefer concrete developer or product examples over abstract theory.

## Code Examples

Use code only when it helps explain or demonstrate the concept.

* Keep examples focused on one idea.
* Prefer short snippets over large implementations.
* Code snippets should generally be no longer than 15 lines unless a longer example is necessary.
* Always use a language tag.

Examples:

```js
const user = await getUser();
```

```python
result = await client.call_tool("generate_blog", args);
```

* Explain important code when the behavior is not obvious.
* Do not include code merely to make an article appear more technical.
* Do not invent APIs, library behavior, configuration options, or code that has not been established.

## Markdown Conventions

Use Markdown consistently:

* `#` — blog title
* `##` — main sections
* `###` — subsections
* `-` — unordered lists
* `1.` — ordered lists when sequence matters
* `**bold**` — important terms or short takeaways
* `*italic*` — occasional emphasis
* `> ` — useful definitions or memorable statements
* Tables — comparisons or structured information where they improve clarity
* Fenced code blocks — code and configuration examples

Do not overuse formatting. Markdown should improve readability rather than decorate the article.

## Examples and Scenarios

Include concrete examples when they genuinely help explain the topic.

Prefer 2–4 examples when the topic benefits from them.

Examples should:

* Be realistic.
* Relate directly to the main topic.
* Demonstrate a problem, solution, workflow, or practical use case.
* Help the reader understand how the concept applies outside the article.

For technical topics, useful examples may come from:

* Web development
* APIs and databases
* Backend systems
* AI and LLM workflows
* Agentic AI
* MCP
* Developer tooling
* Product development
* Startups
* Open-source projects

Do not add examples simply to satisfy a numerical requirement.

## Practical Guidance

When the topic involves a process or implementation:

* Prefer concrete steps over generic advice.
* Explain why an important step is necessary.
* Mention common mistakes when relevant.
* Include trade-offs when there is more than one reasonable approach.
* Avoid advice such as "just practice more" unless it is accompanied by specific actions.

## Accuracy and Technical Honesty

* Do not invent facts, statistics, APIs, features, benchmarks, or references.
* Clearly distinguish established facts from opinions or recommendations.
* Do not present uncertain information as fact.
* When discussing a library, framework, or tool, avoid claiming functionality that has not been verified or provided as context.
* Prefer accurate, useful explanations over impressive-sounding claims.

## Things to Avoid

* Long historical explanations unless directly relevant.
* Excessive theory without practical application.
* Clickbait titles.
* Excessive repetition.
* Unnecessary jargon.
* Large blocks of unexplained code.
* Generic filler.
* Repetitive conclusions.
* Excessive use of "you should".
* Self-promotion unless explicitly requested.
* References to "my blog", "this blog post", or the author's personal experience unless explicitly requested.

## Getting Started Section

When the topic has a practical application, include a section titled:

```text
## How to Get Started
```

This section should provide concrete next steps.

Use a checklist or numbered list when appropriate.

The steps should be specific enough that a reader can actually begin applying the concept.

If the topic is primarily theoretical, do not force an artificial implementation checklist.

## Further Reading

When useful, include:

```text
## Further Reading
```

Provide 2–4 relevant resources.

Each resource should contain:

* Name
* Link
* One short description explaining why it is useful

Do not invent links or references.

If reliable external resources are not available from the provided context, omit this section rather than creating fictional references.

## Closing Note

The template contains a `{{closing_note}}` placeholder.

Use it for a short, natural ending when appropriate.

It may:

* Reinforce the main takeaway.
* Encourage the reader to experiment.
* Suggest applying the concept to a real project.
* Provide a brief call to action.

Do not force a social-media sharing message into every article.

## Consistency With Example Blogs

When example blogs are available in `examples/`, use them as style references.

Match their:

* General level of technical depth.
* Balance between paragraphs and lists.
* Use of examples.
* Heading style.
* Practicality.
* Code-example style.

Examples should guide the **style and quality**, not be copied.

The generated article must contain original wording and structure appropriate to the requested topic.
