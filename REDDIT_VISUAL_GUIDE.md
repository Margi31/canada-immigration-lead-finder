# Reddit Setup: Visual Clicking Guide & Alternatives 📍

## EASIEST WAY: Use Interactive Helper

```bash
python reddit_credentials_helper.py
```

This will:
✅ Open Reddit in your browser
✅ Guide you step-by-step
✅ Copy credentials for you
✅ Save to .env automatically

**No confusing instructions needed!**

---

## Where to Click: Visual Map

### Page 1: Reddit Home
```
https://www.reddit.com
┌────────────────────────────────────────┐
│ Top Right Corner:                      │
│                                        │
│ [Your Username] ▼                      │
│     ↓                                  │
│ ├─ Your profile                        │
│ ├─ User settings      ← CLICK THIS     │
│ ├─ Notifications                       │
│ ├─ Messages                            │
│ ├─ Premium                             │
│ ├─ Logout                              │
│                                        │
└────────────────────────────────────────┘
```

### Page 2: User Settings
```
https://www.reddit.com/settings
┌────────────────────────────────────────┐
│ Left Sidebar:                          │
│                                        │
│ Account                                │
│ ├─ Account preferences                 │
│ ├─ Email & password                    │
│ ├─ Safety & privacy                    │
│ ├─ Notifications                       │
│ │                                      │
│ │ Manage                               │
│ ├─ Saved                               │
│ ├─ Communities                         │
│ ├─ About                               │
│ ├─ Apps        ← CLICK THIS            │
│ └─ Chat settings                       │
│                                        │
└────────────────────────────────────────┘
```

### Page 3: Apps Settings
```
https://www.reddit.com/prefs/apps
┌────────────────────────────────────────┐
│ "Apps" tab opened                      │
│                                        │
│ List of apps (if you have any):        │
│ ├─ App 1                               │
│ ├─ App 2                               │
│ └─ (empty area below)                  │
│                                        │
│ ▼ Scroll down to find:                 │
│                                        │
│ [Create another app...] button         │
│     ↓ OR                               │
│ [Create an app] button                 │
│                                        │
│ Click this button!                     │
└────────────────────────────────────────┘
```

### Page 4: Create App Form
```
┌────────────────────────────────────────┐
│ Create app form:                       │
│                                        │
│ name:                                  │
│ [________________]                     │
│ Type: CanadaImmigrationBot             │
│                                        │
│ app type:  (Choose one)                │
│ ◉ script   ← SELECT THIS ONE           │
│ ○ web app                              │
│ ○ installed app                        │
│                                        │
│ description:                           │
│ [________________]                     │
│ Lead finder for immigration            │
│                                        │
│ about url: (optional)                  │
│ [________________] (leave blank)       │
│                                        │
│ redirect uri:                          │
│ [________________]                     │
│ http://localhost:8080                  │
│                                        │
│ [Create app] button                    │
│     ↓                                  │
│     Click it!                          │
│                                        │
└────────────────────────────────────────┘
```

### Page 5: Your Created App
```
┌────────────────────────────────────────┐
│ CanadaImmigrationBot (script)          │
│                                        │
│ Client ID:                             │
│ a1b2c3d4e5f6g7h                        │
│     ↑                                  │
│ COPY THIS                              │
│                                        │
│ Secret:  [show]                        │
│ ••••••••••••••••••••••••••••••          │
│     ↓ click "show" first               │
│     ↓ then copy                        │
│ personal use script credential         │
│                                        │
│ Redirect URI:                          │
│ http://localhost:8080                  │
│                                        │
│ Created:  2024-01-15                   │
│                                        │
└────────────────────────────────────────┘
```

---

## The Easy Path: Copy-Paste Instructions

### 1️⃣ Go here:
```
https://www.reddit.com/prefs/apps
```
(Copy and paste this into your browser address bar)

### 2️⃣ Find "Create app" button
```
Scroll down if you don't see it
```

### 3️⃣ Fill form:
```
name = CanadaImmigrationBot
type = script (radio button)
description = Lead finder for immigration
redirect_uri = http://localhost:8080
```

### 4️⃣ Click Create

### 5️⃣ Copy these two things:
```
Client ID (visible string)
Secret (click "show" first)
```

