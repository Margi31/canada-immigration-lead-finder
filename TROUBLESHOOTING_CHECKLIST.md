# Reddit API Troubleshooting Checklist ✅

## Before You Start

Use this checklist to verify everything BEFORE running the scripts.

---

## 1️⃣ REDDIT ACCOUNT CHECK

```
☐ Do you have a Reddit account?
  If NO: Go to https://www.reddit.com/signup and create one

☐ Is your account 3+ days old?
  If NO: Reddit blocks new accounts. Wait 3 days, then try again
  
☐ Are you signed in?
  If NO: Sign in at https://www.reddit.com/login
```

---

## 2️⃣ BROWSER CHECK

```
☐ Are you using a modern browser?
  ✓ Chrome (latest)
  ✓ Firefox (latest)
  ✓ Edge (latest)
  ✓ Safari (latest)
  
☐ Try these if stuck:
  ☐ Clear browser cache (Ctrl+Shift+Delete)
  ☐ Try Incognito/Private mode
  ☐ Try a different browser
```

---

## 3️⃣ REDDIT PREFERENCES PAGE CHECK

```
☐ Go to: https://www.reddit.com/prefs/apps

☐ Can you see the page?
  If NO:
    • Try refreshing (Ctrl+R or F5)
    • Sign out and back in
    • Try different browser
    • Try mobile app instead

☐ Do you see an "Apps" section?
  If NO:
    • Try going to: https://www.reddit.com/settings
    • Click "Apps" in left sidebar
    • Then scroll to "Apps" section
```

---

## 4️⃣ CREATE APP BUTTON CHECK

```
☐ Look for one of these buttons:
  ☐ "Create another app..."
  ☐ "Create an app"
  ☐ "Create application"
  ☐ "New app" button
  ☐ "+" icon

☐ Can't find it?
  Try:
    • Scroll to BOTTOM of page (press End key)
    • Refresh page (Ctrl+R)
    • Try different browser
    • Try Reddit mobile app
```

---

## 5️⃣ APP CREATION FORM CHECK

When you click create button, you should see a form with:

```
✓ App name field
✓ App type selector (script, web app, installed app)
✓ Description field
✓ Redirect URI field
✓ Create button
```

**Checklist:**
```
☐ App name field visible?
☐ App type selector visible?
☐ Redirect URI field visible?
☐ Create button visible?

If any missing:
  • Browser might have blocked content
  • Try different browser
  • Try disabling ad blocker
  • Try private/incognito mode
```

---

## 6️⃣ FORM FILL CHECK

Fill the form with these EXACT values:

```
☐ App name: CanadaImmigrationBot
  (Check: No spaces before/after, exact spelling)

☐ App type: script (MUST be selected, not web app)
  (Check: Radio button is filled)

☐ Description: Lead finder for immigration
  (Check: Exact text, no typos)

☐ Redirect URI: http://localhost:8080
  (Check: http not https, :8080 not :3000)
```

---

## 7️⃣ APP CREATION CHECK

```
☐ Did you click "Create app"?
☐ Did page refresh?
☐ Do you see your app listed?
  (Shows: "CanadaImmigrationBot (script)")

If NO:
  • Form might have errors
  • Try again with exact values
  • Clear browser cache and try again
```

---

## 8️⃣ CREDENTIALS VISIBILITY CHECK

After app is created, you should see:

```
App name: CanadaImmigrationBot (script)

Client ID:
[14-character string here]
(visible immediately)

Secret:
[hidden - says "show" or eye icon]
(click "show" or eye to reveal)

Redirect URI:
http://localhost:8080

Created: [date]
```

**Checklist:**
```
☐ Client ID visible? (14+ characters)
☐ Secret field visible? (with show/hide option)
☐ Can you click "show" to reveal secret?
☐ Redirect URI shows http://localhost:8080?
```

---

## 9️⃣ CREDENTIALS COPY CHECK

```
☐ Click on Client ID field
☐ Select all (Ctrl+A)
☐ Copy (Ctrl+C)
☐ Paste somewhere to verify (Ctrl+V)

Verify:
  ☐ No spaces at beginning
  ☐ No spaces at end
  ☐ All characters visible
  ☐ Correct length (10-20 chars)

Then for Secret:
☐ Click "show" to reveal
☐ Click on Secret field
☐ Select all (Ctrl+A)
☐ Copy (Ctrl+C)
☐ Paste somewhere to verify

Verify:
  ☐ Starts with letters/numbers (no spaces)
  ☐ About 25-35 characters
  ☐ No spaces at beginning or end
```

---

## 🔟 .ENV FILE CHECK

