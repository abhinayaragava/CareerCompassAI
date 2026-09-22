import os

from flask import Flask, render_template, request, redirect, url_for, session
from career_recommendation import get_career_recommendations
from graduation_recommendations import recommend_graduation_careers
from graduation_skill_gap import analyze_graduation_skill_gap
from graduation_higher_education import recommend_graduation_higher_education
from graduation_exams import recommend_graduation_exams
from graduation_jobs import recommend_graduation_jobs
from higher_education import higher_education
from after12th_recommendations import (
    AFTER_12TH_CAREER_DOMAINS,
    recommend_after12th_careers,
    recommend_after12th_exams,
    recommend_after12th_higher_education,
    analyze_after12th_skill_gap,
    generate_after12th_learning_roadmap,
    recommend_after12th_learning_resources,
    recommend_after12th_exam_preparation,
    generate_after12th_next_steps
)





from after10th_recommendations import (
    recommend_after10th_pathways,
    recommend_after10th_careers,
    generate_after10th_next_steps,
    generate_after10th_stream_guidance,
    recommend_after10th_exams,
    generate_after10th_career_roadmap,
    generate_after10th_skill_guidance,
    recommend_after10th_learning_resources
)



import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key for login sessions
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")


# ==========================================
# DATABASE CONNECTION
# ==========================================

def get_db_connection():
    connection = sqlite3.connect("careercompass.db")
    connection.row_factory = sqlite3.Row
    return connection


# ==========================================
# CREATE DATABASE TABLES
# ==========================================

