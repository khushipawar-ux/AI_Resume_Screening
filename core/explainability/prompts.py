"""
Prompts Module
"""

EXPLANATION_PROMPT = """
Given the following resume and job description, explain why the match score is {score}:

Resume:
{resume}

Job Description:
{jd}

Provide a detailed explanation covering:
1. Key matching skills
2. Experience alignment
3. Education fit
4. Areas of strength
5. Potential gaps
"""

SKILL_GAP_PROMPT = """
Analyze the skill gap between the candidate and job requirements:

Candidate Skills: {candidate_skills}
Required Skills: {required_skills}

Provide:
1. Missing critical skills
2. Matching skills
3. Transferable skills
4. Recommendations for upskilling
"""
