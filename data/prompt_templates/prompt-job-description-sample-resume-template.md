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
{jobMetadata}
```

### Top 10 Job Qualities (in ranked order)
```yaml
{jobQualities}
```

### Resume Template
```
{resumeTemplate}
```

Using the job metadata and top qualities above, create a sample resume for an ideal candidate who would be perfect for this position. The resume should realistically demonstrate how the candidate has developed and applied each of the top 10 qualities throughout their career. 

For this {jobPositionTitle} role at {companyName}, craft a resume that includes:
1. A compelling summary highlighting expertise in recommendation systems and relevant experience
2. 2-3 previous roles with responsibilities and achievements that clearly demonstrate the top qualities
3. Specific, quantifiable achievements aligned with each of the top qualities
4. A skills section organized by relevant technical and soft skill categories
5. An education section with appropriate degrees for this career path

Format the final resume following the template structure, replacing all placeholder text with content tailored to this specific role.