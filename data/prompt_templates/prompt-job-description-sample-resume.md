# Ideal Candidate Resume Generation Prompt

## Goal
Generate a sample resume that an ideal candidate would submit for the specified job position. This resume should:
1. Demonstrate all top qualities identified from the job description
2. Follow proper resume formatting with clear sections
3. Include realistic and compelling examples of how each top quality would be demonstrated in work experience
4. Serve as a reference template for users tailoring their own resumes

## Return Format
Return the resume as properly formatted markdown text following the provided resume template structure. Ensure all sections are properly populated with realistic information for an ideal candidate, including:
- Professional header with contact info
- Summary that highlights core expertise aligned with job requirements
- Work experience with achievement-focused bullet points demonstrating top qualities
- Achievements section highlighting major accomplishments relevant to the role
- Skills section organized by relevant categories
- Education section with appropriate degrees and distinctions

## Warnings
- Do NOT include generic or vague bullet points. Each bullet should demonstrate specific achievements with metrics where appropriate.
- Do NOT fabricate technologies or companies that don't exist in the real world.
- Do NOT include more than 5-7 bullet points per job role.
- Ensure 60-80% of bullet points include quantifiable outcomes.
- Use strong action verbs in past tense for all experience bullet points.
- The ideal candidate should have exactly the qualifications needed - neither overqualified nor underqualified.
- Maintain realistic career progression aligned with the seniority of the target position.

## Instructions
Using the job metadata and top qualities in the **Context Dump** below, create a sample resume for an ideal candidate who would be perfect for this position. The resume should realistically demonstrate how the candidate has developed and applied each of the top 10 qualities throughout their career. 

For this {jobPositionTitle} role at {companyName}, craft a resume that includes:
1. A compelling summary highlighting the ranked #1 quality and relevant experience
2. 3-4 previous roles with responsibilities and achievements that clearly demonstrate the top qualities
3. Specific, quantifiable achievements from work experience aligned with the top qualities
4. A skills section organized by relevant technical and soft skill categories
5. An education section with appropriate degrees for this career path

Format the final resume following the template structure, replacing all placeholder text with content tailored to this specific role.

## Context Dump

### Job Metadata
```yaml
Company About: |-
  Academia.edu is a for-profit company focused on democratizing and accelerating research worldwide to enhance scientific discovery and technological progress for the benefit of humanity.
Company Name: Academia.edu
Job Position Title: Senior Product Manager
Position Summary: |-
  Lead the Paper Recommendations team to optimize algorithms, collaborate cross-functionally, and improve user experience in the academic research platform.
```