def init_db():

    connection = get_db_connection()

    # Users table
    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # Student profile table
    connection.execute("""
        CREATE TABLE IF NOT EXISTS profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE NOT NULL,
            education TEXT,
            branch TEXT,
            cgpa TEXT,
            skills TEXT,
            interests TEXT,
            strengths TEXT,
            career_goal TEXT,
            career_type TEXT,
            work_preference TEXT,
            exam_interest TEXT,
            exam_preferences TEXT,
            certifications TEXT,
            projects TEXT,
            experience TEXT,
            location_preference TEXT,
            about TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)



    # --------------------------------------
    # AFTER 12TH PROFILE FIELDS
    # --------------------------------------

    existing_columns = [
        row["name"]
        for row in connection.execute(
            "PRAGMA table_info(profiles)"
        ).fetchall()
    ]
    twelfth_columns = {
        "twelfth_percentage": "TEXT",
        "twelfth_board": "TEXT",
        "twelfth_stream": "TEXT",
        "subjects_studied": "TEXT",
        "strongest_subjects": "TEXT",
        "interests_12th": "TEXT",
        "career_direction": "TEXT",
        "twelfth_exam_interest": "TEXT",
        "problem_type": "TEXT",
        "work_style": "TEXT",

        "education_stage": "TEXT",
        "graduation_degree": "TEXT",
        "graduation_status": "TEXT",
        "graduation_domain": "TEXT",
        "graduation_goal": "TEXT",
        "graduation_work_style": "TEXT",
        "graduation_interests": "TEXT"
    }









    for column_name, column_type in twelfth_columns.items():

        if column_name not in existing_columns:

            connection.execute(
                f"ALTER TABLE profiles ADD COLUMN {column_name} {column_type}"
            )
    connection.commit()













    connection.close()


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# REGISTER
# ==========================================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        connection = get_db_connection()

        try:

            connection.execute(
                """
                INSERT INTO users (name, email, password)
                VALUES (?, ?, ?)
                """,
                (name, email, hashed_password)
            )

            connection.commit()

        except sqlite3.IntegrityError:

            connection.close()

            return "Email already registered."

        connection.close()

        return redirect(url_for("login"))

    return render_template("register.html")


# ==========================================
# LOGIN
# ==========================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        connection = get_db_connection()

        user = connection.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,)
        ).fetchone()

        connection.close()

        if user and check_password_hash(
            user["password"],
            password
        ):

            session["user_id"] = user["id"]
            session["user_name"] = user["name"]

            return redirect(url_for("dashboard"))

        return "Invalid email or password."

    return render_template("login.html")


# ==========================================
# DASHBOARD
# ==========================================

@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html")


# ==========================================
# PROFILE
# ==========================================

@app.route("/profile", methods=["GET", "POST"])
def profile():

    # Student must be logged in
    if "user_id" not in session:
        return redirect(url_for("login"))

    connection = get_db_connection()

    # --------------------------------------
    # SAVE PROFILE
    # --------------------------------------

    if request.method == "POST":

        education = request.form.get("education")
        education_stage = request.form.get("education_stage")
        branch = request.form.get("branch")
        cgpa = request.form.get("cgpa")

        selected_skills = request.form.getlist("skills")
        graduation_skills = request.form.getlist("graduation_skills")

        if education_stage == "graduation" and graduation_skills:
            skills = ", ".join(graduation_skills)
        else:
            skills = ", ".join(selected_skills)

        interests = request.form.get("interests")
        strengths = request.form.get("strengths")
        career_goal = request.form.get("career_goal")
        career_type = request.form.get("career_type")
        work_preference = request.form.get("work_preference")
        exam_interest = request.form.get("exam_interest")
        exam_preferences = request.form.get("exam_preferences")
        certifications = request.form.get("certifications")
        projects = request.form.get("projects")
        experience = request.form.get("experience")
        location_preference = request.form.get("location_preference")
        about = request.form.get("about")

        # --------------------------------------
        # GRADUATION PROFILE DATA
        # --------------------------------------
        graduation_degree = request.form.get("graduation_degree")
        graduation_status = request.form.get("graduation_status")
        graduation_domain = request.form.get("graduation_domain")
        graduation_goal = request.form.get("graduation_goal")
        graduation_work_style = request.form.get("graduation_work_style")
        graduation_interests = request.form.get("graduation_interests")


        # --------------------------------------
        # AFTER 12TH PROFILE DATA
        # --------------------------------------

        twelfth_percentage = request.form.get("twelfth_percentage")
        twelfth_board = request.form.get("twelfth_board")
        twelfth_stream = request.form.get("twelfth_stream")
        subjects_studied = request.form.get("subjects_studied")
        strongest_subjects = ", ".join(request.form.getlist("strongest_subjects"))
        interests_12th = request.form.get("interests_12th")
        career_direction = request.form.get("career_direction")
        problem_type = request.form.get("problem_type")

        work_style = request.form.get("work_style")

        twelfth_exam_interest = request.form.get("exam_interest")

        # --------------------------------------
        # AFTER 10TH PROFILE DATA
        # --------------------------------------

        tenth_percentage = request.form.get("tenth_percentage")
        tenth_board = request.form.get("tenth_board")
        favorite_subjects = request.form.get("favorite_subjects")
        interests_10th = request.form.get("interests_10th")
        activity_interest = request.form.get("activity_interest")
        career_interests_10th = request.form.get("career_interests_10th")
        after10_pathway = ", ".join(request.form.getlist("after10_pathway"))

        # Check whether profile already exists
        existing_profile = connection.execute(
            """
            SELECT id FROM profiles
            WHERE user_id = ?
            """,
            (session["user_id"],)
        ).fetchone()

        if existing_profile:

            # Update existing profile
            connection.execute(
                """
                UPDATE profiles
                SET
                    education = ?,
                    education_stage = ?,
                    branch = ?,
                    cgpa = ?,
                    skills = ?,
                    interests = ?,
                    strengths = ?,
                    career_goal = ?,
                    career_type = ?,
                    work_preference = ?,
                    exam_interest = ?,
                    exam_preferences = ?,
                    certifications = ?,
projects=?,
                    experience = ?,
location_preference = ?,
about = ?,
twelfth_percentage = ?,
twelfth_board = ?,
twelfth_stream = ?,
subjects_studied = ?,
strongest_subjects = ?,
interests_12th = ?,
career_direction = ?,
problem_type = ?,
work_style = ?,
twelfth_exam_interest = ?,
                    tenth_percentage = ?,
                    tenth_board = ?,
                    favorite_subjects = ?,
                    interests_10th = ?,
                    activity_interest = ?,
                    career_interests_10th = ?,
                    after10_pathway = ?,
                    graduation_degree = ?,
                    graduation_status = ?,
                    graduation_domain = ?,
                    graduation_goal = ?,
                    graduation_work_style = ?,
                    graduation_interests = ?
WHERE user_id = ?





                """,
                (
                    education,
                    education_stage,
                    branch,
                    cgpa,
                    skills,
                    interests,
                    strengths,
                    career_goal,
                    career_type,
                    work_preference,
                    exam_interest,
                    exam_preferences,
                    certifications,
                    projects,
                    experience,
                    location_preference,
                    about,
                    twelfth_percentage,
                    twelfth_board,
                    twelfth_stream,
                    subjects_studied,
                    strongest_subjects,
                    interests_12th,
                    career_direction,
                    problem_type,
                    work_style,
                    twelfth_exam_interest,
                    tenth_percentage,
                    tenth_board,
                    favorite_subjects,
                    interests_10th,
                    activity_interest,
                    career_interests_10th,
                    after10_pathway,
                    graduation_degree,
                    graduation_status,
                    graduation_domain,
                    graduation_goal,
                    graduation_work_style,
                    graduation_interests,
                    session["user_id"]
                )
            )

      
           

        else:

            # Create new profile
            connection.execute(
                """
                INSERT INTO profiles (
                    user_id,
                    education,
                    education_stage,
                    branch,
                    cgpa,
                    skills,
                    interests,
                    strengths,
                    career_goal,
                    career_type,
                    work_preference,
                    exam_interest,
                    exam_preferences,
                    certifications,
                    projects,
                    experience,
                    location_preference,
                    about,
                    twelfth_percentage,
                    twelfth_board,
                    twelfth_stream,
                    subjects_studied,
                    strongest_subjects,
                    interests_12th,
                    career_direction,
                    problem_type,
                    work_style,
                    twelfth_exam_interest,
                    tenth_percentage,
                    tenth_board,
                    favorite_subjects,
                    interests_10th,
                    activity_interest,
                    career_interests_10th,
                    after10_pathway,
                    graduation_degree,
                    graduation_status,
                    graduation_domain,
                    graduation_goal,
                    graduation_work_style,
                    graduation_interests
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    session["user_id"],
                    education,
                    education_stage,
                    branch,
                    cgpa,
                    skills,
                    interests,
                    strengths,
                    career_goal,
                    career_type,
                    work_preference,
                    exam_interest,
                    exam_preferences,
                    certifications,
                    projects,
                    experience,
                    location_preference,
                    about,
                    twelfth_percentage,
                    twelfth_board,
                    twelfth_stream,
                    subjects_studied,
                    strongest_subjects,
                    interests_12th,
                    career_direction,
                    problem_type,
                    work_style,
                    twelfth_exam_interest,
                    tenth_percentage,
                    tenth_board,
                    favorite_subjects,
                    interests_10th,
                    activity_interest,
                    career_interests_10th,
                    after10_pathway,
                    graduation_degree,
                    graduation_status,
                    graduation_domain,
                    graduation_goal,
                    graduation_work_style,
                    graduation_interests
                )
            )


        connection.commit()
        connection.close()

        return redirect(url_for("profile"))

    # --------------------------------------
    # LOAD EXISTING PROFILE
    # --------------------------------------

    student_profile = connection.execute(
        """
        SELECT * FROM profiles
        WHERE user_id = ?
        """,
        (session["user_id"],)
    ).fetchone()

    print("DEBUG PROFILE STAGE:", student_profile["education_stage"] if student_profile else "NO PROFILE")









    # --------------------------------------
    # AFTER 10TH CAREER PATHWAY RECOMMENDATIONS
    # --------------------------------------

    after10th_recommendations = []

    if student_profile:
       after10th_recommendations = recommend_after10th_pathways(
       student_profile["interests_10th"],
       student_profile["favorite_subjects"],
       student_profile["career_interests_10th"],
       student_profile["activity_interest"],
       student_profile["after10_pathway"]
)







    after10th_career_recommendations = []

    if student_profile and after10th_recommendations:
        after10th_career_recommendations = recommend_after10th_careers(
            after10th_recommendations,
            student_profile["interests_10th"],
            student_profile["favorite_subjects"],
            student_profile["career_interests_10th"],
            student_profile["activity_interest"]
        )

    after10th_next_steps = generate_after10th_next_steps(
        after10th_recommendations
    )

    after10th_stream_guidance = generate_after10th_stream_guidance(
        after10th_recommendations
    )

    after10th_exams = recommend_after10th_exams(
        after10th_recommendations
    )

    after10th_career_roadmap = generate_after10th_career_roadmap(
        after10th_recommendations
    )

    after10th_skill_guidance = generate_after10th_skill_guidance(
        after10th_recommendations
    )

    after10th_learning_resources = recommend_after10th_learning_resources(
        after10th_recommendations
    )






    # --------------------------------------
    # AFTER 12TH CAREER RECOMMENDATIONS
    # --------------------------------------

    after12th_recommendations = []

    if student_profile and student_profile["twelfth_stream"]:
        after12th_recommendations = recommend_after12th_careers(
            student_profile["twelfth_stream"],
            student_profile["strongest_subjects"],
            student_profile["interests_12th"],
            student_profile["career_direction"],
            student_profile["skills"],
            student_profile["problem_type"],
            student_profile["work_style"]
        )

    # --------------------------------------
    # AFTER 12TH COMPETITIVE EXAM GUIDANCE
    # --------------------------------------

    after12th_exams = []

    if student_profile:
        after12th_exams = recommend_after12th_exams(
            student_profile["interests_12th"],
            student_profile["twelfth_stream"],
            student_profile["twelfth_exam_interest"],
            student_profile["strongest_subjects"],
            student_profile["career_direction"]
        )
    # --------------------------------------
    # AFTER 12TH EXAM PREPARATION GUIDANCE
    # --------------------------------------

    after12th_exam_preparation = []

    if after12th_exams:
        after12th_exam_preparation = recommend_after12th_exam_preparation(
            after12th_exams
        )




    # --------------------------------------
    # AFTER 12TH HIGHER EDUCATION GUIDANCE
    # --------------------------------------

    after12th_higher_education = []

    if student_profile:
        after12th_higher_education = recommend_after12th_higher_education(
            student_profile["interests_12th"],
            student_profile["twelfth_stream"],
            student_profile["strongest_subjects"],
            student_profile["career_direction"]
        )



    # AFTER 12TH SKILL GAP ANALYSIS
    # --------------------------------------

    after12th_skill_gap = {
        "possessed": [],
        "missing": []
    }

    if student_profile and after12th_recommendations:
        top_career = after12th_recommendations[0]["career"]

        after12th_skill_gap = analyze_after12th_skill_gap(
            top_career,
            student_profile["skills"] or ""
        )