### 6️⃣ Paste here:
```
In your .env file:
REDDIT_CLIENT_ID=xxxxx
REDDIT_CLIENT_SECRET=xxxxx
```

Done! 🎉

---

## ALTERNATIVE 1: Use Demo Mode (No Reddit Setup)

If Reddit setup is too hard, I can set up a **demo mode** that uses sample data instead:

This is in `src/reddit_scraper.py` - we can modify it to:
- Use pre-scraped test data
- Simulate Reddit API
- Skip authentication

Want me to enable this? Just say "yes"!

---

## ALTERNATIVE 2: Use n8n Workflow (No Coding)

We already have a workflow file: `n8n/workflow.json`

Steps:
1. Download n8n (free): https://n8n.io/download
2. Import workflow.json
3. No Python needed!
4. No coding needed!

Visual workflow with no technical setup.

---

## ALTERNATIVE 3: Use Pre-Made Sample Data

```
output/sample_leads.csv
```

Already has 15 qualified leads!

You can:
- Import these to Google Sheets
- Send to Telegram
- Analyze immediately
- No Reddit API needed!

---

## If You're Still Stuck

### Quick Fixes (Try These First):

1. **Is your account 3+ days old?**
   - If brand new, wait 3 days
   - Reddit blocks new accounts from creating apps

2. **Are you signed in?**
   - Check top right corner
   - Should see your username

3. **Are you on the right page?**
   - URL: https://www.reddit.com/prefs/apps
   - Copy-paste to be sure

4. **Try a different browser:**
   - Chrome → Firefox
   - Firefox → Edge
   - Incognito/Private mode

5. **Check "Developed applications":**
   - Not "Authorized applications"
   - Must be "Developed applications" tab

### Still Stuck?

Post on Reddit: https://www.reddit.com/r/redditdev/
- Super helpful community
- Reddit staff sometimes help
- Include screenshot of where you're stuck

---

## NO Reddit Setup Needed: Use These Instead

### Option A: Use Sample Data
```bash
python main.py
# Uses pre-made sample_leads.csv
```

### Option B: Use API with No Auth
```python
# Some immigration APIs need no keys:
# - Gov Canada APIs
# - Public immigration databases
# - News feeds
```

### Option C: Hybrid Approach
```
1. Use sample data for testing
2. Add Reddit credentials later when ready
3. Start getting results NOW
```

Want me to implement any of these? 👇

---

## Testing Without Reddit

```bash
# Test just Claude AI:
python -c "from posts.ai_qualifier import AIQualifier; AIQualifier()"

# Test just Telegram:
python -c "from Sheets.telegram_notifier import TelegramNotifier; TelegramNotifier()"

# Test just Google Sheets:
python -c "from Claude.sheets_uploader import SheetsUploader; SheetsUploader()"

# Test everything with dummy Reddit:
python main.py
# (Won't scrape Reddit, but will show structure)
```

---

## Still Want Reddit Setup? Let's Debug

Tell me:

1. **What page are you on?**
   - Home
   - Settings
   - Apps page
   - Create app form

2. **What do you see?**
   - No button
   - Page is blank
   - Can't find section
   - Error message

3. **What's your Reddit username?**
   - (Just first letter + number for privacy)
   - Example: M1...

4. **Screenshot?**
   - Right-click → Screenshot or press Print Screen
   - Or describe what's on the page

I can help you solve it! 🔧

---

## Run the Interactive Helper

```bash
python reddit_credentials_helper.py
```

This is the EASIEST way - it:
- Opens browser for you
- Asks what to do
- Guides each click
- Saves credentials
- Tests when done

**Seriously, just run this command above! ⬆️**

---

## Summary

| Method | Effort | Time | Works |
|--------|--------|------|-------|
| Interactive Helper | ⭐ (Easiest) | 5 min | ✅✅✅ |
| Manual Setup | ⭐⭐ (Medium) | 10 min | ✅✅ |
| Sample Data | ⭐ (Instant) | 1 min | ✅ (demo) |
| Alternative API | ⭐⭐⭐ (Hard) | 30 min | ✅ |

**Recommendation: Run the helper!**

```bash
python reddit_credentials_helper.py
```

---

Need immediate help? I'm here! 🚀
