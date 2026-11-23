
import os
import json

from dotenv import load_dotenv
from google import genai
from search import search

# Load API key
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=API_KEY)

MODEL = "gemini-3.5-flash"


# --------------------------------
# 1. Understand user's job request
# --------------------------------

def understand_request(user_request):

    prompt = f"""
    Extract job search information from the user's request.

    Return JSON with these fields:
    skills: list of strings
    level: intern, junior, mid, senior, or null
    location: location name or null
    search_query: a clear semantic job search query

    User request: {user_request}
    """

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt,
            config={"response_mime_type": "application/json"}
        )

        details = json.loads(response.text)

        # Normalize location names
        if details.get("location"):
            city = details["location"].lower()

            aliases = {
                "bangalore": "Bengaluru",
                "bengaluru": "Bengaluru"
            }

            details["location"] = aliases.get(
                city, details["location"]
            )

        print("Request understood using Gemini AI.")

        return details

    except Exception as e:

        print("Gemini unavailable. Using local fallback.")
        print("Reason:", str(e))

        request = user_request.lower()

        # Extract skills
        known_skills = [
            "python",
            "c++",
            "c",
            "java",
            "sql",
            "dsa",
            "machine learning",
            "html",
            "css",
            "javascript",
            "react",
            "data science"
        ]

        skills = []

        for skill in known_skills:
            if skill in request:
                skills.append(skill)

        # Extract experience level
        level = None

        for item in ["intern", "junior", "mid", "senior"]:
            if item in request:
                level = item
                break

        # Extract location
        location = None

        locations = {
            "bangalore": "Bengaluru",
            "bengaluru": "Bengaluru",
            "delhi": "Delhi",
            "mumbai": "Mumbai",
            "hyderabad": "Hyderabad",
            "pune": "Pune",
            "noida": "Noida",
            "gurgaon": "Gurgaon"
        }

        for city, canonical_name in locations.items():
            if city in request:
                location = canonical_name
                break

        search_query = " ".join(skills) + " " + user_request

        return {
            "skills": skills,
            "level": level,
            "location": location,
            "search_query": search_query.strip()
        }


# --------------------------------
# 2. Explain job recommendations
# --------------------------------

def explain_matches(user_request, jobs):

    if not jobs:
        return jobs

    try:

        prompt = f"""
        Explain why each job matches the user's request.

        User request:
        {user_request}

        Jobs:
        {json.dumps(jobs)}

        Return JSON:
        {{
            "matches": [
                {{
                    "job_id": 1,
                    "explanation": "Short explanation"
                }}
            ]
        }}

        Use only the supplied information.
        Do not invent requirements or company details.
        """

        response = client.models.generate_content(
            model=MODEL,
            contents=prompt,
            config={"response_mime_type": "application/json"}
        )

        data = json.loads(response.text)

        explanations = {
            int(item["job_id"]): item["explanation"]
            for item in data["matches"]
        }

    except Exception:

        print("AI explanations unavailable. Using fallback.")

        explanations = {}

    for job in jobs:

        job["explanation"] = explanations.get(
            job["job_id"],
            (
                f"Matches your requested experience level "
                f"and location. Semantic similarity: "
                f"{job['similarity']}."
            )
        )

    return jobs


# --------------------------------
# 3. Main job matching agent
# --------------------------------

def find_jobs(user_request):

    # Understand request
    details = understand_request(user_request)

    print("\nExtracted Details:")
    print(json.dumps(details, indent=4))

    # Search matching jobs
    jobs = search(
        details["search_query"],
        k=5,
        level=details["level"],
        location=details["location"]
    )

    # Generate explanations
    jobs = explain_matches(user_request, jobs)

    # Final structured response
    result = {
        "user_request": user_request,
        "extracted_details": details,
        "recommended_jobs": jobs
    }

    return result


# --------------------------------
# 4. Run the agent
# --------------------------------

if __name__ == "__main__":

    request = input("\nDescribe the job you want: ")

    result = find_jobs(request)

    print("\n========== AI JOB MATCHER ==========")

    print(json.dumps(result, indent=4))

    if not result["recommended_jobs"]:
        print("\nNo matching jobs found. Try another location or experience level.")
