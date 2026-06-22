import tkinter as tk
from tkinter import ttk, messagebox, font
from datetime import datetime
import re

# ── Colour palette ──────────────────────────────────────────────────────────
CLR = {
    "bg":        "#F0F4F8",
    "sidebar":   "#0D3B66",
    "accent":    "#1A8FE3",
    "accent2":   "#E63946",
    "white":     "#FFFFFF",
    "card":      "#FFFFFF",
    "text":      "#1B2A3B",
    "muted":     "#6C7A8D",
    "success":   "#2DC653",
    "border":    "#CBD5E0",
    "header_bg": "#0A2D50",
    "dept_bg":   "#EBF5FB",
}

# ── Department configs ───────────────────────────────────────────────────────
DEPARTMENTS = {
    "General Medicine":   {"icon": "🩺", "color": "#1A8FE3", "symbol": "⚕"},
    "Dentistry":          {"icon": "🦷", "color": "#E63946", "symbol": "🦷"},
    "Cardiology":         {"icon": "❤️",  "color": "#E63946", "symbol": "💓"},
    "Orthopedics":        {"icon": "🦴", "color": "#8B4513", "symbol": "🦴"},
    "Pediatrics":         {"icon": "👶", "color": "#FF69B4", "symbol": "🍼"},
    "Neurology":          {"icon": "🧠", "color": "#9B59B6", "symbol": "🧠"},
    "Ophthalmology":      {"icon": "👁️",  "color": "#3498DB", "symbol": "👁"},
    "ENT":                {"icon": "👂", "color": "#27AE60", "symbol": "👂"},
    "Gynecology":         {"icon": "🌸", "color": "#E91E8C", "symbol": "♀"},
    "Radiology":          {"icon": "🔬", "color": "#607D8B", "symbol": "☢"},
    "Surgery":            {"icon": "🔪", "color": "#455A64", "symbol": "⚕"},
    "Emergency":          {"icon": "🚑", "color": "#E74C3C", "symbol": "🚨"},
}

BLOOD_GROUPS = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-", "Unknown"]
GENDERS      = ["Male", "Female", "Other", "Prefer not to say"]
MARITAL      = ["Single", "Married", "Divorced", "Widowed", "Other"]
STATES       = [
    "Maharashtra", "Karnataka", "Telangana", "Andhra Pradesh", "Tamil Nadu",
    "Gujarat", "Rajasthan", "Madhya Pradesh", "Uttar Pradesh", "Delhi",
    "West Bengal", "Kerala", "Punjab", "Haryana", "Bihar", "Other"
]

