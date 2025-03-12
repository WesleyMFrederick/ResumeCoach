# Project Brief: ResumeCoach

## Overview
ResumeCoach is an agentic AI application that helps users tailor their resumes to specific job descriptions. The system ingests a job description, the user's work experience, and the current version of the user's resume. Through an iterative process of analysis and generation, the AI produces a tailored resume optimized for the target position.

## Core Features
- **Job Description Analysis**
  - Extract job metadata and requirements
  - Identify the top 10 qualities the ideal candidate should possess
  - Generate a sample resume profile for the perfect candidate

- **User Experience Processing**
  - Ingest the user's work experience using a structured format (Company, Project, Situation, Objectives, Obstacle, Actions, Results, Tools, & Skills)
  - Analyze the user's current resume text

- **Resume Generation**
  - Create optimized work experience bullet points that highlight relevant skills matching job requirements
  - Generate a complete, tailored resume text that emphasizes the user's qualifications for the specific position

## Target Users
Product managers with 10+ years of experience who have some technical coding background, using VS Code.

## Technical Implementation
- **Framework:** PocketFlow for agentic workflow orchestration
- **AI Models:** 
  - OpenAI ChatGPT
  - Anthropic Claude
  - Google Gemini
- **Development Environment:** VS Studio Code with Cline AI