# --------------------------------------
# AFTER 12TH PERSONALIZED LEARNING ROADMAP
# --------------------------------------

    after12th_learning_roadmap = []

    if after12th_recommendations:
        top_career = after12th_recommendations[0]["career"]

        after12th_learning_roadmap = generate_after12th_learning_roadmap(
            top_career,
            after12th_skill_gap
        )

    # --------------------------------------
    # AFTER 12TH FREE LEARNING RESOURCES
    # --------------------------------------

    after12th_learning_resources = []

    if after12th_learning_roadmap:
        after12th_learning_resources = recommend_after12th_learning_resources(
            top_career,
            after12th_learning_roadmap
        )





    # --------------------------------------
    # AFTER 12TH CAREER ROADMAP SUMMARY
    # --------------------------------------

    after12th_career_roadmap = []

    if after12th_recommendations:

        top_career_data = after12th_recommendations[0]

        after12th_career_roadmap = {
            "career": top_career_data.get("career"),
            "match_score": top_career_data.get("score"),
            "higher_education": after12th_higher_education,
            "exams": after12th_exams,
            "skills_to_develop": after12th_skill_gap.get("missing", []),
            "learning_roadmap": after12th_learning_roadmap,
            "learning_resources": after12th_learning_resources
        }



    # --------------------------------------
    # AFTER 12TH PERSONALIZED NEXT STEPS
    # --------------------------------------

    after12th_next_steps = []

    if after12th_recommendations:

        top_career = after12th_recommendations[0].get("career")

        after12th_next_steps = generate_after12th_next_steps(
            top_career,
            after12th_skill_gap,
            after12th_learning_roadmap,
            after12th_exams
        )




    # --------------------------------------
    # GRADUATION CAREER RECOMMENDATIONS
    # --------------------------------------

    graduation_recommendations = []

    if student_profile:
        graduation_recommendations = recommend_graduation_careers(
            student_profile["graduation_degree"] or "",
            student_profile["branch"] or "",
            student_profile["cgpa"] or "",
            student_profile["graduation_domain"] or "",
            student_profile["graduation_goal"] or "",
            student_profile["graduation_work_style"] or "",
            student_profile["graduation_interests"] or "",
            student_profile["skills"] or ""
        )

    # --------------------------------------
    # GRADUATION SKILL GAP ANALYSIS
    # --------------------------------------

    graduation_skill_gap = {
        "career": "",
        "required": [],
        "possessed": [],
        "missing": [],
        "priority": [],
        "coverage": 0
    }

    if student_profile and graduation_recommendations:

        top_graduation_career = graduation_recommendations[0]

        graduation_skill_gap = analyze_graduation_skill_gap(
            student_profile["skills"] or "",
            top_graduation_career
        )

    # --------------------------------------
    # GRADUATION HIGHER STUDIES
    # --------------------------------------

    graduation_higher_education = []

    if student_profile:

        top_career_name = ""

        if graduation_recommendations:
            top_career_name = graduation_recommendations[0].get("career", "")

        graduation_higher_education = recommend_graduation_higher_education(
            student_profile["graduation_degree"] or "",
            student_profile["branch"] or "",
            student_profile["graduation_domain"] or "",
            top_career_name
        )

    # --------------------------------------
    # GRADUATION COMPETITIVE EXAMS
    # --------------------------------------

    graduation_exams = []

    if student_profile:

        top_career_name = ""

        if graduation_recommendations:
            top_career_name = graduation_recommendations[0].get("career", "")

        graduation_exams = recommend_graduation_exams(
            student_profile["graduation_degree"] or "",
            student_profile["branch"] or "",
            student_profile["graduation_domain"] or "",
            student_profile["graduation_goal"] or "",
            top_career_name
        )

    # --------------------------------------
    # GRADUATION CAREER OPPORTUNITIES
    # --------------------------------------

    graduation_jobs = recommend_graduation_jobs(
        graduation_recommendations
    )

    allowed_stages = {"after_10th", "after_12th", "graduation"}

    requested_stage = request.args.get("stage")

    if requested_stage in allowed_stages:
        active_stage = requested_stage
    else:
        active_stage = (
            student_profile["education_stage"]
            if student_profile and student_profile["education_stage"]
            else "after_10th"
        )

    connection.close()

    return render_template(
        "profile.html",
        profile=student_profile,
        active_stage=active_stage,
        graduation_recommendations=graduation_recommendations,
        graduation_skill_gap=graduation_skill_gap,
        graduation_higher_education=graduation_higher_education,
        graduation_exams=graduation_exams,
        graduation_jobs=graduation_jobs,
        after10th_recommendations=after10th_recommendations,
        after10th_career_recommendations=after10th_career_recommendations,
        after10th_next_steps=after10th_next_steps,
        after10th_stream_guidance=after10th_stream_guidance,
        after10th_exams=after10th_exams,
        after10th_career_roadmap=after10th_career_roadmap,
        after10th_skill_guidance=after10th_skill_guidance,
        after10th_learning_resources=after10th_learning_resources,
        after12th_recommendations=after12th_recommendations,
        after12th_exams=after12th_exams,
        after12th_higher_education=after12th_higher_education,
        after12th_skill_gap=after12th_skill_gap,
        after12th_learning_roadmap=after12th_learning_roadmap,
        after12th_learning_resources=after12th_learning_resources,
        after12th_exam_preparation=after12th_exam_preparation,
        after12th_career_roadmap=after12th_career_roadmap,
        after12th_next_steps=after12th_next_steps








    )
