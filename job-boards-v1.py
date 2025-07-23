import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Job Websites Directory", layout="wide")

# Title and description
st.title("Job Websites Directory")
st.markdown("Explore a comprehensive list of job websites, including general job boards, remote work platforms, freelance/gig economy sites, and industry-specific resources. Filter by website name using the sidebar.")

# Data for the job websites
job_data = [
    {"Job Website": "Indeed", "URL": "https://www.indeed.com", "Description": "Largest job search engine with millions of listings, resume uploads, and alerts."},
    {"Job Website": "LinkedIn", "URL": "https://www.linkedin.com", "Description": "Professional networking platform with job listings and Easy Apply feature."},
    {"Job Website": "Glassdoor", "URL": "https://www.glassdoor.com", "Description": "Job listings with company reviews, salary data, and interview insights."},
    {"Job Website": "Monster", "URL": "https://www.monster.com", "Description": "Job board with career advice, resume tools, and AI-powered interview prep."},
    {"Job Website": "CareerBuilder", "URL": "https://www.careerbuilder.com", "Description": "Large job database with AI-driven job matching and resume tools."},
    {"Job Website": "ZipRecruiter", "URL": "https://www.ziprecruiter.com", "Description": "AI-driven job matching, resume uploads, and multi-board job posting."},
    {"Job Website": "SimplyHired", "URL": "https://www.simplyhired.com", "Description": "Aggregates job listings with a user-friendly interface and job alerts."},
    {"Job Website": "Google for Jobs", "URL": "https://www.google.com", "Description": "Aggregates listings from various sources, displayed in Google search results."},
    {"Job Website": "Snagajob", "URL": "https://www.snagajob.com", "Description": "Focuses on hourly and part-time jobs in retail, hospitality, and healthcare."},
    {"Job Website": "Job.com", "URL": "https://www.job.com", "Description": "Uses blockchain for job matching and direct employer communication."},
    {"Job Website": "FlexJobs", "URL": "https://www.flexjobs.com", "Description": "Hand-screened remote, hybrid, and flexible jobs (subscription required)."},
    {"Job Website": "Remote.co", "URL": "https://www.remote.co", "Description": "Curates remote job listings in various fields with remote work resources."},
    {"Job Website": "We Work Remotely", "URL": "https://www.weworkremotely.com", "Description": "Remote startup jobs, especially in tech, design, and marketing."},
    {"Job Website": "RemoteOK", "URL": "https://remoteok.com", "Description": "Remote tech and startup jobs with salary transparency."},
    {"Job Website": "SkiptheDrive", "URL": "https://www.skipthedrive.com", "Description": "Niche platform for remote job listings across industries."},
    {"Job Website": "Workew", "URL": "https://www.workew.com", "Description": "Remote jobs in tech and creative fields."},
    {"Job Website": "Remotive", "URL": "https://remotive.com", "Description": "Remote job listings with a community for remote workers."},
    {"Job Website": "Jobspresso", "URL": "https://jobspresso.co", "Description": "High-quality remote jobs in tech and creative fields."},
    {"Job Website": "WFH.io", "URL": "https://wfh.io", "Description": "Remote tech jobs, including software development and IT roles."},
    {"Job Website": "Remotees", "URL": "https://remotees.com", "Description": "Niche remote job board for tech and design roles."},
    {"Job Website": "Remotely Awesome Jobs", "URL": "https://remotelyawesomejobs.com", "Description": "Remote opportunities in tech and startups."},
    {"Job Website": "Remote4Me", "URL": "https://remote4me.com", "Description": "Niche remote job board with a simple interface."},
    {"Job Website": "100 Telecommute Jobs", "URL": "https://100telecommutejobs.com", "Description": "Focuses on telecommuting roles across industries."},
    {"Job Website": "Remote Jobs Club", "URL": "https://remotejobsclub.com", "Description": "Curates remote job opportunities with a community focus."},
    {"Job Website": "Werk", "URL": "https://werk.co", "Description": "Flexible and remote jobs for non-traditional work arrangements."},
    {"Job Website": "Dynamite Jobs", "URL": "https://dynamitejobs.com", "Description": "Remote jobs with a focus on startups and small businesses."},
    {"Job Website": "Outsourcely", "URL": "https://www.outsourcely.com", "Description": "Connects businesses with remote freelancers for long-term projects."},
    {"Job Website": "Upwork", "URL": "https://www.upwork.com", "Description": "Freelance platform for short-term and long-term projects in various fields."},
    {"Job Website": "Fiverr", "URL": "https://www.fiverr.com", "Description": "Gig-based freelance platform for creative and technical services."},
    {"Job Website": "Freelancer.com", "URL": "https://www.freelancer.com", "Description": "Connects freelancers with clients for project-based work."},
    {"Job Website": "Toptal", "URL": "https://www.toptal.com", "Description": "High-end freelance platform for top-tier tech, design, and finance talent."},
    {"Job Website": "PeoplePerHour", "URL": "https://www.peopleperhour.com", "Description": "Freelance platform for creative and technical projects, popular globally."},
    {"Job Website": "ServiceScape", "URL": "https://www.servicescape.com", "Description": "Freelance platform for writing, editing, and translation jobs."},
    {"Job Website": "OdeskWork", "URL": "https://www.odeskwork.com", "Description": "Freelance platform similar to Upwork for project-based work."},
    {"Job Website": "Dice", "URL": "https://www.dice.com", "Description": "Tech and IT job board for software developers, engineers, and IT roles."},
    {"Job Website": "Stack Overflow", "URL": "https://stackoverflow.com/jobs", "Description": "Job board for software developers, integrated with its Q&A community."},
    {"Job Website": "Dribbble", "URL": "https://dribbble.com/jobs", "Description": "Job board for graphic designers to showcase portfolios and find work."},
    {"Job Website": "Behance", "URL": "https://www.behance.net/joblist", "Description": "Portfolio and job platform for creative professionals like UI/UX designers."},
    {"Job Website": "ProBlogger", "URL": "https://problogger.com/jobs", "Description": "Job board for writing, blogging, and content creation roles."},
    {"Job Website": "TechCareers", "URL": "https://techcareers.com", "Description": "Tech and engineering job listings with weekly updates."},
    {"Job Website": "LawCrossing", "URL": "https://www.lawcrossing.com", "Description": "Legal job board for paralegals, attorneys, and legal professionals."},
    {"Job Website": "TeachAway", "URL": "https://www.teachaway.com", "Description": "International teaching jobs, including English teaching abroad."},
    {"Job Website": "Idealist", "URL": "https://www.idealist.org", "Description": "Nonprofit and mission-driven jobs, internships, and volunteer opportunities."},
    {"Job Website": "ArtJobs", "URL": "https://artjobs.com", "Description": "Jobs in theatre, arts, culture, and education."},
    {"Job Website": "BlackTechPipeline", "URL": "https://blacktechpipeline.com", "Description": "Tech jobs for Black professionals, focusing on diversity and inclusion."},
    {"Job Website": "Wellfound", "URL": "https://www.wellfound.com", "Description": "Startup jobs with salary and equity transparency."},
    {"Job Website": "Handshake", "URL": "https://joinhandshake.com", "Description": "Job board for college students and recent graduates, focusing on internships."},
    {"Job Website": "CV-Library", "URL": "https://www.cv-library.co.uk", "Description": "UK-focused job board with resume uploads and career advice."},
    {"Job Website": "Jooble", "URL": "https://jooble.org", "Description": "International job search engine aggregating listings from multiple sources."},
    {"Job Website": "99designs", "URL": "https://99designs.com", "Description": "Freelance platform for graphic designers to find project-based work."},
    {"Job Website": "Working Nomads", "URL": "https://www.workingnomads.com", "Description": "Remote jobs, primarily in tech, marketing, and design."},
    {"Job Website": "JupiterHR", "URL": "https://jupiterhr.com", "Description": "Lesser-known job board for various industries with less competitive listings."},
    {"Job Website": "Work In Startups", "URL": "https://workinstartups.com", "Description": "Startup jobs, particularly in the UK and tech sectors."},
    {"Job Website": "Hubstaff Talent", "URL": "https://talent.hubstaff.com", "Description": "Connects freelancers and remote workers with businesses in tech and creative roles."},
    {"Job Website": "SkillUp", "URL": "https://skillup.org", "Description": "Jobs and training resources for career changers without degrees."},
    {"Job Website": "Craigslist", "URL": "https://www.craigslist.org", "Description": "Local job listings, especially for freelance and gig work (vet carefully)."},
    {"Job Website": "USAJOBS", "URL": "https://www.usajobs.gov", "Description": "Federal government jobs with detailed application processes."}
]

# Convert to DataFrame
df = pd.DataFrame(job_data)

# Sidebar for filtering
st.sidebar.header("Filter Job Websites")
search_term = st.sidebar.text_input("Search by Job Website Name", "")

# Filter DataFrame based on search term
if search_term:
    df = df[df["Job Website"].str.contains(search_term, case=False, na=False)]

# Display the table
st.subheader("Job Websites List")
# Create a clickable URL column
df["URL"] = df["URL"].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')
# Use st.markdown to render HTML for clickable links
st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)

# Styling for better readability
st.markdown("""
    <style>
    table {
        width: 100%;
        border-collapse: collapse;
    }
    th, td {
        padding: 10px;
        text-align: left;
        border: 1px solid #ddd;
    }
    th {
        background-color: #f2f2f2;
        font-weight: bold;
    }
    tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    tr:hover {
        background-color: #f1f1f1;
    }
    </style>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("**Notes**: Use the sidebar to filter by job website name. Click the URLs to visit the sites. For subscription-based platforms like FlexJobs, check pricing on their websites. For xAI-related services, visit [x.ai/grok](https://x.ai/grok) or [help.x.com](https://help.x.com/en/using-x/x-premium).")
