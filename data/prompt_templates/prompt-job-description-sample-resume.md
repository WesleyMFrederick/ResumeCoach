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
{jobQualities}
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
[Achievement Title 1]
[Achievement Description 1]

[Achievement Title 2]
[Achievement Description 2]

[Achievement Title 3]
[Achievement Description 3]


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

Using the job metadata and top qualities above, create a sample resume for an ideal candidate who would be perfect for this position. The resume should realistically demonstrate how the candidate has developed and applied each of the top 10 qualities throughout their career. 

For this {jobPositionTitle} role at {companyName}, craft a resume that includes:
1. A compelling summary highlighting expertise in recommendation systems and relevant experience
2. 3-4 previous roles with responsibilities and achievements that clearly demonstrate the top qualities
3. Specific, quantifiable achievements aligned with each of the top qualities
4. A skills section organized by relevant technical and soft skill categories
5. An education section with appropriate degrees for this career path

Format the final resume following the template structure, replacing all placeholder text with content tailored to this specific role.