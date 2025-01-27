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

# Define a custom color scale
custom_colors = {
    "U.C. Berkeley Department of Electrical Engineering and Computer Sciences": "#4A90E2",  # Soft Blue: Trustworthy and calming
    "Arta Finance": "#50E3C2",  # Aqua Green: Refreshing and innovative
    "TechCarrot": "#B8E986",  # Lime Green: Energetic and optimistic
    "U.C. Berkeley College of Computing, Data Science, and Society": "#F5A623",  # Golden Yellow: Bright and forward-looking
}


fig = px.timeline(
    df,
    x_start="Start",
    x_end="End",
    y="Role",
    hover_name="Organization",  # Show only Organization as the hover title
    hover_data={"Description": True, "Role": False, "Start": False, "End": False},  # Exclude Role, Start, and End
    color="Organization",
    color_discrete_map=custom_colors,
    template="plotly_dark",
    title="Work Experience Timeline",
)

# Adjust the layout for better visibility and theme
fig.update_layout(
    xaxis_title="Timeline",
    title_x=0.5,
    font=dict(
        family="Lato, Arial, sans-serif",  # Choose a clean, modern font
        size=14,  # Adjust the font size
        color="#FFFFFF"  # Set the font color (white)
    ),
    plot_bgcolor="rgba(34, 34, 34, 0.7)",  # Translucent background (dark gray, 70% opacity)
    paper_bgcolor="rgba(34, 34, 34, 0.7)",
)

# Adjust hover label font size and style
fig.update_traces(
    hoverlabel=dict(
        font_size=12,  # Adjust font size for hover box
        font_family="Lato, Arial, sans-serif",  # Match graph font
    )
)


# Save the visualization as an HTML file
fig.write_html("interactive_resume.html")
