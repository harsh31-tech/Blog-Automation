# TRIZ: A 40-Principle Toolkit for Smarter Problem Solving

When you’re stuck on a difficult technical or product problem, "just brainstorm more" often leads to the same ideas being considered again and again.

**TRIZ** (pronounced "trees"), short for *Theory of Inventive Problem Solving*, offers a structured way to approach these situations. It focuses on identifying contradictions and using recurring inventive principles to find alternative solutions.

This post explains:

* What TRIZ is and why it matters
* The 40 inventive principles in plain language
* How developers and builders can adapt the principles
* A practical workflow for applying TRIZ to real problems

---

## What Is TRIZ?

**TRIZ** stands for *Theory of Inventive Problem Solving* (Russian: *Teoriya Resheniya Izobretatelskikh Zadatch*). It was developed by **Genrich Altshuller**, a Soviet engineer and inventor, who studied large collections of patents and looked for recurring patterns in inventive solutions.

His work led to a systematic approach for solving problems rather than relying entirely on trial and error.

Some important parts of the TRIZ methodology include:

* **40 Inventive Principles** — recurring patterns for generating possible solutions
* **Contradictions** — situations where improving one property appears to make another worse
* **Contradiction matrices** — tools that can suggest potentially useful principles for certain engineering contradictions

TRIZ was originally developed for engineering and industrial problems. Its underlying way of thinking can also be adapted to software, product development, and system design.

---

## The Core Idea: Solve Contradictions

Many difficult problems can be expressed as a contradiction.

For example:

* "I want the API to be **faster**, but I don't want the architecture to become **more complex**."
* "I want the product to be **more customizable**, but I don't want the codebase to become **harder to maintain**."
* "I want an AI system to be **more capable**, but I don't want inference to become **slower or more expensive**."

A common approach is to compromise:

> Make the API somewhat faster, accept some additional complexity, and move on.

TRIZ encourages a different question:

> "Is there a way to improve one property without accepting the usual downside?"

The 40 inventive principles provide patterns that can help generate those alternatives.

They are not guaranteed solutions. Instead, they act as **prompts for thinking differently about the problem**.

---

## The 40 TRIZ Principles

You don't need to memorize all 40. Think of them as a playbook of possible moves.

### 1–10: Restructure the System

1. **Segmentation** — Split something into independent parts.
   *Software example:* Separating a large application into well-defined modules.

2. **Taking Out (Extraction)** — Remove or isolate a troublesome part.
   *Software example:* Moving an expensive background task out of the request path.

3. **Local Quality** — Give different parts different properties suited to their roles.
   *Software example:* Using specialized components for different workloads instead of forcing every component to behave identically.

4. **Asymmetry** — Replace a symmetric design with an asymmetric one when it provides an advantage.
   *Example:* Designing an interface around the way users actually interact with it rather than making every element uniform.

5. **Merging** — Combine related functions or operations.
   *Software example:* Combining related processing steps when doing so reduces unnecessary overhead.

6. **Universality** — Make one component perform multiple useful functions.
   *Example:* A smartphone combining communication, navigation, camera, and payment capabilities.

7. **Nesting** — Place one object or component inside another.
   *Example:* A collapsible antenna or a nested configuration structure.

8. **Counterweight** — Balance a force or undesirable effect with another force.
   *Example:* Elevator counterweights balancing the elevator car.

9. **Preliminary Anti-Action** — Apply a counter-effect in advance.
   *Example:* Designing a structure with an initial stress that helps compensate for an expected load.

10. **Preliminary Action** — Perform a required action beforehand.
    *Software example:* Precomputing data that would otherwise have to be calculated repeatedly at runtime.

### 11–20: Change How the System Acts

11. **Beforehand Cushioning** — Prepare protection against possible problems in advance.
    *Example:* Backups, circuit breakers, or graceful fallback mechanisms.

12. **Equipotentiality** — Arrange the system so unnecessary movement or effort is reduced.
    *Example:* Designing a workflow so components operate at compatible stages instead of repeatedly converting between states.

13. **Inversion** — Try doing the opposite of the conventional approach.
    *Example:* Instead of pushing data continuously to every consumer, let consumers request or pull data when needed.

14. **Spheroidality (Curvature)** — Replace straight or rigid arrangements with curved or rotating ones when useful.
    *Example:* Ball bearings reducing friction between moving surfaces.

