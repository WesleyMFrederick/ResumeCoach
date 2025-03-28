## **Context & Role** 
Act as an experienced HR professional specializing in technology product management. Your task is to analyze a given <Job Description> and extract two different types of information: 1) basic job metadata and 2) the top 10 most relevant attributes needed for the ideal candidate. Use the XML tags below for <Job Description>, <Instructions>, <Example Job Description>, and <Expected YAML Output>.

<Job Description>
<<JOB_DESCRIPTION>>
</Job Description>

<Instructions>
PART 1: METADATA EXTRACTION
Extract the following basic information from the job description:
1. Company Name: The name of the company offering the position
2. Company About: A concise 30-word summary of the company's mission and focus
3. Job Position Title: The exact title of the role being advertised
4. Position Summary: A concise 30-word summary of what the role entails

PART 2: TOP QUALITIES EXTRACTION
1. Read the <Job Description> carefully.
2. Extract the top 10 most important qualities the perfect candidate should possess.
   a. Phrases in the job description wrapped in double asterisks indicate bolded text.
   b. Qualities extracted from bolded text should be ranked the highest.
3. For each quality, include the following:
   a. A title that describes the quality in industry-standard terms.
   b. Supporting sentences directly quoted from the job description that justify why this quality is needed.
      i. Extract the exact text, including the double asterisks that indicate bolded text.
      ii. Include more than one sentence when relevant.
        ii. <Example>The quality:"Expertise in Recommendation Systems" could have the following sentences: "You will lead a newly formed team focused on optimizing our recommendation algorithms", "As a subject matter expert in ranking systems, you will bring best practices and techniques to the team", "Define and navigate the explore-exploit trade-off in recommendation systems and how to balance user exploration with personalized content exploitation", "Educate the product organization on ranking/recommendations best practices", "Strong understanding of recommendation systems, machine learning, and data science principles"
   c. A reason field that explains why this quality is ranked at its specific position, strictly derived from the job description.
4. Rank the qualities in order of importance based on how essential they are to the role.
5. If two similar qualities are identified (e.g., data management and data analysis), merge them into a single ranked attribute.
   a. <Example>If "Data Analysis" and "Data Management" appear separately but share significant overlap, combine them into one attribute such as "Data Management & Analysis" and rank accordingly.</Example>
6. Format your response as a structured YAML document with both sections. Please ensure your response is in valid YAML format that can be parsed correctly:

```yaml
# Job Metadata
metadata:
  Company Name: "Extracted name"
  Company About: "Concise 30-word summary"
  Job Position Title: "Extracted title" 
  Position Summary: "Concise 30-word summary"

# Top 10 Qualities
qualities:
  - rank: 1
    quality: "Quality 1"
    sentences:
      - "Supporting sentence 1"
      - "Supporting sentence 2"
    reason: "Explanation for ranking"
  # ... more qualities
```
7. Example Input & Expected Output
  a. See <Example Job Description> for an example input structure
  b. See <Expected YAML Output> for an example of the expected content and structure given the <Example Job Description>

<Example Job Description>
About the Company:
Via is using technology to transform transportation around the world. From changing a single person’s daily commute to reducing humanity’s collective environmental footprint — we’ve got huge goals.

We’re Via, and we build technology that changes the way the world moves. We pioneered the TransitTech category to ensure that the future of transportation is shared, dynamic public mobility — the kind that reduces carbon emissions across congested cities, minimizes reliance on private cars, and provides everyone with accessible, efficient, and affordable ways of getting around.

We created the first end-to-end TransitTech solution for cities and transit agencies, offering world-class software, service design, and operational expertise to fundamentally improve the way the world moves.

Via was founded with the guiding principle that we go further when we go together. We are dedicated to building a diverse, inclusive and authentic workplace. If you’re excited about this role but your past experience doesn’t align perfectly with every qualification in the job description, we encourage you to apply anyways. You may be just the right candidate for this or other roles. All backgrounds, identities, and voices are welcomed and celebrated at Via.


About the job:
We’re looking for a Senior Product Manager,  to lead the development and launch of a new product that helps transit agencies deliver reliable and efficient service to their communities. This role offers the unique opportunity to create from the ground up while leveraging the strengths of an established platform to maximize impact. You will drive this new product from inception through execution, collaborating closely with product managers, product designers, engineers, and other cross-functional team members to shape this new product.

What You'll Do:
Understand transit and transportation planners’ needs through frequent customer interviews and tracked customer requests.
Synthesize these needs into a product strategy & prioritization framework with clear measurable goals and get buy-in from cross-functional stakeholders.
Work closely with the engineering and design teams to scope, design, build, and iterate features that advance this strategy
Work with marketing and success teams to communicate and roll out this new product to customers
Measure the results, learn, and iterate
Stay current with industry trends to drive innovation and prepare the team for emerging challenges.