### Top 10 Job Qualities (in ranked order)
```yaml
- quality: Expertise in Recommendation Systems
  rank: 1
  reason: |-
    This is ranked highest as the role focuses extensively on enhancing recommendation algorithms, requiring expertise in these systems and related technologies.
  sentences:
  - |-
    You will lead a newly formed team focused on optimizing our recommendation algorithms
  - |-
    As a subject matter expert in ranking systems, you will bring best practices and techniques to the team
  - |-
    Define and navigate the explore-exploit trade-off in recommendation systems and how to balance user exploration with personalized content exploitation
  - Educate the product organization on ranking/recommendations best practices
  - |-
    Strong understanding of recommendation systems, machine learning, and data science principles
- quality: Cross-Functional Leadership & Collaboration
  rank: 2
  reason: |-
    Ranked second as the position requires leading diverse teams to achieve shared objectives, crucial for optimizing the recommendation system.
  sentences:
  - |-
    Collaborate with cross-functional teams, including data science, engineering, and UX
  - Lead and coordinate cross-functional teams across engineering and data
- quality: Product Strategy & Roadmap Development
  rank: 3
  reason: |-
    Essential because setting the strategic direction for the product team is critical to guiding development efforts.
  sentences:
  - Build out the first product roadmap for this newly formed team
  - Manage product lifecycle from ideation to launch and post-launch optimization
- quality: Analytical & Problem-Solving Skills
  rank: 4
  reason: |-
    High-level analytical skills are vital for interpreting data and iterating on product features, fundamental to enhancing the recommendation algorithm.
  sentences:
  - Excellent analytical and problem-solving skills
  - Customer-centric approach with a knack for data-driven validation
- quality: Communication Skills
  rank: 5
  reason: |-
    Crucial for effectively conveying complex ideas to various stakeholders and ensuring successful cross-team collaboration.
  sentences:
  - Exceptional communication skills, both written and oral
  - Educate the product organization on ranking/recommendations best practices
- quality: Experience in EdTech or Media-Tech
  rank: 6
  reason: |-
    While specific industry experience is important, it follows fundamental skills and expertise in the ranking systems.
  sentences:
  - 5+ years of experience in product management, preferably in edtech or media-tech
- quality: Self-Motivated & Proactive Approach
  rank: 7
  reason: |-
    Valued as it enables the candidate to drive initiatives independently, ensuring continuous progress without needing direct oversight.
  sentences:
  - Self-starter with a proactive approach to identifying and solving problems
- quality: Impact-Driven Mindset
  rank: 8
  reason: |-
    Important for aligning product improvements with broader company goals, though less critical than technical and leadership capabilities.
  sentences:
  - |-
    Drive business impact (i.e. more engagement with research through better recommendations)
  - Demonstrated ability to make a significant business impact
- quality: Startup Experience
  rank: 9
  reason: |-
    Adds value given the dynamic environment of academia.edu, contributing to agility in addressing challenges, though secondary to primary skills.
  sentences:
  - Previous startup experience is essential
- quality: Background with Large Language Models
  rank: 10
  reason: |-
    Placed last as it's a 'nice to have,' suggesting beneficial but not necessary; primary focus is on recommendation systems and leadership.
  sentences:
  - Background in working with Large Language Models (LLMs)
```

### Resume Template
```
[Full Name]
[Professional Title] | [Professional Attribute 1] | [Professional Attribute 2] 

[Email Address]
[Phone Number]
[LinkedIn Profile URL]
[City], [State]

Summary
======
[Brief professional overview highlighting your core expertise, key achievements, and career trajectory. Emphasize your most significant accomplishments and the unique value you bring to potential employers.]


Experience
======
[Job Title 1]
[Company Name 1]
[Start Date 1] - [End Date 1]
[City], [State]
[Company Description/Industry]
 - [Achievement Description 1]
 - [Achievement Description 2]
 - [Achievement Description 3]
 - [Achievement Description 4]
 - [Achievement Description 5]

[Job Title 2]
[Company Name 2]
[Start Date 2] - [End Date 2]
[City], [State]
[Company Description/Industry]
 - [Achievement Description 1]
 - [Achievement Description 2]
 - [Achievement Description 3]
 - [Achievement Description 4]
 - [Achievement Description 5]


Achievements
======
[Achievement Title 1 - Best Outcome from Work Experience]
[Achievement Description 1 - Best Outcome from Work Experience]

[Achievement Title 2 - Best Outcome from Work Experience]
[Achievement Description 2 - Best Outcome from Work Experience]

[Achievement Title 3 - Best Outcome from Work Experience]
[Achievement Description 3 - Best Outcome from Work Experience]


Skills
======
 - [Skill Category 1]
   - [Skill 1]
   - [Skill 2]
   - [Skill 3]

 - [Skill Category 2]
   - [Skill 1]
   - [Skill 2]
   - [Skill 3]

 - [Skill Category 3]
   - [Skill 1]
   - [Skill 2]
   - [Skill 3]


Education
======
[Degree 1] in [Major 1]
[University Name 1]
 - [Note 1]
 - [Note 2]
 - [Note 3]

[Degree 2] in [Major 2]
[University Name 2]
 - [Note 1]
 - [Note 2]
 - [Note 3]
```