15. **Dynamics** — Make a system adjustable or adaptable.
    *Software example:* Feature flags or configuration-driven behavior.

16. **Partial or Excessive Action** — Deliberately do slightly more or less than the ideal amount when that simplifies the overall process.
    *Example:* Applying slightly more material and trimming it afterward.

17. **Another Dimension** — Use another spatial dimension or change orientation.
    *Software example:* Reorganizing a flat workflow into parallel processing stages.

18. **Mechanical Vibration** — Use oscillation or vibration to achieve a useful effect.
    *Example:* Ultrasonic cleaning or haptic feedback.

19. **Periodic Action** — Replace continuous action with periodic or pulsed action.
    *Software example:* Batch processing instead of continuously processing every individual event.

20. **Continuity of Useful Action** — Reduce idle time and keep useful work moving.
    *Software example:* Designing CI/CD pipelines so independent stages can execute efficiently instead of waiting unnecessarily.

### 21–30: Turn Problems Into Advantages

21. **Skipping** — Perform a potentially harmful operation quickly enough to avoid its undesirable effects.
    *Example:* Performing a manufacturing operation rapidly before heat can spread significantly.

22. **Blessing in Disguise** — Turn a harmful effect into something useful.
    *Software example:* Using production errors to identify missing test cases or monitoring rules.

23. **Feedback** — Use feedback to control and improve system behavior.
    *Software example:* Using latency and error metrics to trigger scaling or fallback behavior.

24. **Intermediary** — Introduce an intermediate component between two elements.
    *Software example:* A message queue, cache, proxy, or API gateway.

25. **Self-Service** — Make a system perform useful maintenance or support work itself.
    *Software example:* Automated recovery mechanisms that restart failed services.

26. **Copying** — Use a simpler or cheaper representation instead of the original.
    *Software example:* Using mocks or simulations during development instead of repeatedly depending on expensive external systems.

27. **Cheap Short-Lived Objects** — Replace expensive durable objects with inexpensive temporary ones when appropriate.
    *Software example:* Ephemeral environments or short-lived compute instances.

28. **Mechanics Substitution** — Replace a mechanical approach with another physical or information-based approach.
    *Software example:* Replacing a manual operational process with software automation.

29. **Pneumatics and Hydraulics** — Use liquids or gases to achieve an effect instead of solid mechanical components.
    *Example:* Hydraulic braking systems.

30. **Flexible Shells or Thin Films** — Replace rigid structures with flexible or thin structures.
    *Software analogy:* Designing loosely coupled plugin boundaries instead of tightly coupling every feature to the core system.

### 31–40: Change Materials or Conditions

31. **Porous Materials** — Introduce pores or porous structures where they provide a useful effect.
    *Example:* Foam insulation or breathable materials.

32. **Color Changes** — Use color, transparency, or visual changes to communicate information.
    *Software example:* Using UI state colors to communicate success, warnings, or errors.

33. **Homogeneity** — Make interacting components more similar when compatibility or interaction improves as a result.
    *Example:* Using compatible materials to reduce corrosion between connected components.

34. **Discarding and Recovering** — Remove something after use or restore it when necessary.
    *Software example:* Recreating disposable environments instead of maintaining them indefinitely.

35. **Parameter Changes** — Change properties such as temperature, concentration, flexibility, speed, or other parameters.
    *Software example:* Adjusting batch size, timeout values, concurrency limits, or model parameters.

36. **Phase Transitions** — Use effects associated with a change of state.
    *Example:* Ice absorbing heat as it melts.

37. **Thermal Expansion** — Use expansion or contraction caused by temperature changes.
    *Example:* Bimetallic strips used in thermostats.

38. **Strong Oxidants** — Use stronger oxidizing agents or related chemical effects.
    *Example:* Oxygen-enriched combustion in industrial processes.

39. **Inert Atmosphere** — Reduce unwanted reactions by changing the surrounding environment.
    *Software analogy:* Running untrusted code inside a sandboxed environment.

40. **Composite Materials** — Combine different materials or properties to create a better overall result.
    *Software analogy:* Combining technologies with different strengths, such as SQL for transactional data and a specialized system for another workload.

---

## How to Use TRIZ as a Developer

You don't need to apply the complete formal TRIZ methodology to start using the principles.

A simple workflow is enough.

### Step 1: Write Down the Contradiction