# ════════════════════════════════════════════════════════════════════════════
class HospitalForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SRT Medical College & Hospital – Patient Registration")
        self.geometry("1100x780")
        self.minsize(960, 700)
        self.configure(bg=CLR["bg"])
        self.resizable(True, True)

        # Fonts
        self.f_title  = font.Font(family="Georgia",      size=18, weight="bold")
        self.f_sub    = font.Font(family="Georgia",      size=11, slant="italic")
        self.f_head   = font.Font(family="Trebuchet MS", size=11, weight="bold")
        self.f_label  = font.Font(family="Trebuchet MS", size=9)
        self.f_entry  = font.Font(family="Trebuchet MS", size=10)
        self.f_small  = font.Font(family="Trebuchet MS", size=8)
        self.f_dept   = font.Font(family="Segoe UI Emoji", size=13)
        self.f_btn    = font.Font(family="Trebuchet MS", size=10, weight="bold")

        self.selected_dept = tk.StringVar(value="General Medicine")
        self.dept_color    = tk.StringVar(value=DEPARTMENTS["General Medicine"]["color"])

        self._build_ui()

    # ── UI Construction ──────────────────────────────────────────────────────
    def _build_ui(self):
        # ---- HEADER --------------------------------------------------------
        header = tk.Frame(self, bg=CLR["header_bg"], height=80)
        header.pack(fill="x")
        header.pack_propagate(False)

        logo_frame = tk.Frame(header, bg=CLR["header_bg"])
        logo_frame.pack(side="left", padx=20, pady=10)

        tk.Label(logo_frame, text="⚕", font=font.Font(size=34),
                 bg=CLR["header_bg"], fg="#1A8FE3").pack(side="left", padx=(0,10))

        title_frame = tk.Frame(header, bg=CLR["header_bg"])
        title_frame.pack(side="left")
        tk.Label(title_frame, text="SRT Medical College & Hospital",
                 font=self.f_title, bg=CLR["header_bg"], fg=CLR["white"]).pack(anchor="w")
        tk.Label(title_frame, text="Ambajogai, Beed District, Maharashtra – 431517  |  Est. 1961",
                 font=self.f_small, bg=CLR["header_bg"], fg="#A0C4E0").pack(anchor="w")

        right_frame = tk.Frame(header, bg=CLR["header_bg"])
        right_frame.pack(side="right", padx=20)
        now = datetime.now()
        tk.Label(right_frame, text=now.strftime("%d %b %Y"),
                 font=self.f_head, bg=CLR["header_bg"], fg=CLR["white"]).pack(anchor="e")
        tk.Label(right_frame, text=now.strftime("%I:%M %p"),
                 font=self.f_small, bg=CLR["header_bg"], fg="#A0C4E0").pack(anchor="e")
        tk.Label(right_frame, text="📋 NEW PATIENT REGISTRATION",
                 font=self.f_small, bg=CLR["header_bg"], fg="#F0C040").pack(anchor="e", pady=(4,0))

        # ---- DEPT BANNER ---------------------------------------------------
        self.dept_banner = tk.Frame(self, bg="#1A8FE3", height=38)
        self.dept_banner.pack(fill="x")
        self.dept_banner.pack_propagate(False)
        self.dept_label = tk.Label(self.dept_banner,
                                   text="🩺  Department: General Medicine  ⚕",
                                   font=self.f_head, bg="#1A8FE3", fg=CLR["white"])
        self.dept_label.pack(expand=True)

        # ---- BODY ----------------------------------------------------------
        body = tk.Frame(self, bg=CLR["bg"])
        body.pack(fill="both", expand=True, padx=16, pady=10)

        # Sidebar – department chooser
        sidebar = tk.Frame(body, bg=CLR["sidebar"], width=200)
        sidebar.pack(side="left", fill="y", padx=(0,12))
        sidebar.pack_propagate(False)

        tk.Label(sidebar, text="Select\nDepartment", font=self.f_head,
                 bg=CLR["sidebar"], fg=CLR["white"], pady=12).pack()

        tk.Frame(sidebar, bg=CLR["accent"], height=1).pack(fill="x", padx=10)

        dept_canvas = tk.Canvas(sidebar, bg=CLR["sidebar"], highlightthickness=0)
        dept_scroll = ttk.Scrollbar(sidebar, orient="vertical", command=dept_canvas.yview)
        dept_frame  = tk.Frame(dept_canvas, bg=CLR["sidebar"])

        dept_frame.bind("<Configure>",
                        lambda e: dept_canvas.configure(scrollregion=dept_canvas.bbox("all")))
        dept_canvas.create_window((0,0), window=dept_frame, anchor="nw")
        dept_canvas.configure(yscrollcommand=dept_scroll.set)
        dept_scroll.pack(side="right", fill="y")
        dept_canvas.pack(side="left", fill="both", expand=True)

        self.dept_btns = {}
        for dept, info in DEPARTMENTS.items():
            btn = tk.Button(dept_frame,
                            text=f"  {info['icon']}  {dept}",
                            font=self.f_small, anchor="w",
                            bg=CLR["sidebar"], fg=CLR["white"],
                            activebackground=info["color"],
                            activeforeground=CLR["white"],
                            relief="flat", bd=0, padx=8, pady=6,
                            cursor="hand2",
                            command=lambda d=dept: self._select_dept(d))
            btn.pack(fill="x", pady=1)
            self.dept_btns[dept] = btn

        self._select_dept("General Medicine")

        # ---- MAIN FORM AREA ------------------------------------------------
        main_area = tk.Frame(body, bg=CLR["bg"])
        main_area.pack(side="left", fill="both", expand=True)

        # Scrollable canvas
        canvas = tk.Canvas(main_area, bg=CLR["bg"], highlightthickness=0)
        scrollbar = ttk.Scrollbar(main_area, orient="vertical", command=canvas.yview)
        self.form_frame = tk.Frame(canvas, bg=CLR["bg"])

        self.form_frame.bind("<Configure>",
                             lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0,0), window=self.form_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.bind_all("<MouseWheel>",
                        lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

        # Build sections
        self.vars = {}
        self._section_personal()
        self._section_medical()
        self._section_contact()
        self._section_emergency()
        self._section_visit()
        self._section_insurance()
        self._action_buttons()

    # ── Department selection ─────────────────────────────────────────────────
    def _select_dept(self, dept):
        self.selected_dept.set(dept)
        info = DEPARTMENTS[dept]
        color = info["color"]

        for d, btn in self.dept_btns.items():
            btn.config(bg=DEPARTMENTS[d]["color"] if d == dept else CLR["sidebar"],
                       fg=CLR["white"], relief="flat")

        self.dept_banner.config(bg=color)
        self.dept_label.config(
            text=f"  {info['icon']}  Department: {dept}  {info['symbol']}",
            bg=color)

        if hasattr(self, "_dept_var"):
            self._dept_var.set(dept)

    # ── Card helper ──────────────────────────────────────────────────────────
    def _card(self, title, icon=""):
        outer = tk.Frame(self.form_frame, bg=CLR["bg"])
        outer.pack(fill="x", pady=(0,10))

        card = tk.Frame(outer, bg=CLR["card"],
                        relief="flat", bd=0,
                        highlightbackground=CLR["border"],
                        highlightthickness=1)
        card.pack(fill="x", padx=2, pady=2)

        head = tk.Frame(card, bg=CLR["accent"], height=32)
        head.pack(fill="x")
        head.pack_propagate(False)
        tk.Label(head, text=f"  {icon}  {title}",
                 font=self.f_head, bg=CLR["accent"],
                 fg=CLR["white"]).pack(side="left", padx=6)

        body = tk.Frame(card, bg=CLR["card"], padx=14, pady=10)
        body.pack(fill="x")
        return body

    # ── Row / field helpers ──────────────────────────────────────────────────
    def _row(self, parent, cols=3):
        row = tk.Frame(parent, bg=CLR["card"])
        row.pack(fill="x", pady=3)
        for i in range(cols):
            row.columnconfigure(i, weight=1)
        return row

    def _field(self, parent, col, label, key, widget="entry",
               options=None, row=None, colspan=1, required=False):
        frame = tk.Frame(parent, bg=CLR["card"])
        frame.grid(row=row or 0, column=col, columnspan=colspan,
                   sticky="nsew", padx=5, pady=2)

        lbl_txt = label + (" *" if required else "")
        tk.Label(frame, text=lbl_txt, font=self.f_label,
                 bg=CLR["card"], fg=CLR["muted"]).pack(anchor="w")

        if widget == "entry":
            var = tk.StringVar()
            e = tk.Entry(frame, textvariable=var,
                         font=self.f_entry, bg=CLR["bg"],
                         relief="flat", bd=0,
                         highlightbackground=CLR["border"],
                         highlightthickness=1,
                         highlightcolor=CLR["accent"])
            e.pack(fill="x", ipady=5)
            self.vars[key] = var

        elif widget == "combo":
            var = tk.StringVar()
            c = ttk.Combobox(frame, textvariable=var,
                             values=options or [], state="readonly",
                             font=self.f_entry)
            c.pack(fill="x")
            if options:
                c.set(options[0])
            self.vars[key] = var

        elif widget == "text":
            t = tk.Text(frame, font=self.f_entry, bg=CLR["bg"],
                        relief="flat", bd=0, height=3,
                        highlightbackground=CLR["border"],
                        highlightthickness=1,
                        highlightcolor=CLR["accent"],
                        wrap="word")
            t.pack(fill="x")
            self.vars[key] = t

        elif widget == "radio":
            var = tk.StringVar(value=options[0] if options else "")
            rframe = tk.Frame(frame, bg=CLR["card"])
            rframe.pack(anchor="w")
            for opt in (options or []):
                tk.Radiobutton(rframe, text=opt, variable=var, value=opt,
                               font=self.f_label, bg=CLR["card"],
                               activebackground=CLR["card"],
                               fg=CLR["text"]).pack(side="left", padx=4)
            self.vars[key] = var

        elif widget == "check":
            var = tk.BooleanVar()
            tk.Checkbutton(frame, text=label, variable=var,
                           font=self.f_label, bg=CLR["card"],
                           activebackground=CLR["card"],
                           fg=CLR["text"]).pack(anchor="w")
            self.vars[key] = var

        return frame

    # ── Sections ─────────────────────────────────────────────────────────────
    def _section_personal(self):
        body = self._card("Personal Information", "👤")

        r0 = self._row(body, 3)
        self._field(r0, 0, "Patient ID (Auto)", "pid", row=0)
        self.vars["pid"].set(f"SRT-{datetime.now().strftime('%Y%m%d%H%M%S')}")
        self._field(r0, 1, "Registration Date", "reg_date", row=0)
        self.vars["reg_date"].set(datetime.now().strftime("%d/%m/%Y"))
        self._field(r0, 2, "Registration Time", "reg_time", row=0)
        self.vars["reg_time"].set(datetime.now().strftime("%I:%M %p"))

        r1 = self._row(body, 3)
        self._field(r1, 0, "Title", "title", "combo",
                    ["Mr.", "Mrs.", "Ms.", "Dr.", "Prof.", "Master", "Baby"], row=0)
        self._field(r1, 1, "First Name", "fname", required=True, row=0)
        self._field(r1, 2, "Last Name", "lname", required=True, row=0)

        r2 = self._row(body, 4)
        self._field(r2, 0, "Date of Birth (DD/MM/YYYY)", "dob", required=True, row=0)
        self._field(r2, 1, "Age", "age", row=0)
        self._field(r2, 2, "Gender", "gender", "combo", GENDERS, row=0)
        self._field(r2, 3, "Marital Status", "marital", "combo", MARITAL, row=0)

        r3 = self._row(body, 4)
        self._field(r3, 0, "Blood Group", "blood_group", "combo", BLOOD_GROUPS, row=0)
        self._field(r3, 1, "Height (cm)", "height", row=0)
        self._field(r3, 2, "Weight (kg)", "weight", row=0)
        self._field(r3, 3, "BMI (auto)", "bmi", row=0)

        # Auto-BMI
        def calc_bmi(*_):
            try:
                h = float(self.vars["height"].get()) / 100
                w = float(self.vars["weight"].get())
                bmi = round(w / (h * h), 1)
                cat = ("Underweight" if bmi < 18.5 else
                       "Normal" if bmi < 25 else
                       "Overweight" if bmi < 30 else "Obese")
                self.vars["bmi"].set(f"{bmi}  ({cat})")
            except:
                self.vars["bmi"].set("")

        self.vars["height"].trace("w", calc_bmi)
        self.vars["weight"].trace("w", calc_bmi)

        r4 = self._row(body, 3)
        self._field(r4, 0, "Nationality", "nationality", "combo",
                    ["Indian", "Other"], row=0)
        self._field(r4, 1, "Religion", "religion", "combo",
                    ["Hindu", "Muslim", "Christian", "Buddhist", "Jain", "Sikh", "Other"], row=0)
        self._field(r4, 2, "Occupation", "occupation", row=0)

        r5 = self._row(body, 2)
        self._field(r5, 0, "Aadhaar Number", "aadhaar", row=0)
        self._field(r5, 1, "PAN / Passport No.", "pan", row=0)

    def _section_medical(self):
        body = self._card("Medical Information", "🏥")

        r0 = self._row(body, 2)
        self._field(r0, 0, "Department", "department", "combo",
                    list(DEPARTMENTS.keys()), row=0)
        self._dept_var = self.vars["department"]
        self._dept_var.set(self.selected_dept.get())
        self._dept_var.trace("w", lambda *_: self._select_dept(self._dept_var.get()))

        self._field(r0, 1, "Consulting Doctor", "doctor", row=0)

        r1 = self._row(body, 2)
        self._field(r1, 0, "Chief Complaint / Reason for Visit",
                    "complaint", "text", row=0, colspan=1)
        self._field(r1, 1, "Known Allergies (drugs / food / environment)",
                    "allergies", "text", row=0, colspan=1)

        r2 = self._row(body, 3)
        self._field(r2, 0, "Existing Medical Conditions", "conditions", row=0)
        self._field(r2, 1, "Current Medications", "medications", row=0)
        self._field(r2, 2, "Previous Surgeries", "surgeries", row=0)

        r3 = self._row(body, 4)
        self._field(r3, 0, "Smoking", "smoking", "combo",
                    ["No", "Yes – Current", "Yes – Former", "Occasional"], row=0)
        self._field(r3, 1, "Alcohol", "alcohol", "combo",
                    ["No", "Occasional", "Moderate", "Heavy"], row=0)
        self._field(r3, 2, "Family History", "family_history", row=0)
        self._field(r3, 3, "Admission Type", "admit_type", "combo",
                    ["OPD", "IPD", "Emergency", "Day Care", "Referral"], row=0)

    def _section_contact(self):
        body = self._card("Contact Details", "📞")

        r0 = self._row(body, 3)
        self._field(r0, 0, "Mobile Number", "mobile", required=True, row=0)
        self._field(r0, 1, "Alternate Number", "alt_mobile", row=0)
        self._field(r0, 2, "Email Address", "email", row=0)

        r1 = self._row(body, 1)
        self._field(r1, 0, "House No. / Building / Street", "address1", row=0)

        r2 = self._row(body, 4)
        self._field(r2, 0, "Village / Town", "city", row=0)
        self._field(r2, 1, "Taluka", "taluka", row=0)
        self._field(r2, 2, "District", "district", row=0)
        self._field(r2, 3, "Pincode", "pincode", row=0)

        r3 = self._row(body, 2)
        self._field(r3, 0, "State", "state", "combo", STATES, row=0)
        self._field(r3, 1, "Country", "country", "combo", ["India", "Other"], row=0)

    def _section_emergency(self):
        body = self._card("Emergency Contact", "🚨")

        r0 = self._row(body, 3)
        self._field(r0, 0, "Contact Name", "em_name", required=True, row=0)
        self._field(r0, 1, "Relationship", "em_relation", "combo",
                    ["Spouse", "Parent", "Child", "Sibling", "Friend", "Guardian", "Other"], row=0)
        self._field(r0, 2, "Mobile Number", "em_mobile", required=True, row=0)

        r1 = self._row(body, 2)
        self._field(r1, 0, "Alternate Number", "em_alt", row=0)
        self._field(r1, 1, "Address (if different)", "em_address", row=0)

    def _section_visit(self):
        body = self._card("Visit & Vitals", "📊")

        r0 = self._row(body, 4)
        self._field(r0, 0, "Temperature (°F)", "temperature", row=0)
        self._field(r0, 1, "Blood Pressure (mmHg)", "bp", row=0)
        self._field(r0, 2, "Pulse (bpm)", "pulse", row=0)
        self._field(r0, 3, "SpO₂ (%)", "spo2", row=0)

        r1 = self._row(body, 3)
        self._field(r1, 0, "Referred By", "referred_by", row=0)
        self._field(r1, 1, "Referral Hospital / Clinic", "ref_hospital", row=0)
        self._field(r1, 2, "Ward / Room No.", "ward", row=0)

    def _section_insurance(self):
        body = self._card("Insurance & Payment", "💳")

        r0 = self._row(body, 2)
        self._field(r0, 0, "Insurance Provider", "insurer", row=0)
        self._field(r0, 1, "Policy / ABHA Number", "policy_no", row=0)

        r1 = self._row(body, 3)
        self._field(r1, 0, "Scheme", "scheme", "combo",
                    ["Self / Private", "PMJAY / Ayushman Bharat",
                     "CGHS", "ESI", "State Scheme", "Other"], row=0)
        self._field(r1, 1, "Payment Mode", "payment_mode", "combo",
                    ["Cash", "UPI", "Card", "Net Banking", "Insurance", "Other"], row=0)
        self._field(r1, 2, "Token / Receipt No.", "receipt_no", row=0)

        # Consent checkboxes
        sep = tk.Frame(body, bg=CLR["border"], height=1)
        sep.pack(fill="x", pady=8)

        tk.Label(body, text="Declarations & Consent",
                 font=self.f_head, bg=CLR["card"], fg=CLR["text"]).pack(anchor="w")

        self.vars["consent_treatment"] = tk.BooleanVar()
        self.vars["consent_data"]      = tk.BooleanVar()
        self.vars["consent_photo"]     = tk.BooleanVar()

        for key, txt in [
            ("consent_treatment",
             "I consent to examination, investigation & treatment as deemed necessary by the medical team."),
            ("consent_data",
             "I agree that my medical data may be used for hospital records & research (anonymised)."),
            ("consent_photo",
             "I consent to clinical photography / video for medical documentation purposes."),
        ]:
            tk.Checkbutton(body, text=txt, variable=self.vars[key],
                           font=self.f_label, bg=CLR["card"],
                           activebackground=CLR["card"],
                           fg=CLR["text"], wraplength=700,
                           justify="left").pack(anchor="w", pady=1)

    # ── Action buttons ────────────────────────────────────────────────────────
    def _action_buttons(self):
        bar = tk.Frame(self.form_frame, bg=CLR["bg"], pady=14)
        bar.pack(fill="x")

        def btn(parent, text, cmd, bg, fg=CLR["white"]):
            b = tk.Button(parent, text=text, command=cmd,
                          font=self.f_btn, bg=bg, fg=fg,
                          activebackground=bg, activeforeground=fg,
                          relief="flat", bd=0, padx=20, pady=10,
                          cursor="hand2")
            b.pack(side="left", padx=6)
            return b

        btn(bar, "✔  Register Patient", self._submit,  CLR["success"])
        btn(bar, "🖨  Print Form",       self._print,   CLR["accent"])
        btn(bar, "⟳  Clear Form",       self._clear,   CLR["muted"])

    # ── Actions ──────────────────────────────────────────────────────────────
    def _get_text(self, key):
        v = self.vars.get(key)
        if v is None:
            return ""
        if isinstance(v, tk.Text):
            return v.get("1.0", "end").strip()
        return v.get().strip()

    def _validate(self):
        errors = []
        if not self._get_text("fname"):
            errors.append("First Name is required.")
        if not self._get_text("lname"):
            errors.append("Last Name is required.")
        if not self._get_text("dob"):
            errors.append("Date of Birth is required.")
        mob = self._get_text("mobile")
        if not mob:
            errors.append("Mobile Number is required.")
        elif not re.fullmatch(r"[6-9]\d{9}", mob):
            errors.append("Mobile Number must be a valid 10-digit Indian number.")
        if not self._get_text("em_name"):
            errors.append("Emergency Contact Name is required.")
        if not self._get_text("em_mobile"):
            errors.append("Emergency Contact Mobile is required.")
        if not self.vars["consent_treatment"].get():
            errors.append("Patient must consent to treatment.")
        return errors

    def _submit(self):
        errors = self._validate()
        if errors:
            messagebox.showerror("Validation Error",
                                 "Please fix the following:\n\n• " + "\n• ".join(errors))
            return

        name = f"{self._get_text('title')} {self._get_text('fname')} {self._get_text('lname')}"
        pid  = self._get_text("pid")
        dept = self._get_text("department")
        info = DEPARTMENTS.get(dept, {})
        messagebox.showinfo(
            "✅ Registration Successful",
            f"Patient Registered Successfully!\n\n"
            f"  Name       : {name}\n"
            f"  Patient ID : {pid}\n"
            f"  Department : {info.get('icon','')} {dept}\n"
            f"  Date       : {self._get_text('reg_date')}\n\n"
            f"Please proceed to the {dept} counter.\n"
            f"Doctor: {self._get_text('doctor') or 'To be assigned'}"
        )

    def _print(self):
        messagebox.showinfo("Print",
                            "Sending form to printer…\n(Connect to a printing module for production use.)")

    def _clear(self):
        if not messagebox.askyesno("Clear Form", "Clear all fields and start fresh?"):
            return
        for key, var in self.vars.items():
            if isinstance(var, tk.Text):
                var.delete("1.0", "end")
            elif isinstance(var, tk.BooleanVar):
                var.set(False)
            else:
                var.set("")
        self.vars["pid"].set(f"SRT-{datetime.now().strftime('%Y%m%d%H%M%S')}")
        self.vars["reg_date"].set(datetime.now().strftime("%d/%m/%Y"))
        self.vars["reg_time"].set(datetime.now().strftime("%I:%M %p"))
        self.vars["department"].set("General Medicine")
        self._select_dept("General Medicine")


# ════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    app = HospitalForm()
    app.mainloop()