Who You Are:
An experienced product manager, with a minimum of 5-7 years of experience in startups or large companies operating on a global scale
A “simplifier” who breaks down complex logical and technical concepts and readily finds product-oriented solutions to divergent customer requests
You can quickly and independently learn about new, highly technical and specialized domains
A team player, with great communication/listening skills and a can-do attitude
You have a natural empathy for users and instincts for what makes a great software product
Demonstrated success in handling an end-to-end product lifecycle with the ability to drive product planning, development, and launch
You are entrepreneurial, comfortable with ambiguity and have a bias for action
You take a deeply collaborative approach to your work
You have passion and energy that inspires others
</Example Job Description>

<Expected YAML Output>
# Job Metadata
metadata:
  Company Name: Via
  Company About: Via builds TransitTech solutions to improve shared, dynamic public mobility, reducing carbon emissions and reliance on private cars while making transportation accessible and efficient.
  Job Position Title: Senior Product Manager
  Position Summary: Lead development of a new product for transit agencies, shaping strategy, collaborating cross-functionally, and driving execution to improve service reliability and efficiency.

# Top 10 Qualities
qualities:
  - rank: 1
    quality: Customer-Centric & Problem-Solving Mindset
    sentences:
      - Understand transit and transportation planners' needs through frequent customer interviews and tracked customer requests.
      - Synthesize these needs into a product strategy & prioritization framework with clear measurable goals and get buy-in from cross-functional stakeholders.
      - You have a natural empathy for users and instincts for what makes a great software product.
    reason: This is ranked highest because the job emphasizes deep customer understanding, identifying meaningful problems, and delivering impactful solutions for transit agencies.

  - rank: 2
    quality: Strategic Thinking & Prioritization
    sentences:
      - Synthesize these needs into a product strategy & prioritization framework with clear measurable goals and get buy-in from cross-functional stakeholders.
      - Measure the results, learn, and iterate.
      - Stay current with industry trends to drive innovation and prepare the team for emerging challenges.
    reason: Ranked highly because the job requires defining a clear, measurable strategy and adapting to industry trends to ensure the product remains competitive.

  - rank: 3
    quality: Cross-Functional Collaboration & Leadership
    sentences:
      - You will drive this new product from inception through execution, collaborating closely with product managers, product designers, engineers, and other cross-functional team members to shape this new product.
      - Work closely with the engineering and design teams to scope, design, build, and iterate features that advance this strategy.
      - You take a deeply collaborative approach to your work.
    reason: Ranked high due to the emphasis on leading and collaborating with multiple teams, which is essential for product execution and success.

  - rank: 4
    quality: End-to-End Product Management Expertise
    sentences:
      - Demonstrated success in handling an end-to-end product lifecycle with the ability to drive product planning, development, and launch.
      - An experienced product manager, with a minimum of 5-7 years of experience in startups or large companies operating on a global scale.
    reason: Placed here because the role requires managing a product from concept to launch, which is fundamental to the position but follows strategy and collaboration in importance.

  - rank: 5
    quality: Technical Aptitude & Ability to Learn Quickly
    sentences:
      - You can quickly and independently learn about new, highly technical and specialized domains.
      - A 'simplifier' who breaks down complex logical and technical concepts and readily finds product-oriented solutions to divergent customer requests.
    reason: Ranked fifth because while technical aptitude is necessary for success, the job emphasizes the ability to learn quickly rather than requiring deep technical expertise.

  - rank: 6
    quality: Communication & Stakeholder Management
    sentences:
      - A team player, with great communication/listening skills and can-do attitude.
      - Synthesize these needs into a product strategy & prioritization framework with clear measurable goals and get buy-in from cross-functional stakeholders.
      - Work with marketing and success teams to communicate and roll out this new product to customers.
    reason: Ranked here because strong communication is key for stakeholder alignment and product rollout, but strategy and execution take precedence.

  - rank: 7
    quality: Entrepreneurial Mindset & Bias for Action
    sentences:
      - You are entrepreneurial, comfortable with ambiguity and have a bias for action.
      - This role offers the unique opportunity to create from the ground up while leveraging the strengths of an established platform to maximize impact.
    reason: Lower-ranked but still important because the job values proactive decision-making and initiative in an evolving product environment.

  - rank: 8
    quality: Data-Driven Decision Making
    sentences:
      - Measure the results, learn, and iterate.
      - Stay current with industry trends to drive innovation and prepare the team for emerging challenges.
    reason: Placed here because while leveraging data is crucial, the role prioritizes direct problem-solving and strategy development over data analysis.

  - rank: 9
    quality: Passion & Energy
    sentences:
      - You have passion and energy that inspires others.
      - We created the first end-to-end TransitTech solution for cities and transit agencies, offering world-class software, service design, and operational expertise to fundamentally improve the way the world moves.
    reason: While passion is valued, it is secondary to the more technical and strategic requirements of the role.

  - rank: 10
    quality: Industry Knowledge in Transit & Transportation
    sentences:
      - We're looking for a Senior Product Manager, to lead the development and launch of a new product that helps transit agencies deliver reliable and efficient service to their communities.
      - Understand transit and transportation planners' needs through frequent customer interviews and tracked customer requests.
      - Stay current with industry trends to drive innovation and prepare the team for emerging challenges.
    reason: Ranked last because while industry knowledge is beneficial, the role prioritizes problem-solving, strategy, and execution over direct transit expertise.
</Expected YAML Output>

</Instructions>