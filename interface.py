# ==================== PRESENTATION TEMPLATE: PART 1 ====================

PART_A1 = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Campus Meal | ALU Portal</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', system-ui, sans-serif; }
        body { background-color: #f1f5f9; min-height: 100vh; display: flex; flex-direction: column; align-items: center; }
        header { background: linear-gradient(135deg, #800020 0%, #4A0E17 100%); width: 100%; padding: 1.25rem 2rem; color: #ffffff; font-weight: 900; box-shadow: 0 4px 12px rgba(0,0,0,0.1); display: flex; align-items: center; gap: 0.75rem; }
        main { flex: 1; width: 100%; display: flex; flex-direction: column; align-items: center; padding: 2rem 1rem; }
        .welcome-card { background: #ffffff; border-radius: 1rem; border: 1px solid #e2e8f0; width: 100%; max-width: 450px; padding: 2rem; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05); text-align: center; }
        .welcome-action-btn { background: #f8fafc; border: 1px solid #cbd5e1; color: #64748b; padding: 0.75rem 1.5rem; font-size: 0.85rem; font-weight: 800; border-radius: 0.5rem; cursor: pointer; transition: all 0.2s; text-transform: uppercase; letter-spacing: 0.05em; width: 48%; }
        .welcome-action-btn.active-tab { background: #800020; border-color: #800020; color: #ffffff; box-shadow: 0 4px 6px -1px rgba(128,0,32,0.2); }
        .input-field { width: 100%; padding: 0.75rem 1rem; background-color: #f8fafc; border: 1px solid #cbd5e1; border-radius: 0.75rem; outline: none; font-size: 0.9rem; font-weight: 600; color: #0f172a; transition: border-color 0.2s; margin-top: 0.35rem; }
        .input-field:focus { border-color: #800020; background-color: #ffffff; }
        @keyframes pulseAlert { 0% { opacity: 1; } 50% { opacity: 0.85; background: #dc2626; } 100% { opacity: 1; } }
        .urgent-countdown-blink { animation: pulseAlert 1.5s infinite ease-in-out; }
    </style>
</head>
<body>
    <header>
        <span style="font-size: 1.5rem;">🍲</span>
        <h2 style="font-size: 1.15rem; letter-spacing: 0.05em; text-transform: uppercase;">Campus Meal</h2>
    </header>
    <main>
        <!-- 🔒 AUTHENTICATION ACCESS INTERFACE CONTROL CONTAINER -->
        <div id="screen-auth" class="welcome-card">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">👋</div>
            <h3 style="font-size: 1.25rem; font-weight: 900; color: #0f172a;">Welcome to ALU Dining</h3>
            <p style="font-size: 0.75rem; color: #64748b; margin-top: 0.15rem; margin-bottom: 1.5rem;">Secure Student & Vendor Gateway Hub</p>
            
            <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem;">
                <button type="button" id="btn-welcome-signin" onclick="activateFormMode('signin')" class="welcome-action-btn">Sign In</button>
                <button type="button" id="btn-welcome-signup" onclick="activateFormMode('signup')" class="welcome-action-btn">Sign Up</button>
            </div>
            
            <div id="fieldsWrapper" style="display: none; text-align: left;">
                <div id="container-name" style="margin-bottom: 1rem; display: none;">
                    <label style="font-size: 0.65rem; font-weight: 800; color: #64748b; text-transform: uppercase; letter-spacing: 0.05em;">Full Identity Name</label>
                    <input id="authName" type="text" placeholder="e.g., Jane Doe" class="input-field">
                </div>
                <div style="margin-bottom: 1rem;">
                    <label style="font-size: 0.65rem; font-weight: 800; color: #64748b; text-transform: uppercase; letter-spacing: 0.05em;">Email Address Profile</label>
                    <input id="authEmail" type="email" placeholder="username@alustudent.com" class="input-field">
                </div>
                <div style="margin-bottom: 1.25rem;">
                    <label style="font-size: 0.65rem; font-weight: 800; color: #64748b; text-transform: uppercase; letter-spacing: 0.05em;">Secure Password Credentials</label>
                    <input id="authPassword" type="password" placeholder="••••••••" class="input-field">
                </div>
                <div id="container-confirm" style="margin-bottom: 1.25rem; display: none;">
                    <label style="font-size: 0.65rem; font-weight: 800; color: #64748b; text-transform: uppercase; letter-spacing: 0.05em;">Confirm Password Match</label>
                    <input id="authConfirmPassword" type="password" placeholder="••••••••" class="input-field">
                </div>
                
                <div id="signup-extra-row" style="display: none; grid-template-columns: 1fr 1fr; gap: 0.75rem; margin-bottom: 1.5rem;">
                    <div>
                        <label style="font-size: 0.65rem; font-weight: 800; color: #64748b; text-transform: uppercase; letter-spacing: 0.05em;">Profile Access Role</label>
                        <select id="authRole" onchange="handleRoleSelectionChange()" class="input-field" style="padding: 0.7rem 0.5rem; font-size: 0.8rem; font-weight: bold;">
                            <option value="student" selected>🧑‍🎓 Student</option>
                            <option value="provider_a">🏪 Provider A Counter</option>
                            <option value="provider_b">🏪 Provider B Counter</option>
                            <option value="admin">🏛️ School Official</option>
                        </select>
                    </div>
                    <div id="container-hostel">
                        <label style="font-size: 0.65rem; font-weight: 800; color: #64748b; text-transform: uppercase; letter-spacing: 0.05em;">Hostel Residence</label>
                        <select id="authResidence" class="input-field" style="padding: 0.7rem 0.5rem; font-size: 0.8rem; font-weight: bold;">
                            <option value="Infinity Hostel" selected>Infinity Hostel</option>
                            <option value="Soual Hostel">Soual Hostel</option>
                        </select>
                    </div>
                </div>
                
                <button type="button" onclick="submitAuthForm()" id="authSubmitBtn" style="width: 100%; background: linear-gradient(135deg, #800020 0%, #4A0E17 100%); color: #ffffff; font-weight: 800; font-size: 0.85rem; padding: 1rem; border: none; border-radius: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; cursor: pointer; box-shadow: 0 4px 6px -1px rgba(128,0,32,0.2);">Proceed</button>
            </div>
        </div>"""
# ==================== PRESENTATION TEMPLATE: PART 2 ====================

PART_A2 = """        <!-- 🧑‍🎓 STUDENT COMPONENT DASHBOARD GRID WORKSPACE CONTAINER -->
        <div id="dash-student" style="display: none; width: 100%; max-width: 900px; margin-top: 1rem;">
            <div id="studentNotificationBanner" style="display: none; background: linear-gradient(135deg, #b91c1c 0%, #7f1d1d 100%); color: #ffffff; padding: 1rem; border-radius: 0.75rem; font-weight: 800; font-size: 0.85rem; text-align: center; margin-bottom: 1.5rem; border-left: 5px solid #f59e0b; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); letter-spacing: 0.025em; text-transform: uppercase;">
                <span style="margin-right: 0.5rem;">🔔</span> <span id="notificationMessageText">Notice Placeholder</span>
            </div>
            <div style="display: grid; grid-template-columns: 1fr; gap: 1.5rem; width: 100%;">
                <div style="background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 1rem; padding: 1.5rem; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
                    <div style="border-bottom: 1px solid #e2e8f0; padding-bottom: 0.75rem; margin-bottom: 1rem;">
                        <h3 style="font-size: 1rem; font-weight: 800; color: #1e293b;">📅 Weekly Campus Lunch Planner</h3>
                        <p style="font-size: 0.75rem; color: #64748b; margin-top: 0.15rem;">Select dates for campus dining allocation logs</p>
                    </div>
                    <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 0.5rem; margin: 1rem 0; text-align: center;">
                        <label style="border: 1px solid #e2e8f0; padding: 0.75rem 0.25rem; border-radius: 0.75rem; background-color: #f8fafc; display: block; cursor: pointer; font-size: 0.75rem; font-weight: bold;"><input type="checkbox" id="mon" style="display: block; margin: 0 auto 0.5rem auto; accent-color: #800020;">Mon</label>
                        <label style="border: 1px solid #e2e8f0; padding: 0.75rem 0.25rem; border-radius: 0.75rem; background-color: #f8fafc; display: block; cursor: pointer; font-size: 0.75rem; font-weight: bold;"><input type="checkbox" id="tue" style="display: block; margin: 0 auto 0.5rem auto; accent-color: #800020;">Tue</label>
                        <label style="border: 1px solid #e2e8f0; padding: 0.75rem 0.25rem; border-radius: 0.75rem; background-color: #f8fafc; display: block; cursor: pointer; font-size: 0.75rem; font-weight: bold;"><input type="checkbox" id="wed" style="display: block; margin: 0 auto 0.5rem auto; accent-color: #800020;">Wed</label>
                        <label style="border: 1px solid #e2e8f0; padding: 0.75rem 0.25rem; border-radius: 0.75rem; background-color: #f8fafc; display: block; cursor: pointer; font-size: 0.75rem; font-weight: bold;"><input type="checkbox" id="thu" style="display: block; margin: 0 auto 0.5rem auto; accent-color: #800020;">Thu</label>
                        <label style="border: 1px solid #e2e8f0; padding: 0.75rem 0.25rem; border-radius: 0.75rem; background-color: #f8fafc; display: block; cursor: pointer; font-size: 0.75rem; font-weight: bold;"><input type="checkbox" id="fri" style="display: block; margin: 0 auto 0.5rem auto; accent-color: #800020;">Fri</label>
                    </div>
                    <button type="button" onclick="studentLockSchedule()" style="width: 100%; background: #0f172a; color: #ffffff; font-weight: 800; font-size: 0.85rem; padding: 0.875rem; border: none; border-radius: 0.75rem; text-transform: uppercase; cursor: pointer; margin-top: 1rem;">Sync Weekly Plan</button>
                </div>
                <div style="background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 1rem; padding: 1.5rem; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
                    <h3 style="font-size: 1rem; font-weight: 800; color: #1e293b; margin-bottom: 0.25rem;">🍲 Collect Daily Campus Lunch</h3>
                    <p style="font-size: 0.75rem; color: #64748b; margin-bottom: 1rem;">Request your daily checkout ticket reference code.</p>
                    <select id="foodItem" class="input-field" style="margin-bottom: 1rem; padding: 0.75rem 1rem;">
                        <option value="" disabled selected>Select menu preference item choice...</option>
                        <option value="PROV_A-101">Provider A: Beef Burger Combo (3,500 Frw)</option>
                        <option value="PROV_A-104">Provider A: Buffet Beef Combo (3,500 Frw)</option>
                        <option value="PROV_A-105">Provider A: Chicken Wrap Combo (3,500 Frw)</option>
                        <option value="PROV_B-201">Provider B: Standard Campus Rice Meal (3,000 Frw)</option>
                    </select>
                    <button type="button" onclick="studentGenerateToken()" style="width: 100%; background: linear-gradient(135deg, #800020 0%, #4A0E17 100%); color: #ffffff; font-weight: 800; font-size: 0.85rem; padding: 0.875rem; border: none; border-radius: 0.75rem; text-transform: uppercase; cursor: pointer;">Request Ticket ID</button>
                    <div id="studentTokenBox" style="background-color: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 0.75rem; padding: 1rem; text-align: center; margin-top: 1rem; display: none;">
                        <div style="font-size: 0.65rem; font-weight: bold; color: #047857; text-transform: uppercase;">Authorized Verification Token</div>
                        <div id="displayToken" style="font-size: 2.25rem; font-weight: 900; color: #065f46; letter-spacing: 0.1em; margin-top: 0.25rem;">00000</div>
                    </div>
                </div>
            </div>
        </div>"""
# ==================== PRESENTATION TEMPLATE: PART 3 ====================

PART_A3 = """        <!-- 🏪 DYNAMIC MEAL PROVIDER DESK VERIFICATION INTERFACE CONTAINER -->
        <div id="dash-provider" style="display: none; width: 100%; max-width: 500px; margin-top: 1rem;">
            <div style="background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 1rem; padding: 2rem; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05); text-align: center;">
                <div style="border-bottom: 2px solid #f1f5f9; padding-bottom: 1rem; margin-bottom: 1.5rem;">
                    <span style="font-size: 2.5rem;">🏪</span>
                    <h3 style="font-size: 1.25rem; font-weight: 900; color: #0f172a; margin-top: 0.5rem;">Meal Provider Terminal</h3>
                    <p style="font-size: 0.75rem; color: #64748b; margin-top: 0.15rem;">ALU Campus Cashier Counter Desk</p>
                </div>
                <div style="margin-bottom: 1.5rem; text-align: left;">
                    <label style="display: block; font-size: 0.65rem; font-weight: 800; color: #64748b; text-transform: uppercase; margin-bottom: 0.5rem;">Enter Student Verification Token ID</label>
                    <input id="providerTokenInput" type="text" placeholder="e.g., 52369" class="input-field" style="font-size: 1.5rem; font-weight: 900; letter-spacing: 0.1em; text-align: center; color: #800020; padding: 0.75rem;">
                </div>
                <button type="button" onclick="providerLookupStudentVoucher()" id="btn-lookup-voucher" style="width: 100%; background: #0f172a; color: #ffffff; font-weight: 800; font-size: 0.85rem; padding: 1rem; border: none; border-radius: 0.75rem; text-transform: uppercase; cursor: pointer; margin-bottom: 1rem;">Check Ticket ID</button>
                <div id="providerOrderReviewBox" style="background-color: #f8fafc; border: 2px dashed #cbd5e1; border-radius: 0.75rem; padding: 1.25rem; text-align: left; display: none; margin-top: 1rem;">
                    <div style="font-size: 0.65rem; font-weight: 800; color: #64748b; text-transform: uppercase; margin-bottom: 0.25rem;">Student Identity Reference</div>
                    <div id="reviewStudentId" style="font-size: 0.85rem; font-weight: 800; color: #1e293b; margin-bottom: 1rem;">student@alustudent.com</div>
                    <div style="font-size: 0.65rem; font-weight: 800; color: #64748b; text-transform: uppercase; margin-bottom: 0.25rem;">Selected Menu Preference Item</div>
                    <div id="reviewFoodDetails" style="font-size: 0.95rem; font-weight: 900; color: #800020; margin-bottom: 1.25rem; background-color: #fff1f2; padding: 0.5rem 0.75rem; border-radius: 0.5rem; border: 1px solid #fecdd3;">Food Package Details</div>
                    <button type="button" onclick="providerConfirmServed()" style="width: 100%; background: linear-gradient(135deg, #16a34a 0%, #15803d 100%); color: #ffffff; font-weight: 900; font-size: 0.9rem; padding: 0.875rem; border: none; border-radius: 0.65rem; text-transform: uppercase; cursor: pointer;">✔️ Served & Release Funds</button>
                </div>
            </div>
        </div>
        
        <!-- 🏛️ SCHOOL OFFICIAL ADMINISTRATIVE CONTROLS -->
        <div id="dash-admin" style="display: none; width: 100%; max-width: 950px; margin-top: 1rem;">
            <div style="background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 1rem; padding: 1.5rem; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); margin-bottom: 1.5rem;">
                <div style="border-bottom: 2px solid #f1f5f9; padding-bottom: 0.75rem; margin-bottom: 1.25rem; display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <h3 style="font-size: 1.15rem; font-weight: 900; color: #0f172a;">📊 Multi-Vendor Financial Settlement & Ledgers</h3>
                        <p style="font-size: 0.725rem; color: #64748b; margin-top: 0.15rem;">Live tracking calculated at standard unit baseline of 3,500 Frw per serving package</p>
                    </div>
                    <button type="button" onclick="loadAdminStats()" style="background: #800020; color: #ffffff; font-weight: 800; font-size: 0.725rem; padding: 0.5rem 1rem; border: none; border-radius: 0.5rem; cursor: pointer; text-transform: uppercase;">Refresh Balances</button>
                </div>
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; text-align: center;">
                    <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 0.75rem; padding: 1rem; display: flex; flex-direction: column; justify-content: center;">
                        <div style="font-size: 0.65rem; font-weight: 800; color: #64748b; text-transform: uppercase;">Total Active Profiles</div>
                        <div id="adminTotalSyncs" style="font-size: 2rem; font-weight: 900; color: #0f172a; margin-top: 0.25rem;">0</div>
                    </div>
                    <div style="background-color: #fff1f2; border: 1px solid #fecdd3; border-radius: 0.75rem; padding: 1rem; text-align: left;">
                        <div style="font-size: 0.7rem; font-weight: 900; color: #9f1239; text-transform: uppercase; border-bottom: 1px solid #fecdd3; padding-bottom: 0.25rem;">🏪 MEAL PROVIDER A</div>
                        <div style="font-size: 0.75rem; font-weight: bold; color: #4c0519; margin-top: 0.5rem;">Today's Cash: <b id="cashADay" style="color: #b91c1c; float: right;">0 Frw</b></div>
                        <div style="font-size: 0.75rem; font-weight: bold; color: #4c0519; margin-top: 0.25rem;">Weekly Total: <b id="cashAWeek" style="color: #b91c1c; float: right;">0 Frw</b></div>
                    </div>
                    <div style="background-color: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 0.75rem; padding: 1rem; text-align: left;">
                        <div style="font-size: 0.7rem; font-weight: 900; color: #166534; text-transform: uppercase; border-bottom: 1px solid #bbf7d0; padding-bottom: 0.25rem;">🏪 MEAL PROVIDER B</div>
                        <div style="font-size: 0.75rem; font-weight: bold; color: #052e16; margin-top: 0.5rem;">Today's Cash: <b id="cashBDay" style="color: #15803d; float: right;">0 Frw</b></div>
                        <div style="font-size: 0.75rem; font-weight: bold; color: #052e16; margin-top: 0.25rem;">Weekly Total: <b id="cashBWeek" style="color: #15803d; float: right;">0 Frw</b></div>
                    </div>
                </div>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">
                <div style="background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 1rem; padding: 1.5rem; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
                    <h4 style="font-size: 0.9rem; font-weight: 800; color: #1e293b; margin-bottom: 0.25rem;">📁 Simple Bulk Upload Student Roster</h4>
                    <p style="font-size: 0.725rem; color: #64748b; margin-bottom: 1rem;">Select a valid file containing column arrays: <b>name, email</b></p>
                    <div style="border: 2px dashed #cbd5e1; padding: 1.25rem; border-radius: 0.75rem; text-align: center; background-color: #f8fafc; margin-bottom: 1rem;">
                        <input type="file" id="adminCsvFileInput" accept=".csv" style="font-size: 0.8rem; cursor: pointer;">
                    </div>
                    <button type="button" onclick="adminProcessBulkCsvUpload()" style="width: 100%; background: #0f172a; color: #ffffff; font-weight: 800; font-size: 0.85rem; padding: 0.875rem; border: none; border-radius: 0.75rem; text-transform: uppercase; cursor: pointer;">Provision Student Accounts</button>
                </div>
                <div style="background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 1rem; padding: 1.5rem; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <h4 style="font-size: 0.9rem; font-weight: 800; color: #1e293b; margin-bottom: 0.25rem;">📦 Export Residential Logistics Files</h4>
                        <p style="font-size: 0.725rem; color: #64748b; margin-bottom: 1rem;">Download synced layouts showing explicitly <b>CAMPUS</b> or <b>HOSTEL</b> slots for wardens.</p>
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 0.5rem;">
                        <button onclick="triggerHostelRosterDownload('Infinity Hostel')" style="width: 100%; text-align: center; background: linear-gradient(135deg, #475569 0%, #1e293b 100%); color: #ffffff; font-weight: 800; font-size: 0.8rem; padding: 0.75rem; border-radius: 0.5rem; border: none; cursor: pointer; text-transform: uppercase;">📥 Download Infinity Hostel Sheet</button>
                        <button onclick="triggerHostelRosterDownload('Soual Hostel')" style="width: 100%; text-align: center; background: linear-gradient(135deg, #475569 0%, #1e293b 100%); color: #ffffff; font-weight: 800; font-size: 0.8rem; padding: 0.75rem; border-radius: 0.5rem; border: none; cursor: pointer; text-transform: uppercase;">📥 Download Soual Hostel Sheet</button>
                    </div>
                </div>
            </div>
        </div>"""
# ==================== PRESENTATION TEMPLATE: PART 3 ====================

PART_A3 = """        <!-- 🏪 DYNAMIC MEAL PROVIDER DESK VERIFICATION INTERFACE CONTAINER -->
        <div id="dash-provider" style="display: none; width: 100%; max-width: 500px; margin-top: 1rem;">
            <div style="background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 1rem; padding: 2rem; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05); text-align: center;">
                <div style="border-bottom: 2px solid #f1f5f9; padding-bottom: 1rem; margin-bottom: 1.5rem;">
                    <span style="font-size: 2.5rem;">🏪</span>
                    <h3 style="font-size: 1.25rem; font-weight: 900; color: #0f172a; margin-top: 0.5rem;">Meal Provider Terminal</h3>
                    <p style="font-size: 0.75rem; color: #64748b; margin-top: 0.15rem;">ALU Campus Cashier Counter Desk</p>
                </div>
                <div style="margin-bottom: 1.5rem; text-align: left;">
                    <label style="display: block; font-size: 0.65rem; font-weight: 800; color: #64748b; text-transform: uppercase; margin-bottom: 0.5rem;">Enter Student Verification Token ID</label>
                    <input id="providerTokenInput" type="text" placeholder="e.g., 52369" class="input-field" style="font-size: 1.5rem; font-weight: 900; letter-spacing: 0.1em; text-align: center; color: #800020; padding: 0.75rem;">
                </div>
                <button type="button" onclick="providerLookupStudentVoucher()" id="btn-lookup-voucher" style="width: 100%; background: #0f172a; color: #ffffff; font-weight: 800; font-size: 0.85rem; padding: 1rem; border: none; border-radius: 0.75rem; text-transform: uppercase; cursor: pointer; margin-bottom: 1rem;">Check Ticket ID</button>
                <div id="providerOrderReviewBox" style="background-color: #f8fafc; border: 2px dashed #cbd5e1; border-radius: 0.75rem; padding: 1.25rem; text-align: left; display: none; margin-top: 1rem;">
                    <div style="font-size: 0.65rem; font-weight: 800; color: #64748b; text-transform: uppercase; margin-bottom: 0.25rem;">Student Identity Reference</div>
                    <div id="reviewStudentId" style="font-size: 0.85rem; font-weight: 800; color: #1e293b; margin-bottom: 1rem;">student@alustudent.com</div>
                    <div style="font-size: 0.65rem; font-weight: 800; color: #64748b; text-transform: uppercase; margin-bottom: 0.25rem;">Selected Menu Preference Item</div>
                    <div id="reviewFoodDetails" style="font-size: 0.95rem; font-weight: 900; color: #800020; margin-bottom: 1.25rem; background-color: #fff1f2; padding: 0.5rem 0.75rem; border-radius: 0.5rem; border: 1px solid #fecdd3;">Food Package Details</div>
                    <button type="button" onclick="providerConfirmServed()" style="width: 100%; background: linear-gradient(135deg, #16a34a 0%, #15803d 100%); color: #ffffff; font-weight: 900; font-size: 0.9rem; padding: 0.875rem; border: none; border-radius: 0.65rem; text-transform: uppercase; cursor: pointer;">✔️ Served & Release Funds</button>
                </div>
            </div>
        </div>
        
        <!-- 🏛️ SCHOOL OFFICIAL ADMINISTRATIVE CONTROLS -->
        <div id="dash-admin" style="display: none; width: 100%; max-width: 950px; margin-top: 1rem;">
            <div style="background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 1rem; padding: 1.5rem; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); margin-bottom: 1.5rem;">
                <div style="border-bottom: 2px solid #f1f5f9; padding-bottom: 0.75rem; margin-bottom: 1.25rem; display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <h3 style="font-size: 1.15rem; font-weight: 900; color: #0f172a;">📊 Multi-Vendor Financial Settlement & Ledgers</h3>
                        <p style="font-size: 0.725rem; color: #64748b; margin-top: 0.15rem;">Live tracking calculated at standard unit baseline of 3,500 Frw per serving package</p>
                    </div>
                    <button type="button" onclick="loadAdminStats()" style="background: #800020; color: #ffffff; font-weight: 800; font-size: 0.725rem; padding: 0.5rem 1rem; border: none; border-radius: 0.5rem; cursor: pointer; text-transform: uppercase;">Refresh Balances</button>
                </div>
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; text-align: center;">
                    <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 0.75rem; padding: 1rem; display: flex; flex-direction: column; justify-content: center;">
                        <div style="font-size: 0.65rem; font-weight: 800; color: #64748b; text-transform: uppercase;">Total Active Profiles</div>
                        <div id="adminTotalSyncs" style="font-size: 2rem; font-weight: 900; color: #0f172a; margin-top: 0.25rem;">0</div>
                    </div>
                    <div style="background-color: #fff1f2; border: 1px solid #fecdd3; border-radius: 0.75rem; padding: 1rem; text-align: left;">
                        <div style="font-size: 0.7rem; font-weight: 900; color: #9f1239; text-transform: uppercase; border-bottom: 1px solid #fecdd3; padding-bottom: 0.25rem;">🏪 MEAL PROVIDER A</div>
                        <div style="font-size: 0.75rem; font-weight: bold; color: #4c0519; margin-top: 0.5rem;">Today's Cash: <b id="cashADay" style="color: #b91c1c; float: right;">0 Frw</b></div>
                        <div style="font-size: 0.75rem; font-weight: bold; color: #4c0519; margin-top: 0.25rem;">Weekly Total: <b id="cashAWeek" style="color: #b91c1c; float: right;">0 Frw</b></div>
                    </div>
                    <div style="background-color: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 0.75rem; padding: 1rem; text-align: left;">
                        <div style="font-size: 0.7rem; font-weight: 900; color: #166534; text-transform: uppercase; border-bottom: 1px solid #bbf7d0; padding-bottom: 0.25rem;">🏪 MEAL PROVIDER B</div>
                        <div style="font-size: 0.75rem; font-weight: bold; color: #052e16; margin-top: 0.5rem;">Today's Cash: <b id="cashBDay" style="color: #15803d; float: right;">0 Frw</b></div>
                        <div style="font-size: 0.75rem; font-weight: bold; color: #052e16; margin-top: 0.25rem;">Weekly Total: <b id="cashBWeek" style="color: #15803d; float: right;">0 Frw</b></div>
                    </div>
                </div>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">
                <div style="background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 1rem; padding: 1.5rem; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
                    <h4 style="font-size: 0.9rem; font-weight: 800; color: #1e293b; margin-bottom: 0.25rem;">📁 Simple Bulk Upload Student Roster</h4>
                    <p style="font-size: 0.725rem; color: #64748b; margin-bottom: 1rem;">Select a valid file containing column arrays: <b>name, email</b></p>
                    <div style="border: 2px dashed #cbd5e1; padding: 1.25rem; border-radius: 0.75rem; text-align: center; background-color: #f8fafc; margin-bottom: 1rem;">
                        <input type="file" id="adminCsvFileInput" accept=".csv" style="font-size: 0.8rem; cursor: pointer;">
                    </div>
                    <button type="button" onclick="adminProcessBulkCsvUpload()" style="width: 100%; background: #0f172a; color: #ffffff; font-weight: 800; font-size: 0.85rem; padding: 0.875rem; border: none; border-radius: 0.75rem; text-transform: uppercase; cursor: pointer;">Provision Student Accounts</button>
                </div>
                <div style="background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 1rem; padding: 1.5rem; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <h4 style="font-size: 0.9rem; font-weight: 800; color: #1e293b; margin-bottom: 0.25rem;">📦 Export Residential Logistics Files</h4>
                        <p style="font-size: 0.725rem; color: #64748b; margin-bottom: 1rem;">Download synced layouts showing explicitly <b>CAMPUS</b> or <b>HOSTEL</b> slots for wardens.</p>
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 0.5rem;">
                        <button onclick="triggerHostelRosterDownload('Infinity Hostel')" style="width: 100%; text-align: center; background: linear-gradient(135deg, #475569 0%, #1e293b 100%); color: #ffffff; font-weight: 800; font-size: 0.8rem; padding: 0.75rem; border-radius: 0.5rem; border: none; cursor: pointer; text-transform: uppercase;">📥 Download Infinity Hostel Sheet</button>
                        <button onclick="triggerHostelRosterDownload('Soual Hostel')" style="width: 100%; text-align: center; background: linear-gradient(135deg, #475569 0%, #1e293b 100%); color: #ffffff; font-weight: 800; font-size: 0.8rem; padding: 0.75rem; border-radius: 0.5rem; border: none; cursor: pointer; text-transform: uppercase;">📥 Download Soual Hostel Sheet</button>
                    </div>
                </div>
            </div>
        </div>"""
# ==================== PRESENTATION TEMPLATE: PART 4 ====================

PART_B1 = """<script>
        let activeAuthMode = null;
        let sessionUser = null;

        function activateFormMode(mode) {
            activeAuthMode = mode;
            document.getElementById('fieldsWrapper').style.display = 'block';
            document.getElementById('btn-welcome-signin').className = mode === 'signin' ? 'welcome-action-btn active-tab' : 'welcome-action-btn';
            document.getElementById('btn-welcome-signup').className = mode === 'signup' ? 'welcome-action-btn active-tab' : 'welcome-action-btn';
            document.getElementById('container-name').style.display = mode === 'signup' ? 'block' : 'none';
            document.getElementById('signup-extra-row').style.display = mode === 'signup' ? 'grid' : 'none';
            document.getElementById('container-confirm').style.display = mode === 'signup' ? 'block' : 'none';
            document.getElementById('authSubmitBtn').innerText = mode === 'signup' ? 'Create Account & Sign Up' : 'Secure Login & Sign In';
        }

        function handleRoleSelectionChange() {
            const role = document.getElementById('authRole').value;
            const isStudent = role === 'student';
            document.getElementById('container-hostel').style.opacity = isStudent ? '1' : '0.3';
            document.getElementById('authResidence').disabled = !isStudent;
        }

        async function checkInAppNotificationAlerts(studentEmail) {
            try {
                const r = await fetch(`${window.location.origin}/student/check-notification?email=${encodeURIComponent(studentEmail)}`);
                const d = await r.json();
                const banner = document.getElementById('studentNotificationBanner');
                if (r.ok && d.show_banner) {
                    document.getElementById('notificationMessageText').innerText = d.message;
                    banner.style.display = 'block';
                } else {
                    banner.style.display = 'none';
                }
            } catch (e) { console.log("Notification check failed"); }
        }

        async function submitAuthForm() {
            const email = document.getElementById('authEmail').value.trim();
            const pass = document.getElementById('authPassword').value;
            if (!email || !pass) return alert("Please enter your credentials.");
            
            if (activeAuthMode === 'signup') {
                const name = document.getElementById('authName').value.trim();
                const confirm = document.getElementById('authConfirmPassword').value;
                const role = document.getElementById('authRole').value;
                const residence = document.getElementById('authResidence').value;
                if (!name) return alert("Please fill in your full name.");
                if (pass !== confirm) return alert("Passwords do not match.");
                
                const r = await fetch(`${window.location.origin}/auth/signup`, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ name: name, email: email, password: pass, role: role, residence: residence })
                });
                const d = await r.json();
                if (r.ok) {
                    alert("🎉 Account registered successfully into Supabase rows!");
                    activateFormMode('signin');
                } else alert("❌ Registration Error: " + d.detail);
            } else {
                const r = await fetch(`${window.location.origin}/auth/signin`, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ email: email, password: pass })
                });
                const d = await r.json();
                if (r.ok) {
                    sessionUser = d;
                    alert("🎉 Login Approved! Mounting Workspace Dashboard.");
                    document.getElementById('screen-auth').style.display = 'none';
                    if (d.role === 'student') {
                        document.getElementById('dash-student').style.display = 'block';
                        checkInAppNotificationAlerts(d.email);
                    } else if (d.role === 'provider_a' || d.role === 'provider_b') {
                        document.getElementById('dash-provider').style.display = 'block';
                    } else if (d.role === 'admin') {
                        document.getElementById('dash-admin').style.display = 'block';
                        loadAdminStats();
                    }
                } else alert("❌ Access Denied: " + d.detail);
            }
        }

        async function studentLockSchedule() {
            if (!sessionUser) return alert("Session profile timeout. Please log in again.");
            const monVal = document.getElementById('mon').checked;
            const tueVal = document.getElementById('tue').checked;
            const wedVal = document.getElementById('wed').checked;
            const thuVal = document.getElementById('thu').checked;
            const friVal = document.getElementById('fri').checked;
            
            const r = await fetch(`${window.location.origin}/student/submit-schedule`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    student_name: sessionUser.name,
                    student_email: sessionUser.email,
                    residence_name: sessionUser.residence,
                    monday: monVal,
                    tuesday: tueVal,
                    wednesday: wedVal,
                    thursday: thuVal,
                    friday: friVal
                })
            });
            if (r.ok) alert("🎉 Schedule synchronized successfully down into your Supabase columns!");
            else alert("❌ Synch Lockout.");
        }

        async function studentGenerateToken() {
            if (!sessionUser) return alert("Session timeout.");
            const fv = document.getElementById('foodItem').value;
            if (!fv) return alert("Please select a menu preference option.");
            const randomToken = String(Math.floor(10000 + Math.random() * 90000));
            const r = await fetch(`${window.location.origin}/student/request-voucher`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ student_email: sessionUser.email, item_code: fv, generated_token: randomToken })
            });
            const d = await r.json();
            if (r.ok) {
                document.getElementById('displayToken').innerText = randomToken;
                document.getElementById('studentTokenBox').style.display = 'block';
                alert("🎉 Meal Voucher registered successfully! Pass token " + randomToken + " to the cashier counter.");
            } else alert("❌ Request Blocked: " + d.detail);
        }

        async function providerLookupStudentVoucher() {
            if (!sessionUser) return alert("Session timeout.");
            const token = document.getElementById('providerTokenInput').value.trim();
            if (!token) return alert("Please enter the student's 5-digit verification token.");
            const r = await fetch(`${window.location.origin}/provider/lookup-token`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ input_token: token, cashier_provider_id: sessionUser.role })
            });
            const d = await r.json();
            if (r.ok) {
                document.getElementById('reviewStudentId').innerText = d.student_id;
                document.getElementById('reviewFoodDetails').innerText = d.food_details;
                document.getElementById('providerOrderReviewBox').style.display = 'block';
            } else {
                document.getElementById('providerOrderReviewBox').style.display = 'none';
                alert("❌ Terminal Rejection: " + d.detail);
            }
        }

        async function providerConfirmServed() {
            const token = document.getElementById('providerTokenInput').value.trim();
            if (!token) return alert("Missing voucher validation reference target.");
            const r = await fetch(`${window.location.origin}/provider/confirm-serve`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ input_token: token })
            });
            if (r.ok) {
                alert("✅ Success: Order confirmed as SERVED. Funds safely cleared to provider billing rows.");
                document.getElementById('providerTokenInput').value = '';
                document.getElementById('providerOrderReviewBox').style.display = 'none';
            } else alert("❌ Verification Error.");
        }

        async function loadAdminStats() {
            if (!sessionUser) return;
            try {
                const r = await fetch(`${window.location.origin}/admin/stats`);
                const d = await r.json();
                if (r.ok && document.getElementById('adminTotalSyncs')) {
                    document.getElementById('adminTotalSyncs').innerText = d.total_syncs;
                    document.getElementById('cashADay').innerText = d.a_day_cash.toLocaleString() + " Frw";
                    document.getElementById('cashAWeek').innerText = d.a_week_cash.toLocaleString() + " Frw";
                    document.getElementById('cashBDay').innerText = d.b_day_cash.toLocaleString() + " Frw";
                    document.getElementById('cashBWeek').innerText = d.b_week_cash.toLocaleString() + " Frw";
                }
} catch (e) { console.log("Ledger refresh error"); }
}
        async function adminProcessBulkCsvUpload() {
            if (!sessionUser) return alert("Session timeout.");
            const fileInput = document.getElementById('adminCsvFileInput');
            if (fileInput.files.length === 0) return alert("Please select a student CSV file roster first.");
            const file = fileInput.files;
            const reader = new FileReader();
            reader.onload = async function(e) {
                const text = e.target.result;
                const lines = text.split("\\n").map(l => l.trim()).filter(l => l.length > 0);
                lines.shift(); 
                let successCount = 0;
                for (let line of lines) {
                    const columns = line.split(",").map(c => c.trim());
                    if (columns.length < 2) continue;
                    const [fullName, studentEmail] = columns;
                    const predictedResidence = successCount % 2 === 0 ? "Infinity Hostel" : "Soual Hostel";
                    try {
                        const r = await fetch(`${window.location.origin}/auth/signup`, {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({ name: fullName, email: studentEmail, password: "alu123", role: "student", residence: predictedResidence })
                        });
                        if (r.ok) successCount++;
                    } catch (err) {}
                }
                alert("🎉 Bulk provisioned " + successCount + " students automatically! Passwords defaulted to: alu123");
                fileInput.value = '';
                loadAdminStats();
            };
            reader.readAsText(file);
        }

        function triggerHostelRosterDownload(targetHostelName) {
            window.open(`${window.location.origin}/admin/export-hostel-pdf?residence=${encodeURIComponent(targetHostelName)}`, '_blank');
        }
    </script>
</body>
</html>"""
# Thread presentation fragments into a master engine template
HTML_TEMPLATE = PART_A1 + PART_A2 + PART_A3 + PART_B1
