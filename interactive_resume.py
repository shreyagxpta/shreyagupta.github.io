import pandas as pd
import plotly.express as px

# Prepare the DataFrame
data = {
    "Role": [
        "Head TA @ Data100 - Principles & Techniques of Data Science",
        "TechCarrot | Software Engineering & Data Analyst Intern",
        "Arta Finance | Research & Software Engineering Intern",
        "Academic Intern @ CS61B - Data Structures",
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
        "2025-05-31",
        "2024-08-31",
        "2023-08-31",
        "2023-05-31",
    ],
    "Description": [
        "Coordinating course logistics for 1000+ students, hands-on teaching support, and Python automation for grading efficiency.",
        "Developed LLM solutions using OpenAI and Flask, and created dashboards using Microsoft Fabric and PowerBI.",
        "Conducted multivariate risk analysis and developed Java-based software for portfolio optimization. Improved financial modeling software with Bazel and Redis.",
        "Guided students in OOP and program design, assisted in debugging, and supported assignments with JUnit testing.",
    ],
}

df = pd.DataFrame(data)

# Define a custom color scale
custom_colors = {
    "U.C. Berkeley Department of Electrical Engineering and Computer Sciences": "#1E90FF",  # Deep Blue: Professional and distinct
    "Arta Finance": "#20B2AA",  # Teal: Sleek and modern
    "TechCarrot": "#9ACD32",  # Olive Green: Subtle yet energetic
    "U.C. Berkeley College of Computing, Data Science, and Society": "#DAA520",  # Goldenrod: Rich and bold
}

# Create the timeline visualization
fig = px.timeline(
    df,
    x_start="Start",
    x_end="End",
    y="Role",
    hover_name="Role",  # Ensure Role appears as the hover title
    hover_data={
        "Description": True,  # Include the detailed description
        "Organization": True,  # Show Organization in hover
        "Start": False,  # Hide start date in hover
        "End": False,  # Hide end date in hover
    },
    color="Organization",
    color_discrete_map=custom_colors,
    template="plotly_dark",
    title="Work Experience Timeline",
)

# Customize layout
fig.update_layout(
    xaxis_title="Timeline",
    yaxis_title="",
    title_x=0.5,
    font=dict(
        family="Lato, Arial, sans-serif",
        size=14,
        color="#FFFFFF",
    ),
    plot_bgcolor="rgba(34, 34, 34, 0.7)",  # Translucent dark background
    paper_bgcolor="rgba(34, 34, 34, 0.7)",
)

# Customize hover labels
fig.update_traces(
    hoverlabel=dict(
        font_size=12,
        font_family="Lato, Arial, sans-serif",
    )
)

# Save as an HTML file
fig.write_html("interactive_resume.html")
