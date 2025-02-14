from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import os

app = Flask(__name__, static_folder="static")

# Ensure 'generated' folder exists
if not os.path.exists("generated"):
    os.makedirs("generated")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get form data
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        summary = request.form["summary"]
        education = request.form["education"]
        experience = request.form["experience"]
        skills = request.form["skills"]

        # Generate PDF
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)

        pdf.cell(200, 10, "Resume", ln=True, align="C")
        pdf.ln(10)

        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, f"Name: {name}", ln=True)
        pdf.cell(200, 10, f"Email: {email}", ln=True)
        pdf.cell(200, 10, f"Phone: {phone}", ln=True)
        pdf.ln(5)

        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, "Summary:", ln=True)
        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 10, summary)
        pdf.ln(5)

        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, "Education:", ln=True)
        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 10, education)
        pdf.ln(5)

        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, "Experience:", ln=True)
        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 10, experience)
        pdf.ln(5)

        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, "Skills:", ln=True)
        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 10, skills)

        pdf_filename = f"generated/{name}_resume.pdf"
        pdf.output(pdf_filename)

        return send_file(pdf_filename, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