Start with a specific problem.

For example:

> "We want the API to be faster, but we don't want the architecture to become more complex."

Or:

> "We want the AI agent to handle more tasks, but we don't want latency and cost to increase significantly."

A useful format is:

**"We want to improve X without making Y worse."**

### Step 2: Choose Candidate Principles

Select 3–5 principles that could provide a different way of looking at the problem.

For software problems, principles such as these can often generate useful questions:

* **Segmentation** — Can the problem be split into smaller parts?
* **Feedback** — Can system behavior respond to real-time measurements?
* **Intermediary** — Would a queue, cache, proxy, or buffer help?
* **Dynamics** — Can the behavior become configurable?
* **Preliminary Action** — Can expensive work happen earlier?
* **Copying** — Can a simulation or simpler representation replace the expensive original?

The goal isn't to prove that a principle is correct. The goal is to generate possible approaches.

### Step 3: Turn Principles Into Questions

For each selected principle, ask:

> "If I had to apply this principle to my system, what would I change?"

For example:

**Segmentation**

> Could this feature be separated into independent modules or services?

**Intermediary**

> Could a queue or cache separate the fast request path from the expensive operation?

**Dynamics**

> Could this behavior be controlled through configuration instead of hardcoded logic?

**Feedback**

> Which metric could automatically trigger scaling, fallback, or another response?

Generate several possibilities before deciding which one to build.

### Step 4: Prototype and Measure

Choose one or two promising ideas.

Then:

1. Build a small prototype.
2. Measure the relevant metrics.
3. Compare the result with the original approach.
4. Keep, modify, or discard the idea.

Useful metrics might include:

* Latency
* Cost
* Reliability
* Complexity
* Throughput
* Developer experience
* Resource usage

TRIZ is most useful when the generated ideas are eventually tested against the real problem.

---

## Examples

### Example 1: Faster API Without Excessive Complexity

**Contradiction:** Faster responses without significantly increasing architectural complexity.

Potential principles:

* **Preliminary Action** — Precompute expensive aggregations.
* **Segmentation** — Move expensive work into a separate worker.
* **Intermediary** — Introduce caching or a queue where appropriate.
* **Feedback** — Monitor latency and automatically adjust resources.

The important part isn't choosing the "correct" principle. It is using each principle to generate a different design possibility and then testing those possibilities.

### Example 2: More Customization Without a Messier Codebase

**Contradiction:** More flexibility for users without turning the core system into a collection of special cases.

Potential approaches:

* **Segmentation** — Separate core functionality from customization modules.
* **Dynamics** — Drive behavior through configuration.
* **Universality** — Build reusable components with configurable behavior.
* **Copying** — Provide isolated environments for testing customizations.

The resulting architecture can then be evaluated for maintainability, complexity, and development speed.

### Example 3: More Capable AI Systems Without Uncontrolled Cost

**Contradiction:** More capable behavior without proportionally increasing latency and cost.

Potential approaches:

* **Segmentation** — Route simple tasks to deterministic logic and complex tasks to an LLM.
* **Preliminary Action** — Precompute or cache information that is repeatedly needed.
* **Feedback** — Monitor token usage, latency, and error rates.
* **Dynamics** — Select different models or workflows depending on the task.

These approaches do not guarantee a better system. They provide hypotheses that can be tested with real workloads.

---

## How to Get Started

Try TRIZ on one problem you are currently working on:

1. Write the problem as a contradiction.
2. Identify what you want to improve and what you don't want to make worse.
3. Choose 3–5 potentially relevant principles.
4. Turn each principle into a question about your system.
5. Generate several possible solutions.
6. Prototype the most promising ideas.
7. Measure the results and compare them with the original approach.

The goal isn't to memorize all 40 principles. It is to build the habit of looking at a difficult problem from several different angles.

---

## Further Reading

* [TRIZ40 — Interactive list of the 40 principles](https://www.triz40.com/aff_Principles_TRIZ.php) — A reference for exploring the individual principles.
* [TRIZ 40](https://triz-40.peteraim.com/) — A practical reference containing examples and explanations.
* [Eureka TRIZ Guide](https://eureka.patsnap.com/blog/what-is-triz-methodology-guide/) — An overview of TRIZ and its methodology.

---

*The most useful part of TRIZ is not memorizing the principles. It is learning to question the assumptions behind a problem and generate alternatives systematically.*