# ==========================================
# SAVE GRADUATION PROFILE
# ==========================================

@app.route("/save-graduation", methods=["POST"])
def save_graduation():

    if "user_id" not in session:
        return redirect(url_for("login"))

    graduation_degree = request.form.get("graduation_degree", "").strip()
    branch = request.form.get("branch", "").strip()
    cgpa = request.form.get("cgpa", "").strip()
    graduation_status = request.form.get("graduation_status", "").strip()
    graduation_domain = request.form.get("graduation_domain", "").strip()
    graduation_goal = request.form.get("graduation_goal", "").strip()
    graduation_work_style = request.form.get("graduation_work_style", "").strip()
    graduation_interests = request.form.get("graduation_interests", "").strip()

    graduation_skills = request.form.getlist("graduation_skills")
    skills = ", ".join(graduation_skills)

    connection = get_db_connection()

    existing = connection.execute(
        "SELECT id FROM profiles WHERE user_id = ?",
        (session["user_id"],)
    ).fetchone()

    if existing:

        connection.execute(
            """
            UPDATE profiles
            SET
                education_stage = ?,
                branch = ?,
                cgpa = ?,
                skills = ?,
                graduation_degree = ?,
                graduation_status = ?,
                graduation_domain = ?,
                graduation_goal = ?,
                graduation_work_style = ?,
                graduation_interests = ?
            WHERE user_id = ?
            """,
            (
                "graduation",
                branch,
                cgpa,
                skills,
                graduation_degree,
                graduation_status,
                graduation_domain,
                graduation_goal,
                graduation_work_style,
                graduation_interests,
                session["user_id"]
            )
        )

    else:

        connection.execute(
            """
            INSERT INTO profiles (
                user_id,
                education_stage,
                branch,
                cgpa,
                skills,
                graduation_degree,
                graduation_status,
                graduation_domain,
                graduation_goal,
                graduation_work_style,
                graduation_interests
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                session["user_id"],
                "graduation",
                branch,
                cgpa,
                skills,
                graduation_degree,
                graduation_status,
                graduation_domain,
                graduation_goal,
                graduation_work_style,
                graduation_interests
            )
        )

    connection.commit()
    connection.close()

    return redirect(url_for("profile", stage="graduation"))


# ==========================================
# LOGOUT
# ==========================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))


# ==========================================
# INITIALIZE DATABASE
# ==========================================

init_db()


# ==========================================
# START APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)
# --------------------------------------
# CAREER RECOMMENDATIONS
# --------------------------------------
@app.route("/recommendations")
def recommendations():

    if "user_id" not in session:
        return redirect(url_for("login"))

    connection = get_db_connection()

    student_profile = connection.execute(
        "SELECT * FROM profiles WHERE user_id = ?",
        (session["user_id"],)
    ).fetchone()

    connection.close()

    if not student_profile:
        return redirect(url_for("profile"))

    profile = dict(student_profile)

    career_recommendations = get_career_recommendations(profile)

    return render_template(
        "recommendations.html",
        recommendations=career_recommendations
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
