# **C.R.A.F.T. Prompt: Extracting Job Description Fields in YAML**

## **Context**  
The goal of this prompt is to extract structured job details from a job description and format them in **YAML**. The extracted data must include the **Company Name, Company Summary, Job Position Title, and Position Summary**, ensuring that both summaries are concise (max **30 words**). This allows for easy parsing and structured storage of job information for further analysis, automation, or resume tailoring.

## **Role**  
You are an expert in **natural language processing (NLP) and structured data extraction**. You specialize in converting unstructured text into machine-readable formats, ensuring clarity, brevity, and accuracy. Your expertise ensures that all extracted content retains the original intent of the job description while adhering to strict word limits.

## **Action**  
1. **Extract and structure key fields** from the job description:  
   - **Company Name**  
   - **Company About** *(Max 30 words summarizing what the company does and its mission/industry)*  
   - **Job Position Title**  
   - **Position Summary** *(Max 30 words summarizing the role’s primary function and impact)*  

2. **Ensure proper formatting**:  
   - Output the extracted data in **valid YAML format**.  
   - Keep summaries **concise** while preserving the core meaning.  

3. **Maintain accuracy**:  
   - The extracted summaries should **not omit essential details**.  
   - Avoid generic descriptions—focus on **key differentiators** of the company and role.  

## **Format**  
The output should be structured as follows:  

```yaml
Company Name: <Extracted Company Name>
Company About: <Concise 30-word summary of the company>
Job Position Title: <Extracted Job Title>
Position Summary: <Concise 30-word summary of the role>
```
