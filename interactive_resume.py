import pandas as pd
import plotly.express as px

# Prepare the DataFrame
data = {
    "Role": [
        "Head TA | Data100",
        "Software Engineering & Data Analyst Intern | TechCarrot",
        "Research & Software Engineering Intern | Arta Finance",
        "Academic Intern | CS61B",
    ],
    "Organization": [
        "U.C. Berkeley College of Computing, Data Science, and Society",
        "TechCarrot",
        "Arta Finance",
        "U.C. Berkeley Department of Electrical Engineering and Computer Sciences",
    ],
    "Start": [
        "2023-08-01",
        "2024-05-01",
        "2023-05-01",
        "2023-01-01",
    ],
    "End": [
        "2024-05-31",
        "2024-08-31",
        "2023-08-31",
        "2024-05-31",
    ],
    "Description": [
        "Coordinating course logistics for 1000+ students, hands-on teaching support, and Python automation for grading efficiency.",
        "Developed LLM solutions using OpenAI and Flask, and created dashboards using Microsoft Fabric and PowerBI.",
        "Conducted multivariate risk analysis and developed Java-based software for portfolio optimization. Improved financial modeling software with Bazel and Redis.",
        "Guided students in OOP and program design, assisted in debugging, and supported assignments with JUnit testing.",
    ],
}

df = pd.DataFrame(data)

# Create the Plotly Timeline
fig = px.timeline(
    df,
    x_start="Start",
    x_end="End",
    y="Role",
    hover_name="Organization",
    hover_data={"Description": True, "Start": True, "End": True},
    color="Organization",
    template="plotly_dark",
    title="Interactive Resume Timeline",
)

# Adjust the layout for better visibility
fig.update_layout(
    xaxis_title="Timeline",
    yaxis_title="Roles",
    title_x=0.5,
    font=dict(family="Raleway, sans-serif", size=14),
)

# Save the visualization as an HTML file
fig.write_html("interactive_resume.html")