```
☐ .env file created in project root?
  (Should be: c:\Users\Margi\Downloads\canada-immigration-lead-finder\.env)

☐ Contains:
  REDDIT_CLIENT_ID=xxxxx
  REDDIT_CLIENT_SECRET=xxxxx
  REDDIT_USER_AGENT=CanadaImmigrationLeadFinder/1.0

☐ Values are NOT empty?
☐ Values are NOT surrounded by quotes?
☐ No extra spaces around = sign?

Correct format:
REDDIT_CLIENT_ID=a1b2c3d4e5f6g7h    ✓
REDDIT_CLIENT_ID = a1b2c3d4e5f6g7h   ✗ (spaces around =)
REDDIT_CLIENT_ID="a1b2c3d4e5f6g7h"   ✗ (quotes)
```

---

## 1️⃣1️⃣ TEST CONNECTION

```bash
# Run this command:
python test_apis.py

# You should see:
✅ Reddit API connection: SUCCESS

# If you see:
❌ Reddit API connection: FAILED
Error: received 401 HTTP response

Then:
  • Go back to .env file
  • Copy credentials again (fresh copy)
  • Check for typos
  • Wait 5 minutes for Reddit to sync
  • Try again
```

---

## PROBLEM SOLVER

### Problem: "Page doesn't load"
```
Solution 1: Hard refresh
  • Ctrl+Shift+R (Chrome/Firefox)
  • Cmd+Shift+R (Mac)
  
Solution 2: Clear cache
  • Settings → Clear browsing data
  
Solution 3: Try different browser
  Chrome → Firefox → Edge
```

### Problem: "Can't find create button"
```
Solution 1: Scroll down
  • Press End key to go to bottom
  
Solution 2: Check section
  • Should be under "Apps" section
  • Not "Authorized applications"
  
Solution 3: Try mobile app
  • Download Reddit app
  • Settings → Apps
  • Create from there
```

### Problem: "Form won't submit"
```
Solution 1: Check required fields
  • Name: not empty
  • Type: script selected
  • Redirect URI: has value
  
Solution 2: Check values
  • App name: CanadaImmigrationBot (exact)
  • Type: script (radio button filled)
  • URI: http://localhost:8080 (http not https)
  
Solution 3: Browser issue
  • Disable ad blocker
  • Try private mode
  • Try different browser
```

### Problem: "Can't find credentials"
```
Solution 1: Scroll on credentials page
  • Should see Client ID at top
  • Should see Secret below
  • Both on same page
  
Solution 2: Check you're looking at right app
  • Should say "script" after app name
  • Should be your newly created app
  
Solution 3: Create new app
  • Maybe something went wrong
  • Create app again
  • Try immediately after creation
```

### Problem: "API says 401 error"
```
This means credentials are wrong

Solution 1: Re-copy credentials
  • Don't type - use Ctrl+A and Ctrl+C
  • Fresh copy from Reddit
  
Solution 2: Check for typos
  • Compare character by character
  • Check no spaces
  
Solution 3: Wait and retry
  • Sometimes Reddit takes 5 min to sync
  
Solution 4: Create new app
  • Delete old app (edit button → delete)
  • Create brand new app
  • Try again
```

---

## QUICK CHECKLIST (Print This)

```
BEFORE RUNNING SCRIPT:

Account:
  ☐ Account created
  ☐ Account is 3+ days old
  ☐ Signed in to Reddit

Browser:
  ☐ Using modern browser
  ☐ Cache cleared
  ☐ Not in private mode (try regular mode)

Reddit Prefs:
  ☐ Visited https://www.reddit.com/prefs/apps
  ☐ Found "Apps" section
  ☐ Found "Create app" button

Form:
  ☐ Filled with exact values
  ☐ App type is "script"
  ☐ Redirect URI is http://localhost:8080

Credentials:
  ☐ Client ID copied (no spaces)
  ☐ Client Secret revealed and copied (no spaces)
  ☐ Both pasted into .env file

Testing:
  ☐ Ran: python test_apis.py
  ☐ Saw: ✅ Reddit API connection: SUCCESS
```

---

## IF ALL ELSE FAILS

### Option 1: Use Interactive Helper
```bash
python reddit_credentials_helper.py
```
(Does everything for you step by step)

### Option 2: Use Demo Mode
```bash
python demo.py
```
(Doesn't need Reddit at all)

### Option 3: Post for Help
```
Reddit: https://www.reddit.com/r/redditdev/
Include:
  • Screenshot of where you're stuck
  • What you've tried
  • Your browser type
  • Exact error message
```

### Option 4: Ask Me
Just tell me what's not working and I'll:
  • Create a detailed custom guide
  • Write a script to do it for you
  • Set up alternative APIs
  • Fix any issues

---

## SUCCESS SIGNS ✅

When everything is working:

```
1. Can see your app on Reddit
2. Can copy Client ID and Secret
3. .env file has both values
4. Run test_apis.py shows ✅ SUCCESS
5. Can run python main.py
6. Gets results in output/sample_leads.csv
```

---

## TIME LIMITS

```
Account wait: 3 days (if new)
Reddit sync: 5 minutes (after creating app)
First run: 2-3 minutes (qualifies leads)
```

---

**You got this! Let me know if you get stuck on any step!** 🚀
